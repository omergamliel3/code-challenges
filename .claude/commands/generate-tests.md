# Generate Tests Command

Generate comprehensive unit tests for a solution file with full coverage validation.

## Input

Solution file path: $ARGUMENTS

## Workflow

### Step 1: Analyze the Solution

Read and analyze the solution file at `$ARGUMENTS`:
- Identify all public functions and their signatures
- Understand the problem being solved (from docstring)
- Note edge cases, constraints, and input types
- Identify code branches that need test coverage

### Step 2: Generate Tests (Hybrid Approach)

Create a test file following project conventions (do NOT use comments for grouping):

**Template Structure:**
- File location: `tests/test_<solution_name>.py`
- Use `unittest.TestCase` with `@parameterized.expand()`
- Test method naming: `test_given_<input>_then_<expected_output>`
- Create a base test class with common setup/utilities
- Group related test cases by creating separate classes that inherit from the base class

**Class Organization:**
```python
class TestSolutionNameBase(unittest.TestCase):
    """Base class with shared setup and utilities."""
    pass

class TestBasicCases(TestSolutionNameBase):
    """Standard input scenarios."""
    pass

class TestEdgeCases(TestSolutionNameBase):
    """Empty inputs, single elements, boundary conditions."""
    pass

class TestLargeInputs(TestSolutionNameBase):
    """Performance and scale scenarios (if applicable)."""
    pass

class TestSpecialCases(TestSolutionNameBase):
    """Problem-specific edge scenarios."""
    pass
```

**AI-Generated Test Cases:**
- Generate test cases based on solution analysis
- Distribute tests across appropriate classes:
  - `TestBasicCases` - standard input scenarios
  - `TestEdgeCases` - empty inputs, single elements, boundaries
  - `TestLargeInputs` - if applicable
  - `TestSpecialCases` - problem-specific scenarios

### Step 3: Review Before Saving

**IMPORTANT:** Before writing the test file, show the complete generated code to the user and ask for approval:
- Display the full test file content
- Ask: "Does this test file look good? Should I save it?"
- Wait for user confirmation before proceeding
- If user requests changes, modify and show again

### Step 4: Run Tests

After user approves and file is saved:
```bash
python -m unittest tests.test_<solution_name> -v
```

### Step 5: Verify 100% Coverage

Run coverage analysis on the specific solution file:
```bash
coverage run --source=solutions/<solution_name>.py -m unittest tests.test_<solution_name>
coverage report --fail-under=100
```

**If coverage is not 100%:**
1. Run `coverage report -m` to identify uncovered lines
2. Analyze what test cases are missing
3. Generate additional tests to cover the missing lines
4. Show the new tests to user for approval
5. Update the test file
6. Repeat until 100% coverage is achieved

### Step 6: Run Linter

Verify the test file passes linting:
```bash
flake8 tests/test_<solution_name>.py
```

Fix any linting issues found.

### Step 7: Final Summary

Report:
- Number of test classes created
- Number of test methods per class
- Coverage percentage (should be 100%)
- Linting status

## Example Usage

```
/generate-tests solutions/two_sum.py
```
