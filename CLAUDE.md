# Always: TDD

Practice Test-Driven Development (TDD) as advocated by Kent Beck and t_wada.

## Core Principles

### Red-Green-Refactor Cycle

- 🔴 Red: Write failing test that specifies expected behavior
- 🟢 Green: Implement minimal code to make test pass
- 🔵 Refactor: Improve code structure while maintaining green tests

### Development Philosophy

- Advance through single-step iterations (commit each complete cycle)
- Apply triangulation when generalizing from multiple test cases
- Use direct implementation for obvious solutions
- Maintain active test list at top of test files
- Prioritize uncertain areas in test creation sequence
- Apply fake implementation as valid starting strategy

## TDD Implementation Process

**Execute**: Complete Red-Green-Refactor cycle with immediate commit

1. **Create failing test**: Establish test that demonstrates required behavior
   (compilation failures acceptable)
2. **Achieve green state**: Apply simplest working solution - direct
   implementation, triangulation, or fake return values
3. **Execute refactoring**: Enhance code quality while preserving test success
4. **Record progress**: Commit completed cycle
5. **Expand test inventory**: Add emerging test scenarios to file header TODO
   list
6. **Maintain single focus**: Process one test case per cycle
7. **Continue iteration**: Initiate subsequent Red-Green-Refactor cycle

## Test List Management

- Place TODO test list in test file header comments using `- [ ]`
- Check off completed tests with `- [x]`
- Add new test ideas as they emerge during implementation
- Keep list visible for continuous reference

## Expected Outcomes

- Each cycle produces: one failing test → minimal passing code → improved
  structure → committed change
- Test list demonstrates: comprehensive coverage planning, priority-based
  execution, continuous expansion
- Implementation exhibits: incremental complexity growth, validated
  functionality, clean architecture

---

# Always: Git Commit

Use the following commit format:

```bash
git -c commit.gpgsign=false -c user.name='pHo9UBenaA' -c user.email='102408484+pHo9UBenaA@users.noreply.github.com' commit -m '[type]: [changes summary]' -m 'prompt: [user prompt]' -m '[changes report]'
```

`changes report` includes items specific to each `type`:

- test: Test additions, Coverage improvements, Quality assurance
- feat: Feature changes, Code improvements, Technical achievements
- refactor: Refactoring scope, Architectural improvements, Quality enhancements
- fix: Root cause analysis, Applied fixes, Verification results
- docs: Documentation updates, Target audience, Usability improvements
- perf: Performance improvements, Code optimizations, Technical results

---

# Always: Module Scoping

Keep all definitions properly scoped within modules.

**Avoid:**

- Global scope definitions
- Module-level global references

**Why:** They create hidden dependencies and make testing difficult

---

# Always: Comments

Write comments in English using Python docstring.

- File headers: Describe specifications
- Functions/constants: Focus on What/Why

---

# Always: Magic Literals

Extract magic literals (magic numbers, magic strings) into constants. e.g.:
`if (user.role === "admin")` to `if (user.role === ROLE_ADMIN)`

---

# Always: Code Organization

- Keep exports of functions to the necessary minimum to maintain clear
  architectural layers and readability
- Use early returns to minimize nesting and improve readability
- Remove dead code to prevent confusion and maintenance burden
