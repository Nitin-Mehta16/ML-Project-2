#setup.py is the configuration file for packaging a Python project.

# Why is it needed?
# 1> Without setup.py, you cannot install your project as a package.
# 2> If you're creating a machine learning or software project that others will install, setup.py is necessary.

# What Does setup.py Do?
# 1> Defines package name, version, and author.
# 2> Includes dependencies (install_requires).
# 3> Finds all sub-packages (find_packages()).  packages >> sub-packages >> collection of modules >> module >> sinlge python file >> functions, classes, variables.
# 4> Makes the project pip-installable.

#❌ Without setup.py, You Must:
# 1. Copy files manually to use them in another project.
# 2. Set PYTHONPATH manually to access packages.
# 3. Install dependencies manually using pip install -r requirements.txt.
# 4. Remember all dependencies when sharing the project.

# 📌 What Do You Mean by "Manually Importing the Module"?
# 1. By default, Python only looks for modules in certain directories (like the current folder, installed packages, and system paths).
# 2. If your custom module (Python script or package) is outside these directories, Python won’t find it, and you will get an ImportError or ModuleNotFoundError.

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:  #(file_path:str)-> input type, List[str]--> output type #Type hints do not affect execution; they are just for readability and help tools like PyCharm, VSCode, or MyPy catch potential errors.
        '''
        this function will return the list of the requirments
        '''
        requirements = []
        with open(file_path) as file_obj:
            requirements= file_obj.readlines()
            requirements= [req.replace("\n","") for req in requirements]

            if "-e ." in requirements:
                  requirements.remove("-e .")
            return requirements




setup(
name  = "mlproject",
version = "0.0.1",
author = " nitin",
author_email = "nitin@gmail.com",
packages = find_packages(),  ## it will consider all folder as package which have __init__.py file and build them in process
# install_requires = ["numpy","pandas","seaborn", "matplotlib.pyplot"]
install_requires = get_requirements('requirement.txt')

)