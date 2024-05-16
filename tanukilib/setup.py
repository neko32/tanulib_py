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
        'keras_facenet',
        'tensorflow==2.13',
        'tensorflow_hub',
        'boto3',
        'pillow',
        'python-dotenv',
        'pydot',
        'flask',
        'matplotlib',
        'protobuf3',
        'grpcio-tools',
        'dnspython',
        'beautifulsoup4',
        'mecab-python',
        'unidic-lite',
        'chardet',
        'pyyaml',
        'pexels-api',
        'tqdm',
        'cvat-sdk',
        'scikit-image',
        'fiftyone',
        'scikit-learn',
    ]
)

