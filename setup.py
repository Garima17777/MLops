from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", " ") for req in requirements]


    return requirements

# def get_requirements(file_path: str) -> List[str]:
#     with open(file_path, "r") as file:
#         requirements = [line.strip() for line in file if line.strip() and not line.startswith("#")]
#     return requirements

setup(
    name="MLops project",
    version='0.0.1',
    author='Garima',
    author_email='garimachouhan17770@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)