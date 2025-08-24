# selenium-python-framework

Selenium Python Framework
This repository contains a robust and scalable test automation framework built with Python and Selenium. The framework is designed for end-to-end (E2E) testing of web applications, focusing on clean code, maintainability, and ease of use. It follows the Page Object Model (POM) design pattern to ensure test scripts are organized and reusable.

Key Features
Pytest Framework: Utilizes the powerful pytest testing framework for writing simple, readable, and efficient tests.

Page Object Model (POM): Implements the POM design pattern to separate test logic from page actions, making tests easier to maintain and understand.

End-to-End (E2E) Testing: The framework is structured to support comprehensive E2E test scenarios.

Configuration Management: Manages test data and configurations separately to avoid hardcoding values in test scripts.

HTML Reporting: Automatically generates detailed test reports for easy analysis and sharing.

Prerequisites
To get started, ensure you have the following installed on your system:

Python 3.x

pip (Python package installer)

Getting Started
Follow these steps to set up and run the framework on your local machine.

1. Clone the Repository
First, clone this repository to your local machine using Git.

git clone https://github.com/MaxMoya/selenium-python-framework.git

Navigate to the project directory:

cd selenium-python-framework

2. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

This will install packages such as pytest, selenium, and pytest-html.

3. Setup Web Drivers
This framework uses pytest-selenium. The repository's conftest.py file should handle the setup and teardown of the browser. If you run into issues with the driver, you can use the webdriver-manager library to automatically download the correct driver for your browser.

pip install webdriver-manager

Running Tests
Use the pytest command to execute your tests. Here are some common examples:

Run All Tests
To run all tests in the tests directory, simply run:

pytest

Run a Specific Test File
To run tests from a single file, provide the path to that file:

pytest tests/test_login.py

Run Tests with a Keyword
To run all tests that contain a specific name (e.g., tests related to "login"), use the -k flag:

pytest -k login

Generate a Detailed HTML Report
To generate a human-readable HTML report of your test run, use the --html and --self-contained-html flags:

pytest --html=report.html --self-contained-html

This will create a report.html file in the project's root directory.

Project Structure
The framework is organized into the following directories:

selenium-python-framework/
├── tests/                 # All test cases and test suites
│   ├── conftest.py        # Pytest fixtures and configurations
│   └── test_*.py          # Test files
├── pageObjects/           # Page Object Model classes
│   └── BasePage.py
│   └── LoginPage.py
├── utilities/             # Helper functions and utilities
│   └── config.py
├── requirements.txt       # Python dependencies
└── README.md              # Project README file

Page Object Model (POM)
The POM is a design pattern that creates an object repository for UI elements. Each web page in the application has a corresponding class in the pageObjects directory. This approach makes the tests more readable and resilient to UI changes. For example, if a button's locator changes, you only need to update the locator in the page object class instead of in every test case where that button is used.

Contributing
Contributions are welcome! If you have suggestions for improvements or want to add a new feature, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
