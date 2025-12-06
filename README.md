# code-challenges

Short solutions for selected FreeCodeCamp daily challenges and LeetCode problems, organized with tests and coverage.

## Project Overview

This repository contains solutions for code challenges their unit tests. It's intended for practicing problem-solving and verifying solutions with `unittest`.

## Repository Structure

- **`solutions/`**: Implementation files for each challenge (e.g. `ai_detector.py`, `convert_list_item.py`).
- **`tests/`**: Unit tests that validate the behavior of the corresponding functions in `solutions/`.
- **`requirements.txt`**: Python dependencies used for running tests and tooling.

## Requirements

- Python 3.8+ (recommend 3.10+)
- Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

Run the test suite with `unittest` from the repository root:

```bash
python -m unittest discover
```

To run tests with coverage and generate coverage report:

```bash
chmod +x scripts/generate_coverage.sh # first time
scripts/generate_coverage.sh
```

## Contributing

- Add new solutions under `solutions/` and tests under `tests/`.
- Keep functions small and pure where possible to simplify testing.
- Follow existing naming and project conventions.

## Next Steps

- Run the tests and review coverage.
- Add more challenges and corresponding tests.
