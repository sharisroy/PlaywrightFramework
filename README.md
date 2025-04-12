# Playwright API Testing with Pytest

This project utilizes **Playwright** in combination with **Pytest** to provide an efficient, scalable, and automated framework for **API testing**. The setup supports structured test execution, fixtures, markers, parallel test execution, and generates detailed reports for effective analysis and investigation of test results.

While **Playwright** is traditionally used for browser automation, it is leveraged here for API testing without requiring the launch of a browser. This makes Playwright a versatile tool for interacting with APIs. It supports a variety of HTTP methods such as **GET, POST, PUT, PATCH**, and **DELETE**, along with powerful capabilities for data handling, assertions, and environment configuration. This makes it an ideal choice for comprehensive **end-to-end API validation**.

---

## 🚀 Getting Started

### Required Packages
To get started, you need to install the necessary dependencies. Run the following commands:

```bash
pip install pytest
pip install pytest-playwright
pip install pytest-xdist
playwright install
```

---

## 💻 Running Tests

### Basic Commands
If your test files are located in a different directory, make sure to navigate to that directory first. Then, use the following commands to run your tests:

| Action                              | Command |
|-------------------------------------|---------|
| Run all tests                       | `pytest -s` |
| Run a specific test file            | `pytest test_file.py` |
| Run a specific test class/module    | `pytest test_file.py::TestClassName` |
| Run a test by method name           | `pytest -k "partial_method_name"` |
| Run tests with a specific marker (e.g., smoke) | `pytest -m smoke -v` |
| Run in headed mode (useful for UI testing) | `pytest test_file.py::test_case --headed` |
| Run tests in parallel using 4 worker processes | `pytest -n 4` |

---

## 🛠️ Pytest Fixtures

**Fixtures** are reusable setup routines used before and after tests to ensure that the necessary environment is in place.

### Example:
```python
@pytest.fixture(scope="function")
def setup_data():
    # Setup logic
    yield
    # Teardown logic
```

### Fixture Scopes:
- **`function`** (default): Runs before and after each test function.
- **`class`**: Runs once per test class, shared across all test functions in the class.
- **`module`**: Runs once per module (test file), shared across all test functions and classes in the module.
- **`session`**: Runs once per test session, ideal for setup tasks like initializing a database or API connection.

---

## 🏷️ Pytest Markers

Markers are used to tag and organize tests for easier filtering and execution.

### Common Markers:
- **`@pytest.mark.skip`**: Skip a test.
- **`@pytest.mark.smoke`**: Tag a test as part of the smoke test suite.
- **`@pytest.mark.regression`**: Tag a test as part of the regression test suite.

### Example:
```python
@pytest.mark.smoke
def test_login():
    assert True
```

Run the **smoke** suite with:
```bash
pytest -m smoke -v
```

---

## ♻️ Parallel Test Execution

To speed up test execution by running tests in parallel across multiple CPUs:

```bash
pytest -n 4
```

Make sure you have `pytest-xdist` installed to enable parallel execution.

---

## 🚫 Skipping Tests

To exclude a test temporarily, you can use the `skip` marker:

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    pass
```

---

## 📁 Project Structure

Here’s an example of the project structure:

```
project_root/
├── tests/
│   ├── test_login.py
│   └── test_api.py
├── fixtures/
│   └── common_fixtures.py
├── reports/
│   └── test_report.html
├── conftest.py
├── requirements.txt
└── README.md
```

---

Happy Testing! 🚀

