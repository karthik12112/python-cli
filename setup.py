from setuptools import setup, find_packages, os

here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'karthik/version.py')).read())

setup(
    name='karthik-test',
    version=__version__,
    description='Provides a wrapper for Okta authentication to awscli',
    packages=find_packages(),
    license='Apache License 2.0',
    author='James Hale',
    author_email='kreddy8512@gmail.com',
    url='https://github.com/karthik12112/test',
    entry_points={
        'console_scripts': [
            'karthik-cli=karthik.kp:main',
        ],
    },
    install_requires=[
        'requests',
        'boto3',
        ],
    extras_require={
        'U2F': ['python-u2flib-host']
    },
)
