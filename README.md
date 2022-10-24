Selenium automation testing using python for amazon website.

Selenium is an open source web application automation tool which can also test with different browser

You can install selenium by

pip3 install selenium

Once the installation is complete you can confirm it with bselenium --version 

Link for pytest setup - https://www.geeksforgeeks.org/how-to-install-selenium-on-macos/

Basic Structure of Framework

• base – This directory contains of functions which can be used across all the directory

• Configuration – contains config file to get the data


• Logs – Contains logs and allure logs

• Testcases-

In this folder we have all the test file with conftest.py which invoke the driver

• Commands to run the testcases

pytest --alluredir= folder_name_to_store_report

• Commands to generate allure report

allure serve report_path
