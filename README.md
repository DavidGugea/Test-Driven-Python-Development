# Test-Driven Python Development

## 1. Getting Started with Test-Driven Development
## 2. Red-Green-Refactor - The TDD Cycle
## 3. Code Smells and Refactoring
## 4. Using Mock Objects to Test Interactions
## 5. Working with Legacy Code
## 6. Maintaining Your Test Suite
## 7. Executable Documentation with doctest
## 8. Extending unittest with nose2
## 9. Unit Testing Patterns
## 10. Tools to Improve Test-Driven Development

---
---

# 1. Getting Started with Test-Driven Development

## Understanding test-driven development

The flowchart below shows the three steps in the process of TDD.

![Figure](ScreenshotsForNotes/Chapter1/Figure1.PNG)

Let's walk through the preceding flowchart in a little more detail.

* Red: The first step is to write a small unit test case. As we have only written the test and haven't written the implementation yet, this test will naturally fail.
* Green: Next, we write the code that implements the desired functionality. At this point, we aren't looking to create the best design or the most readable code. We just want something simple that will pass the test.
* Refactor: Now that the test is passing, we go back and look at the code to see whether it can be improved. This may involve improving the design, or making it more readable or maintainable. We can use the tests written so far to ensure that we aren't breaking anything during the refactoring step.
* The cycle repeats as we proceed to the next test and implement the next bit of functionality.

Developers who are familiar with TDD usually go through this cycle many times an hour, implementing small steps of functionality each time.

## TDD versus unit testing versus integration testing

Before we go further, let's take a short detour to define some terms and understand the differences between them. It is very easy to get confused between these terms, and they are often used with different meanings in different places.

In the broadest sense of the term, unit testing simply means testing a single unit of code, isolated from other code that it might be integrated with. Traditionally, unit testing was an activity that was primarily performed by test engineers. These engineers would take code given by the developers and run them through a suite of tests to verify that the code worked. Since this code was tested before integration, the process fits into the definition of a unit test. Traditional unit testing was typically a manual affair, with test engineers walking through the tests cases by hand, although some teams would go a step further and automate the tests.

An integration test is a test that involves exercising more than one unit of the system. The goal is to check whether these units have been integrated correctly. A typical integration test might be to go to a web page, fill in a form, and check whether the right message is displayed on the screen. In order for this test to pass, the UI must show the form correctly, the input must be captured correctly, and that input must be passed on to any logic processing. The steps might involve reading and writing from a database before a message is generated and the UI has to display it correctly. Only if all these interactions succeed will the integration test pass. If any one step should fail, the integration test will fail.

At this point, a valid question would be to ask why we need unit testing at all. Why not write only integration tests, where a single test could check so many parts of the application at once? The reason is that integration tests do not pinpoint the location of failure. A failing integration test could have an error in the UI, or in the logic, or somewhere in the way data is read or written. It will take a lot of investigation to see where the error is and fix it. By contrast, with well-written unit tests, a failing unit test will pinpoint exactly what is failing. Developers can go right to the point and fix the error.

Along the way, teams started moving to a process where developers themselves wrote tests for the code that they had implemented. These tests would be written after the developer had finished the implementation, and helped verify that the code worked as expected. These tests were usually automated. Such a process is generally called developer testing or developer unit testing.

TDD takes developer tests one step further, by writing the test before starting the implementation.

* **Developer tests:** Any kind of automated unit tests written by the developer, either before or after functionality is implemented.
* **Unit testing:** Any kind of testing of a particular unit of an application, either by a developer or a tester. These tests might be automated, or run manually.
* **Integration testing:** Any kind of testing that involves two or more units working together. These tests are typically performed by a tester, but they could be done by a developer as well. These tests might be manual or automated.

As we can see, unit testing is a general term, whereas developer testing is a specific subset of unit testing, and TDD is a specific form of developer testing.

On the surface, traditional unit testing, developer testing and TDD look similar. They all appear to be about writing tests for a single unit of code, with only minor variations based on who writes the test and whether the tests are written before the code or after.

However, dig deeper and differences appear. First, the intent is vastly different. Traditional unit testing and developer testing are all about writing tests to verify that the code works as it is supposed to. On the other hand, the main focus of TDD is not really about testing. The simple act of writing a test before the implementation changes the way we think when we implement the corresponding functionality. The resulting code is more testable, usually has a simple and elegant design, and is more maintainable and readable. This is because making a class easy to test also encourages good design practices, such as decoupling dependencies and writing small, modular classes.

Thus, one can say that TDD is all about writing better code, and it is just a happy side effect that we end up with a fully automated test suite as an outcome.

This difference in intent manifests itself in the type of tests. Developer testing usually results in large test cases, with a hefty part of the test code involved in test setup. By contrast, tests written using TDD are very small and numerous. Some people like to call them micro tests to differentiate them from other developer tests or traditional unit tests. TDD-style unit tests also try to be very fast to run because they are executed every few minutes during the development process.

