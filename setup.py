from setuptools import find_packages, setup
from typing import List # type: ignore

variable = '-e .'
def get_requirements(file_path: str)->List[str]:
    requirements=[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if variable in requirements:
            requirements.remove(variable)
    return requirements


setup(
name='ml_project',
version = '0.0.0',
author = 'Lokesh Sreenath Jakka',
author_email= 'lokeshsreenathjakka@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')

)