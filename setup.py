from setuptools import setup

setup(
    name='pypoller',
    version='1.0.0',
    python_requires='>=3.5',
    install_requires=['pymodbus'],
    scripts=['pypoller.py'],
)