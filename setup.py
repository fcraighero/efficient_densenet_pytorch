from setuptools import find_packages, setup

setup(
   name='eff-densenet',
   version="0.1.0",
   package_dir={'model':'models'},
   packages=find_packages(where="./models"),
)
