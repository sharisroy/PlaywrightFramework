# Playwright API Testing with BDD (pytest-bdd)

This project uses Playwright with Pytest-BDD for automated API testing. It supports BDD-style test scenarios, structured execution, fixtures, markers, parallel testing, and generates reports for further investigation.

## 🚀 Getting Started

### Required Packages

Install all dependencies:

```bash
pip install pytest
pip install pytest-playwright
pip install pytest-bdd
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

### 🦢 Feature Files (BDD)

Feature files describe your test cases in plain English.

#### Example: `features/login.feature`

```gherkin
Feature: Login Functionality

  Scenario Outline: Successful login with valid credentials
    Given a user with email "<userEmail>" and password "<userPassword>"
    When the user sends a login request
    Then the login should be successful
    And the response should contain a token

    Examples:
      | userEmail              | userPassword |
      | sqa.haris@gmail.com     | H@12345bd    |
```

#### Example: `features/order.feature`

```gherkin
Feature: Order Creation

  Scenario: Create order with valid product ID
    Given a valid authorization token
    When a user creates an order with product ID "67a8dde5c0d3e6622a297cc8"
    Then the order should be placed successfully

  Scenario: Create order with invalid product ID
    Given a valid authorization token
    When a user creates an order with product ID "67a8dde5c0d3e6622a297000"
    Then the API should return "Wrong Product ID"
```

---

### 🛠️ Fixtures & Setup

Fixtures are reusable setups used before and after tests.

Defined in `conftest.py`, e.g.:

#### `api_context`: Initializes Playwright request context

```python
@pytest.fixture(scope="module")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url=BASE_URL, extra_http_headers=HEADERS)
    yield request_context
    request_context.dispose()
```

#### `auth_token`: Authenticates and returns a token

```python
@pytest.fixture(scope="module")
def auth_token(api_context):
    response = api_context.post('/auth', json=credentials)
    return response.json()['token']
```

#### `latest_order_id`: Gets the latest order ID

```python
@pytest.fixture(scope="module")
def latest_order_id(api_context):
    response = api_context.get('/orders')
    return response.json()[0]['id']
```

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

