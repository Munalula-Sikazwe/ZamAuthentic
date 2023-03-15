from setuptools import setup, find_packages

VERSION: str = '0.0.6'
DESCRIPTION: str = 'A validation library for Zambia'
NAME: str = "zam_authentic"
AUTHOR: str = "Munalula Sikazwe"
AUTHOR_EMAIL: str = 'munalulasikazwe67@gmail.com'
KEY_WORDS: list = ['validation', 'zambia', 'zambia_kyc', 'kyc']
CLASSIFIERS: list = ['Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9', 'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent', 'Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers', 'Topic :: Software Development :: Libraries :: Python Modules',
                     'Topic :: Utilities', 'Natural Language :: English']
INSTALL_REQUIRES: list = ['phonenumbers']
LONG_DESCRIPTION: str = 'Readme.txt'
with open('README.md', 'r') as file:
    LONG_DESCRIPTION = file.read()

### settting up

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    keywords=KEY_WORDS,
    classifiers=CLASSIFIERS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
)
