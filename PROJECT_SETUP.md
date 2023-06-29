## Setting up a new PyCharm project: Local venv

Steps taken to create initial PyCharm project:
* Create a virtual environment (based on Python 3.10)
* Install pyspark `pip install pyspark`
* Install jupyter `pip install jupyter`
* ~~Create requirements.txt: `Tools > Sync Python Requirements...`~~
* Create requirements.txt
  ```shell
  pip freeze > requirements.txt
  ```

### Install project on a new machine:

#### Create Virtual Environment:  

##### Virtual Environment: Local 

* From the menu select `File > Settings` 
* Go to `Project: learning-spark > Python Interpreter`
* To the right of the Python Interpreter drop down, click on `Add Interpreter...` and `Add Local Interpreter...`
* Python Interpreter > New environment using `Virtualenv`
* Python Interpreter > Location: `C:\Users\<username>\projects\py-project\venv`
* Base interpreter:
  * Click on `...` and navigate to the python.exe you want to use
  * e.g. 3.10: `C:\Users\<username>\Python\Python310\python.exe`
* Create new 3.10 Virtual Environment (venv)
* Activate venv (if not already)
  ```shell
  ./bin/Scripts/activate.ps1
  ```
* Install requirements
  ```shell
  pip install -r requirements.txt
  ```

[//]: # (##### Virtual Environment: SSH)

[//]: # ()
[//]: # (TODO:)

[//]: # ()
[//]: # (##### Virtual Environment: Docker)

[//]: # ()
[//]: # (TODO:)