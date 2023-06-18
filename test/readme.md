API Test Framework

This is a test framework for API testing using Python and PyTest. It is designed to run tests against a specific API endpoint and generate an HTML report of the test results.
Prerequisites

    Docker should be installed on your machine.

Getting Started

    Clone the repository to your local machine. https://github.com/Nandi-007/trading_api_testing.git

    Build the Docker image by running the following command in the project directory:

docker build -t api-test-suite .

Run the Docker image in a container using the following command:

bash

    docker run --network bridge -it -v ${PWD}/reports:/app/reports api-test-suite

    The test suite will be executed, and the test results will be displayed in the console.

    Once the test execution is completed, an HTML report named report.html will be generated. You can find this report in the reports folder within the test directory.

Test Reports

The test framework generates an HTML report that provides a comprehensive overview of the test results. You can open the report.html file in any web browser to view the report. The report includes information such as:

    Test execution summary
    Individual test case results (pass/fail)
    Detailed test case descriptions
    Error messages and stack traces (if any)

Customizing Tests

You can customize the test cases by modifying the test files located in the API_test directory. Add or update test functions as per your requirements. The framework uses PyTest, so you can leverage its features for writing and organizing your tests.
Feedback

If you have any feedback, suggestions, or issues with the test framework, please feel free to open an issue on the GitHub repository. We appreciate your contribution and feedback to make this framework even better.

Happy testing!