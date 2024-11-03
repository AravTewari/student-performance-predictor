from setuptools import setup, find_packages
from typing import List

def get_requirements(filename: str) -> List[str]:
    ''' Read requirements from file '''
    
    reqs = []
    with open(filename, 'r') as f:
        for line in f:
            if '-e .' not in line:
                reqs.append(line.strip())
    return reqs


setup(
    name='student-performance-indicator',
    version='0.0.1',
    author='Arav Tewari',
    author_email='tewari6@purdue.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)