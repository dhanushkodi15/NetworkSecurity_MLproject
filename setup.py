
from setuptools import find_packages,setup
from typing import List

#Function return the list of requirements
def get_requirements()->List[str]:
    requirement_lst=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            #Iterate through the each line
            for line in lines:
                requirement=line.strip()

                #Check for empty line and not include '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirement.txt is not found")

    return requirement_lst

setup(
    name="NetworkSecurity_MLproject",
    version="0.0.1",
    author="Dhanushkodi",
    author_email="gdevkodi15@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)