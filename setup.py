from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()


setup(name='passwordgeneratorrohan',
version='1.0',
description='generates random passwords',
url='#',
author='rohan',
author_email='rohaniam777@gmail.com',
license='MIT',
packages=['passwordgeneratorrohan'],
install_requires = install_requires,
zip_safe=False)