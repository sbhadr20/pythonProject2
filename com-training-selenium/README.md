#To install the pipenv

pip install pipenv

<!--pipenv --python 3.7-->

#To install the dependencies from Pipfile.lock

pipenv install (when you open this project in PyCharm IDE, pycharm automatically detects pipfile and propmt to install the dependencies)

#To remove the existing virtual environment (run this cmd only if "pipenv install" fails due to existing environment)

pip uninstall virtualenv

#To run all tests in a module 

pytest test_mod.py or pipenv run pytest test_mod.py

#To run all tests in a directory 

pytest test/ or pipenv run pytest test/

#To run tests by marker expressions (tag) 

pytest -m shopping or pipenv run pytest -m shopping

#To run tests and generate pytest html report 

pytest  --html=.\Reports\report.html .\src\onlineshopping\test\login.py

pipenv run pytest --html=report.html