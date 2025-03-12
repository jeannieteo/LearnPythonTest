Barebones test automation framework that includes Python, Pytest, Selenium, Allure, and automatic screenshot capturing for both test success and failure scenarios. 
-Generate Allure Reports-
pytest
allure serve allure-results


Install Allure using Scoop:
scoop install allure
Alternatively, download the Allure ZIP file from the Allure GitHub releases page. Extract it and add the bin folder to your system's PATH.

Mac:
Install Allure using Homebrew:

bash
brew install allure
Linux:
Download the Allure package from the Allure GitHub releases page https://github.com/allure-framework/allure2/releases.
Extract the package and add the bin folder to your PATH.
On Windows, add the path to the Allure installation directory 
(e.g., C:\Users\<YourUser>\scoop\apps\allure\current\bin) to the PATH variable.
On Mac/Linux, add the Allure binary path to your .bashrc or .zshrc file:
export PATH=$PATH:/path/to/allure/bin
