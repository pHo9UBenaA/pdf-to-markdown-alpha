"""PDF to Markdown conversion script using PyMuPDF and markdownify."""

import argparse
import sys
from pathlib import Path
from typing import Optional, cast

import fitz
from markdownify import markdownify as md


def convert_pdf_to_markdown(
    pdf_path: Path,
    output_path: Optional[Path] = None,
    disable_image: bool = False,
) -> Path:
    """Convert PDF file to Markdown format.

    Args:
        pdf_path: Path to the input PDF file
        output_path: Path for the output Markdown file. If None, defaults to same name with .md extension
        disable_image: If True, skip image extraction

    Returns:
        Path to the created Markdown file
    """
    # Determine output path if not specified
    if output_path is None:
        output_path = pdf_path.with_suffix(".md")

    # Ensure parent directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Open PDF document
    doc = fitz.open(pdf_path)

    markdown_content = []

    try:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)

            # Extract text
            text = page.get_text()

            if text.strip():
                # Convert HTML-like formatting to Markdown
                markdown_text = md(text, heading_style="ATX")
                markdown_content.append(f"## Page {page_num + 1}\n\n{markdown_text}\n")

            # Extract images if not disabled
            if not disable_image:
                image_list = page.get_images(full=True)

                for img_index, img in enumerate(image_list):
                    # Get image data
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)

                    if pix.n - pix.alpha < 4:  # GRAY or RGB
                        # Create images directory relative to output file
                        images_dir = output_path.parent / "images"
                        images_dir.mkdir(exist_ok=True)

                        # Save image
                        image_filename = f"page_{page_num + 1}_img_{img_index + 1}.png"
                        image_path = images_dir / image_filename
                        pix.save(image_path)

                        # Add image reference to markdown
                        markdown_content.append(
                            f"![Image {img_index + 1}](images/{image_filename})\n"
                        )

                    del pix  # Free memory

    finally:
        doc.close()

    # Write markdown content to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))

    return output_path


def main() -> None:
    """Main function to handle command line arguments and execute conversion."""
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown using PyMuPDF and markdownify"
    )
    parser.add_argument("pdf_path", type=Path, help="Path to the PDF file to convert")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output Markdown file path (default: same name with .md extension)",
    )
    parser.add_argument(
        "--disable-image", action="store_true", help="Disable image extraction"
    )

    args = parser.parse_args()

    # Cast argparse attributes to proper types
    pdf_path = cast(Path, args.pdf_path)
    output = cast(Optional[Path], args.output)
    disable_image = cast(bool, args.disable_image)

    # Validate input file
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    if not pdf_path.suffix.lower() == ".pdf":
        print(f"Error: Input file must be a PDF: {pdf_path}")
        sys.exit(1)

    try:
        output_path = convert_pdf_to_markdown(pdf_path, output, disable_image)
        print(f"Successfully converted PDF to Markdown: {output_path}")

        if not disable_image:
            images_dir = output_path.parent / "images"
            if images_dir.exists() and any(images_dir.iterdir()):
                print(f"Images extracted to: {images_dir}")

    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
