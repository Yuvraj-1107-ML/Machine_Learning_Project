from setuptools import find_packages,setup
from typing import List
hypen_dot='-e .'
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n"," ") for req in requirements ]
    if hypen_dot in requirements:
        requirements.remove(hypen_dot)
    return requirements
         
setup( 
  name="ML project",
  version="0.0.1",
  author="Yuvraj Dawande",
 author_email="yuvrajdawande373@gmail.com",
 packages=find_packages(),
 install_requires=get_requirement('requirements.txt'))

