from setuptools import setup, find_packages

setup(
    name='githack',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ItsaBella/githack.git',
    author='Itumeleng Mothapo',
    author_email='itumelengbotshelo7@gmail.com'
)
