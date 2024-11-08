
# Pytest Selenium Base Framework

This repository is a base framework for automating web tests using **Pytest** and **Selenium**. It is designed for ease of use, modularity, and scalability. This framework provides a solid foundation to create, manage, and execute test cases for web applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Configuration](#configuration)
- [Writing Tests](#writing-tests)
- [Running Tests](#running-tests)
- [Reports](#reports)
- [Best Practices](#best-practices)

---

## Prerequisites

- **Python 3.7+**
- **Selenium** library
- **Pytest** library
- **Browser WebDriver** (e.g., ChromeDriver, GeckoDriver)

Ensure that your system has the correct WebDriver installed and available in the system path.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   - `pytest`: For running the tests
   - `selenium`: For web automation
   - `pytest-html` (optional): For generating HTML reports
   - `pytest-xdist` (optional): For parallel test execution

3. **Configure WebDriver path** if not added to system path. For example, download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the desired location, then set the path in the configuration.

## Directory Structure

```
├── tests/                     # Test cases
│   ├── test_example.py        # Sample test file
│   ├── conftest.py            # Pytest fixtures
│
├── pages/                     # Page Object Models (POM)
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Example page model
│
├── utils/                     # Helper utilities
│   ├── driver_manager.py      # WebDriver management
│
├── config/                    # Configuration files
│   ├── config.yaml            # Test configuration settings
│
├── reports/                   # Test reports (generated after execution)
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Configuration

Update the configuration file in the `config/` directory (`config.yaml`) with your test settings such as browser, environment URLs, credentials, etc.

### Example `config.yaml`:

```yaml
base_url: "https://your-site-url.com"
browser: "chrome"
timeout: 10
```

## Writing Tests

1. **Page Object Model (POM)**: Define page objects in the `pages/` directory. Each page class should contain locators and methods relevant to a specific page in the application.

   Example `login_page.py`:

   ```python
   from selenium.webdriver.common.by import By
   from .base_page import BasePage

   class LoginPage(BasePage):
       USERNAME_INPUT = (By.ID, "username")
       PASSWORD_INPUT = (By.ID, "password")
       LOGIN_BUTTON = (By.ID, "loginButton")

       def login(self, username, password):
           self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
           self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
           self.driver.find_element(*self.LOGIN_BUTTON).click()
   ```

2. **Writing Test Cases**: Write test cases in the `tests/` directory using Pytest.

   Example `test_login.py`:

   ```python
   import pytest
   from pages.login_page import LoginPage

   @pytest.mark.usefixtures("setup")
   def test_valid_login():
       login_page = LoginPage()
       login_page.login("username", "password")
       assert login_page.is_logged_in()
   ```

3. **Fixtures**: Use `conftest.py` to define fixtures for setup and teardown operations, such as browser setup.

   Example `conftest.py`:

   ```python
   import pytest
   from selenium import webdriver

   @pytest.fixture(scope="function")
   def setup():
       driver = webdriver.Chrome()
       driver.maximize_window()
       yield driver
       driver.quit()
   ```

## Running Tests

1. **Single Test**: Run a specific test file.

   ```bash
   pytest tests/test_example.py
   ```

2. **All Tests**: Run all tests in the `tests/` directory.

   ```bash
   pytest
   ```

3. **Generate HTML Report**: Use `pytest-html` for HTML reports.

   ```bash
   pytest --html=reports/report.html
   ```

4. **Parallel Execution**: Use `pytest-xdist` to run tests in parallel.

   ```bash
   pytest -n 4
   ```

## Reports

- Test reports are generated in the `reports/` folder.
- You can use `pytest-html` to generate HTML reports or configure CI/CD tools to produce test results.

## Best Practices

- Follow the Page Object Model (POM) to separate test logic from page elements.
- Keep test methods modular and independent.
- Use fixtures in `conftest.py` for setup and teardown tasks.
- Parameterize tests where necessary to improve test coverage.
- Run tests in parallel to speed up the test execution process.

---

This base framework aims to make test automation simple, maintainable, and efficient. Customize it as needed to suit your application's requirements. Happy testing!

---

### License

This project is licensed under the MIT License.
