# Playwright API Testing with pytest Framework

This project uses Playwright with Pytest-BDD for automated API testing. It supports structured execution, fixtures, markers, parallel testing, and generates reports for further investigation.

## 🚀 Getting Started

### Required Packages

Install all dependencies:

```bash
pip install pytest
pip install pytest-playwright
pip install pytest-xdist
playwright install
```

To generate `requirements.txt` with all installed dependencies, use:

```bash
pip freeze > requirements.txt
```

This command will create a `requirements.txt` file with all the necessary packages.

---

### 💻 Running Tests

#### Basic Commands

| Action | Command |
|--------|---------|
| Run all tests | `pytest -s` |
| Run a specific file | `pytest tests/test_login.py` |
| Run by test method name | `pytest -k "partial_method_name"` |
| Run tests with marker (e.g., smoke) | `pytest -m smoke -v` |
| Run in headed mode (for UI, if needed) | `pytest tests/test_file.py::test_case --headed` |
| Run tests in parallel | `pytest -n 4` |



---

---

### 🏷️ Pytest Markers

Markers help organize and filter tests.

#### Common Markers:

```python
@pytest.mark.skip  # Skip a test.
@pytest.mark.smoke  # Tag a test as part of smoke suite.
@pytest.mark.regression  # Tag a test as part of regression suite.
```

Run with:

```bash
pytest -m smoke -v
```

---

### 🔄 Parallel Test Execution

To speed up test execution using multiple CPUs:

```bash
pytest -n 4
```

Make sure `pytest-xdist` is installed.

---

### 📁 Folder Structure (BDD Version)

```plaintext
project_root/
├── features/
│   ├── login.feature
│   └── order.feature
├── steps/
│   ├── test_login.py
│   └── test_order.py
├── data/
│   └── credentials.json
├── config/
│   └── config.json
├── conftest.py
├── requirements.txt
└── README.md
```

Happy Testing! 🚀

