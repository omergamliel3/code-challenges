# code-challenges

![code-challenges](https://img.shields.io/badge/github-repo-blue?logo=github)
![CI](https://github.com/omergamliel3/code-challenges/actions/workflows/python-app.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14%2B-blue)
![Coverage](https://img.shields.io/badge/coverage-local-green)

Solutions for selected FreeCodeCamp daily challenges and LeetCode problems, organized with tests, coverage and linter.

## 📌 Project Overview

This repository contains solutions for code challenges and their unit tests. It's intended for practicing problem-solving and verifying solutions.

## 🗂 Repository Structure

- **`solutions/`**: Implementation files for each challenge (e.g. `ai_detector.py`, `convert_list_item.py`).
- **`tests/`**: Unit tests that validate the behavior of the corresponding functions in `solutions/`.
- **`requirements.txt`**: Python dependencies used for running tests and tooling.

## ⚙️ Requirements

- Python **3.14+** (developed and tested with 3.14)
- Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 📦 Managing Dependencies

Install or remove a dependency
```bash
pip install <package_name>
pip uninstall <package_name>
```

Update dependencies
```bash
# update specific package
pip install --upgrade <package_name>
# or upgrade all from requirements
pip install --upgrade -r requirements.txt
```

Freeze current environment
```bash
# Save all installed packages and versions to requirements.txt
python -m pip freeze > requirements.txt
```

### Make scripts executable (one-time)
```bash
chmod +x scripts/run_lint.sh
chmod +x scripts/generate_coverage.sh
```

## 🧹 Running Linter

Run the linter (We are using Flake8)

```bash
scripts/run_lint.sh
```

The script will report errors, warnings and style issues in the terminal including information.

## 🧪 Running Tests

Run the test suite with `unittest` from the repository root:

```bash
python -m unittest discover
```

To generate coverage report:

```bash
scripts/generate_coverage.sh
```

The script will print output in the terminal and open UI coverage report in default browser

## 🤝 Contributing

- Add new solutions under `solutions/` and tests under `tests/`.
- Keep functions small and pure where possible to simplify testing.
- Follow existing naming and project conventions.

---

Built for learning, experimentation, and clean problem-solving.