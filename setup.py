from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().split()

setup(
    name='soogic',
    version='1.0',
    packages=find_packages(),
    include_package_datga=True,
    url='http://www.soogic.com/',
    author='Bain',
    # entry_points={'console_scripts': ['soogic = soogic.manage:cli.main']},
    install_requires=requirements
)
