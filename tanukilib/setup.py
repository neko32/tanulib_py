from setuptools import setup, find_packages

setup(
    name='tanukilib',
    version='0.1.0',
    packages=find_packages(),
    author='neko64',
    install_requires = [
        'pandas',
        'numpy',
        'opencv-python'
    ]
)

