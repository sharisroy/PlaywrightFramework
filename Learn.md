1. pip3 install pytest
2. pip install pytest-playwright
3. playwright install
4. pip install pytest-xdist - The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution


## How to run from comment line

1. All test case file - pytest -s
2. Single File - pytest file_name
3. Single Module - pytest file_name::module_name
4. Run using test Name - @pytest.mark.test_name -v (smoke, regression)
5. Run using test method name - pytest -k part_of_method_name
6. Run headed browser - pytest test_file_name.py::test_module_name --headed
7. Run using n number of worker - pytest -n number_of_worker



### pytest.fixture
    - A fixture in testing is a setup that provides a known precondition before running a test and ensures proper cleanup after the test. Fixtures help maintain test reliability by ensuring each test starts with a consistent state.
        -- scope="function" -> The fixture is created before each test function and destroyed after the function completes. Useful when you need fresh data for every test.
        -- scope="class" -> The fixture is created once per test class and is shared among all test methods within the class. Useful when test cases in a class can share the same setup.
        -- scope="module" -> The fixture is created once per module (file) and shared across all test functions/classes in that module. Useful when tests in the same file can reuse the same setup.
        -- scope="session" -> The fixture is created once for the entire pytest session (across multiple test files). Useful for database connections, API authentication, or other expensive setups.

### @pytest.mark
    - pytest.mark.skip is a function that skips a test or a fixture during execution. It is useful when a test should not run under certain conditions.
    - @pytest.mark.test_name @pytest.mark.smoke




