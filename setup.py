from setuptools import find_packages, setup

setup(
   name='eff_densenet',
   version="0.1.0",
   package_dir={'':'models'},
   packages=find_packages(where="./models"),
)
