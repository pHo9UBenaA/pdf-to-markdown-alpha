"""PDF to Markdown conversion script using PyMuPDF and markdownify."""

import argparse
import sys
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF
from markdownify import markdownify as md


def convert_pdf_to_markdown(
    pdf_path: Path,
    output_dir: Path,
    disable_image: bool = False,
    output_filename: Optional[str] = None,
) -> Path:
    """Convert PDF file to Markdown format.

    Args:
        pdf_path: Path to the input PDF file
        output_dir: Directory to save the converted Markdown file
        disable_image: If True, skip image extraction
        output_filename: Optional custom output filename

    Returns:
        Path to the created Markdown file
    """
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine output filename
    if output_filename is None:
        output_filename = pdf_path.stem + ".md"

    output_path = output_dir / output_filename

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
                        # Create images directory
                        images_dir = output_dir / "images"
                        images_dir.mkdir(exist_ok=True)

                        # Save image
                        image_filename = f"page_{page_num + 1}_img_{img_index + 1}.png"
                        image_path = images_dir / image_filename
                        pix.save(image_path)

                        # Add image reference to markdown
                        markdown_content.append(
                            f"![Image {img_index + 1}](images/{image_filename})\n"
                        )

                    pix = None  # Free memory

    finally:
        doc.close()

    # Write markdown content to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))

    return output_path


def main():
    """Main function to handle command line arguments and execute conversion."""
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown using PyMuPDF and markdownify"
    )
    parser.add_argument("pdf_path", type=Path, help="Path to the PDF file to convert")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("docs/output"),
        help="Directory to save the converted Markdown file (default: docs/output)",
    )
    parser.add_argument(
        "--disable-image", action="store_true", help="Disable image extraction"
    )
    parser.add_argument(
        "--output-filename",
        type=str,
        help="Custom output filename (default: [input_filename].md)",
    )

    args = parser.parse_args()

    # Validate input file
    if not args.pdf_path.exists():
        print(f"Error: PDF file not found: {args.pdf_path}")
        sys.exit(1)

    if not args.pdf_path.suffix.lower() == ".pdf":
        print(f"Error: Input file must be a PDF: {args.pdf_path}")
        sys.exit(1)

    try:
        output_path = convert_pdf_to_markdown(
            args.pdf_path, args.output_dir, args.disable_image, args.output_filename
        )
        print(f"Successfully converted PDF to Markdown: {output_path}")

        if not args.disable_image:
            images_dir = args.output_dir / "images"
            if images_dir.exists() and any(images_dir.iterdir()):
                print(f"Images extracted to: {images_dir}")

    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
