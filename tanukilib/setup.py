from setuptools import setup, find_packages

setup(
    name='tanukilib',
    version='0.1.0',
    packages=find_packages(),
    author='neko64',
    install_requires = [
        'pandas',
        'numpy',
        'opencv-python',
        'python-magic',
        'keras',
        'tensorflow==2.13',
        'tensorflow_hub',
        'boto3',
        'pillow',
        'python-dotenv',
        'pydot',
        'flask'
    ]
)

