from setuptools import setup

setup(
    name='fastcli',
    version='0.1.0',
    py_modules=['fastcli'],
    install_requires=[
        'Click',
        'emoji',
    ],
    entry_points={
        'console_scripts': [
            'fastcli = fastcli.main:cli',
        ],
    },
)
