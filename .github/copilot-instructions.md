# Copilot Instructions for code-challenges

## Project Overview

A Python repository of LeetCode/FreeCodeCamp problem solutions with comprehensive unit testing, coverage reporting, and linting. This is a learning-focused project for practicing algorithmic problem-solving with clean, testable code.

## Directory Structure & Conventions

- **`solutions/`**: Pure Python implementation files for each challenge. Functions are documented with docstrings explaining the problem statement, constraints, and approach. Example: `valid_anagram.py`, `solve_sudoku.py`
- **`tests/`**: Unit tests using `unittest` framework with `parameterized` library for data-driven tests. File naming strictly follows `test_<solution_name>.py`. Example: `test_valid_anagram.py` tests `solutions/valid_anagram.py`
- **`scripts/`**: Executable shell scripts for development workflows (`run_lint.sh`, `generate_coverage.sh`)

## Testing Patterns

All tests follow these conventions:

1. **Use `unittest.TestCase`** as the base class for all test classes
2. **Use `@parameterized.expand()`** decorator for data-driven tests instead of writing multiple test methods. Example from `test_valid_anagram.py`:
   ```python
   @parameterized.expand([
       ("anagram", "nagaram"),
       ("listen", "silent"),
       ("", ""),
   ])
   def test_given_valid_anagram_then_return_true(self, first: str, second: str):
       self.assertTrue(is_anagram(first, second))
   ```

3. **Naming convention**: Use descriptive test method names following the `test_given_<input>_then_<expected_output>` pattern (see `test_best_time_to_sell_stock.py` for extensive examples with edge cases, monotonic patterns, and realistic data)

4. **Comprehensive edge case coverage**: Always include empty inputs, single-element inputs, boundary conditions, and realistic scenarios. See `test_best_time_to_sell_stock.py` for the exemplary test case organization pattern

5. **Test organization**: Group test cases by category using comments (e.g., `# --- Edge cases ---`, `# --- Monotonic patterns ---`)

## Development Workflows

### Running Tests
```bash
python -m unittest discover
```

### Generating Coverage Reports
```bash
scripts/generate_coverage.sh
```
This command runs tests with coverage tracking, generates a terminal report, and opens an HTML coverage report in the default browser. Coverage configuration is in `.coveragerc` (omits `__init__.py` files and main blocks).

### Running Linter
```bash
scripts/run_lint.sh
```
Uses Flake8 for style and error checking. See `requirements.txt` for linting tools: `flake8`, `pycodestyle`, `pyflakes`, `mccabe`.

## Code Style & Type Hints

- **Type annotations** are mandatory for function parameters and return types. Example: `def is_anagram(s: str, t: str) -> bool:`
- Use `from collections import defaultdict` or other standard library data structures for algorithmic efficiency
- Keep functions pure (no side effects) and small to simplify testing
- Write docstrings for all solution functions explaining the problem, constraints, and approach (see `solve_sudoku.py` for format)

## Python Environment

- **Minimum Python version**: 3.14+
- **Virtual environment**: Use `.venv/` with `python -m venv .venv`
- **Dependency management**: Use `pip` with `requirements.txt`. Always run `pip freeze > requirements.txt` after installing new packages
- **Key dependencies**: `unittest` (built-in), `parameterized`, `coverage`, `flake8`

## Adding New Solutions

When adding a new challenge solution:

1. Create `solutions/<challenge_name>.py` with comprehensive docstring (problem statement, constraints)
2. Define type-annotated functions implementing the solution
3. Create corresponding `tests/test_<challenge_name>.py` using parameterized tests with edge case coverage
4. Run `python -m unittest discover` to verify tests pass
5. Run `scripts/generate_coverage.sh` to ensure adequate coverage
6. Run `scripts/run_lint.sh` to check code style

## Critical Files & Patterns to Reference

- **`solutions/valid_anagram.py`**: Simple algorithmic solution with efficient hash-based approach
- **`solutions/solve_sudoku.py`**: Complex backtracking algorithm using helper functions and type aliases
- **`tests/test_valid_anagram.py`**: Minimal parameterized test pattern
- **`tests/test_best_time_to_sell_stock.py`**: Exemplary comprehensive test coverage with organized edge cases and realistic data scenarios
