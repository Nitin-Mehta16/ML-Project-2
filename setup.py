from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
        '''
        this function will return the list of the requirments
        '''
        requirements = []
        with open(file_path) as file_obj:
            requirements= file_obj.readlines()
            requirements= [req.replace("/n","") for req in requirements]

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