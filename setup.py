from setuptools import setup

with open('README.md') as f:
    readme = f.read()

MAJOR = 0
MINOR = 0
PATCH = 24

VERSION = '{}.{}.{}'.format(MAJOR, MINOR, PATCH)
DESCRIPTION = 'String validation and sanitization'

# Setting up
setup(
    name="py.validator",
    version=VERSION,
    author="Sanel",
    author_email="sanelbgd@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=['pyvalidator'],
    install_requires=['typing', 'timestring'],
    keywords=['python', 'validation', 'string', 'sanitization', 'validator.js'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    project_urls={
        'GitHub': 'https://github.com/theteladras/py.validator'
    },
    license='MIT'
)
