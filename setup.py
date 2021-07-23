from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='passwd_encrypt',
    version='0.2.1',
    author='Javier Ramos',
    author_email='jrdcasa@gmail.com',
    description="A simple tool to generate RSA keys and use them to encrypt/decrypt messages.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url='https://github.com/jrdcasa',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering'
    ],
    # Dependencies
    install_requires=[
        'pycryptodome'
    ],
    # Contents
    packages=find_packages(exclude=['example', 'recipes']),
)
