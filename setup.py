from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()    ## read lines
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileExistsError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network-security",
    version="0.0.1",
    author="Sankalp S",
    author_email="sankalps410@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)