Finally, the tests that are written in TDD are those that drive the development forward, and not necessarily those that cover all imaginable scenarios. For example, a function that is supposed to process a file might have tests to handle cases when the file exists or it doesn't exist, but probably won't have tests to see what happens if the file is 1 terabyte in size. The latter is something that a tester might conceivably test for, but would be an unusual test in TDD unless the function is clearly expected to work with such a file.

This really highlights the difference between TDD and other forms of unit testing.

> TDD is about writing better, cleaner, more maintainable code, and only incidentally about testing.

## Unit Test Example

```Python3
import unittest

class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)


if __name__ == '__main__':
    unittest.main()
```

What does this code do?

1. First, we import unittest. This is the library that has the test framework that we are going to use. Luckily for us, it is bundled into the Python standard library by default and is always available, so we don't need to install anything, we can just import the module directly.

2. Second, we create a class StockTest. This class will hold all the test cases for the Stock class. This is just a convenient way of grouping related tests together. There is no rule that every class should have a corresponding test class. Sometimes, if we have a lot of tests for a class, then we may want to create separate test classes for each individual behavior, or group the tests some other way. However, in most cases, creating one test class for an actual class is the best way to go about it.

3. Our StockTest class inherits from the TestCase class in the unittest module. All tests need to inherit from this class in order to be identified as a test class.

4. Inside the class, we have one method. This method is a test case. The unittest framework will pick up any method that starts with test. The method has a name that describes what the test is checking for. This is just so that when we come back after a few months, we still remember what the test does.

5. The test creates a Stock object and then checks if the price is None. assertIsNone is a method provided by the TestCase class that we are inheriting from. It checks that its parameter is None. If the parameter is not None, it raises an AssertionError and fails the test. Otherwise, execution continues to the next line. Since that is the last line of the method, the test completes and is marked as a pass.

6. The last segment checks if the module was executed directly from the command line. In such a case, the __name__ variable will have the value __main__, and the code will execute the unittest.main() function. This function will scan the current file for all tests and execute them. The reason we need to wrap this function call inside the conditional is because this part does not get executed if the module is imported into another file.

## Test errors versus test failures

There are two reasons why a test might not pass: It might have failed or it might have caused an error. There is a small difference between these two. A failure indicates that we expected some outcome (usually via an assert), but got something else. For example, in our test, we are asserting that stock.price is None. Suppose stock.price has some other value apart from None, then the test will fail.

An error indicates that something unexpected happened, usually an unexpected exception was raised. In our previous example, we got an error because the Stock class has not yet been defined.

In both the cases, the test does not pass, but for different reasons, and these are reported separately as test failures and test errors.

## Reorganizing the test code

We've added the test cases in the same file as the code. This is a good, simple way to add test cases to standalone scripts and applications that are not too complex. However, for larger applications, it is a good idea to keep test code separate from production code.

There are two common patterns for organizing test code this way.

The first pattern is to keep test code in a separate root directory, as shown in the following:

![Figure](ScreenshotsForNotes/Chapter1/Figure2.PNG)

The other pattern is to keep test code as a submodule of the main code, as shown in the following:

![Figure](ScreenshotsForNotes/Chapter1/Figure3.PNG)

The first pattern is commonly used for standalone modules as it allows us to distribute the code and tests together. Tests can generally be run without having to perform a lot of setup or configuration. The second pattern has an advantage when the application has to be packaged without the test code, for example when deploying to production servers, or distributing to customers (in the case of a commercial application). However, both the patterns are in popular use, and it is mainly a personal preference as to which method to use.

## Running the tests

The command that you use in order to write the tests is:

``` python.exe -m unittest ```

This command will go through the current directory and all subdirectories and run all the tests that are found. This is the default autodiscover mode of execution, where the command searches all the files and runs the tests. Autodiscovery can also be explicitly run with the following command:

```python3 -m unittest discover```

Autodiscover can be customized to check in specific directories or files with the following parameters:

* -s start_directory: Specify the start directory from where the discovery should start. This defaults to the current directory.

* -t top_directory: Specify the top-level directory. This is the directory from which imports are performed. This is important if the start directory is inside the package and you get errors due to incorrect imports. This defaults to the start directory.

* -p file_pattern: The file pattern that identifies test files. By default it checks for python files that start with test. If we name our test files something else (for example, stock_test.py), then we have to pass in this parameter so that the file is correctly identified as a test file.

To illustrate the difference between the start and top directory, run the following command from the src directory:

```python3 -m unittest discover -s stock_alerter```

The preceding command will fail with an import error. The reason is because when the start directory is set to stock_alerter, then the tests directory is imported as a top-level module, and the relative import fails. To get around this, we need to use the following command:

```python3 -m unittest discover -s stock_alerter -t```

This command will import all modules relative to the top directory, and so stock_ alerter correctly becomes the main module.

You can also disable autodiscovery and specify only certain tests to be run:

* Passing in a module name will only run the tests within that module. For example, python3 -m unittest stock_alerter.tests.test_stock will run the tests only in test_stock.py.

* You can further refine to a specific class or method, such as python3 -m unittest stock_alerter.tests.test_stock.StockTest.



