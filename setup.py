from setuptools import find_packages, setup

setup(
   name='eff_densenet',
   version="0.1.0",
   package_dir={'':'model'},
   packages=find_packages(where="./model"),
)
