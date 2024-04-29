from setuptools import find_packages,setup
from typing  import List
import os

HYPEN_E_DOT ='-e .'

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))
def get_requirements(file_path:str)->List[str]:
    '''
    This function will retrun the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if  HYPEN_E_DOT in  requirements : # only if it is there remove it
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Market segmentaion',
    version =  '0.0.1',
    author='Sunayna',
    author_email='sunaynamore10@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt')
)