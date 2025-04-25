from setuptools import setup, find_packages

setup(
    name='inbo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        *open('requirements.txt').read().splitlines(),
    ],
    author='Sai Raveendra Kandregula',
    author_email='sairaveendrakandregula@gmail.com',
    description='A Bot Framework for GitLab',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sai-Raveendra-Kandregula/InBo',  # Optional
)