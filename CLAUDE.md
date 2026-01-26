# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python repository of LeetCode/FreeCodeCamp coding challenge solutions with comprehensive unit testing, coverage reporting, and linting. Python 3.14+ required.

## Commands

```bash
# Run all tests
python -m unittest discover

# Run specific test file
python -m unittest tests.test_<name>

# Run linter (flake8)
scripts/run_lint.sh

# Generate coverage report (opens HTML in browser)
scripts/generate_coverage.sh
```

## Architecture

- **`solutions/`**: Pure Python implementations with type-annotated functions and docstrings explaining problem, constraints, and approach
- **`tests/`**: Unit tests following `test_<solution_name>.py` naming convention
- **`scripts/`**: Shell scripts for linting and coverage workflows

## Testing Patterns

- Use `unittest.TestCase` with `@parameterized.expand()` for data-driven tests
- Test method naming: `test_given_<input>_then_<expected_output>`
- Group test cases by category with comments (e.g., `# --- Edge cases ---`)
- Always cover: empty inputs, single elements, boundary conditions

Example:
```python
@parameterized.expand([
    ("anagram", "nagaram"),
    ("listen", "silent"),
])
def test_given_valid_anagram_then_return_true(self, first: str, second: str):
    self.assertTrue(is_anagram(first, second))
```

## Code Style

- Type annotations mandatory for all function parameters and return types
- Keep functions pure (no side effects) and small
- Write docstrings for solution functions explaining problem and approach

## Design Principles

**SOLID:**
- Single Responsibility: Each function solves one specific problem
- Open/Closed: Use helper functions to extend behavior without modifying core logic
- Liskov Substitution: Maintain consistent interfaces for similar solution patterns
- Interface Segregation: Keep function signatures minimal with only required parameters
- Dependency Inversion: Depend on abstractions (e.g., pass iterables, not concrete list types)

**DRY (Don't Repeat Yourself):**
- Extract repeated logic into helper functions
- Use parameterized tests instead of duplicating test methods
- Leverage standard library utilities (`collections`, `itertools`) over custom implementations

**KISS (Keep It Simple, Stupid):**
- Prefer readable solutions over clever one-liners
- Avoid premature optimization; prioritize correctness first
- Use straightforward data structures appropriate to the problem

**Clean Code:**
- Use descriptive, intention-revealing names for functions and variables
- Keep functions short and focused (ideally under 20 lines)
- Avoid magic numbers; use named constants or explain in comments
- Structure code to read top-to-bottom like a narrative

## Adding New Solutions

1. Create `solutions/<name>.py` with docstring and type-annotated functions
2. Create `tests/test_<name>.py` with parameterized tests and edge cases
3. Run tests, coverage, and linter before committing

## Reference Files

- `solutions/valid_anagram.py`: Simple hash-based solution pattern
- `solutions/solve_sudoku.py`: Complex backtracking with helper functions
- `tests/test_best_time_to_sell_stock.py`: Exemplary comprehensive test coverage
