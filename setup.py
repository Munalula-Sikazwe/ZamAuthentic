from setuptools import setup, find_packages

VERSION: str = '0.0.1'
DESCRIPTION: str = 'A validation library for Zambia'
NAME: str = "zam_authetic"
AUTHOR: str = "Munalula Sikazwe"
AUTHOR_EMAIL: str = 'munalulasikazwe67@gmail.com'
KEY_WORDS: list = ['validation', 'zambia', 'zambia_kyc', 'kyc']
### settting up

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=KEY_WORDS,
    classifiers=['Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9', 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent', 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers', 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Utilities', 'Natural Language :: English']

)
