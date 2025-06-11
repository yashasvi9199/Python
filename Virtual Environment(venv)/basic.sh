#* Virtual environment in Python is used to create multiple instances of Python interpreter. It is a way to separate the dependencies of different projects.

#* It is a way to create a separate environment for each project.

#* We can install different packages and versions of packages in different virtual environments.

#? To create a virtual environment
python3 -m venv myenv

#? To Activate the virtual environment (Mac/Linux)
source myenv/bin/activate

#? To Activate the virtual environment (windows)
myenv\Scripts\activate.bat #Terminal
myenv\Scripts\activate.ps1 #PowerShell

#? To deactivate the virtual environment
deactivate

#? To remove the virtual environment
rm -rf myenv

#* To get all the installed packages in environement
pip freeze

#* To get this list as a text file
pip freeze >requirements.txt #This can be later used to directly install all packages in another env

#* To install packages from text file
pip install -r requirements.txt

#* To get all installed packages in global environment
pip list

#* To install package in environment
pip install package_name
