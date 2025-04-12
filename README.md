# Playwright API Testing with Pytest

This project uses **Playwright** with **Pytest** for automated API testing. It supports structured test execution, fixtures, markers, parallel testing, and generates reports for further investigation.

---

## 🚀 Getting Started

### Required Packages
Install all dependencies:

```bash
pip install pytest
pip install pytest-playwright
pip install pytest-xdist
playwright install
```

---

## 💻 Running Tests

### Basic Commands
NB: If your test files are in a different directory, navigate to that directory first and then run the following commands:

| Action                              | Command |
|-------------------------------------|---------|
| Run all tests                       | `pytest -s` |
| Run a specific file                 | `pytest test_file.py` |
| Run a specific class/module         | `pytest test_file.py::TestClassName` |
| Run by test method name             | `pytest -k "partial_method_name"` |
| Run tests with marker (e.g., smoke) | `pytest -m smoke -v` |
| Run in headed mode (for UI)         | `pytest test_file.py::test_case --headed` |
| Run tests in parallel using 4 worker processes              | `pytest -n 4` |

---

## 🛠️ Pytest Fixtures

Fixtures are reusable setups used before and after tests.

### Example:
```python
@pytest.fixture(scope="function")
def setup_data():
    # Setup logic
    yield
    # Teardown logic
```

### Fixture Scopes:
- `function`: (default) Runs before and after each test function.
- `class`: Runs once per class, shared within the class.
- `module`: Runs once per file, shared across functions/classes.
- `session`: Runs once for the entire test session. Useful for DB/API setup.

---

## 🏷️ Pytest Markers

Markers help organize and filter tests.

### Common Markers:
- `@pytest.mark.skip` – Skip a test.
- `@pytest.mark.smoke` – Tag a test as part of smoke suite.
- `@pytest.mark.regression` – Tag a test as part of regression suite.

### Example:
```python
@pytest.mark.smoke
def test_login():
    assert True
```

Run with:
```bash
pytest -m smoke -v
```

---

## 🔄 Parallel Test Execution

To speed up test execution using multiple CPUs:

```bash
pytest -n 4
```

Make sure `pytest-xdist` is installed.

---

## 🚫 Skipping Tests

Use skip marker to exclude a test:
```python
@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    pass
```

---

## 📁 Folder Structure

```
project_root/
├── tests/
│   ├── test_login.py
│   └── test_api.py
├── fixtures/
│   └── common_fixtures.py
├── conftest.py
├── requirements.txt
└── README.md
```

---

Happy Testing! 🚀

