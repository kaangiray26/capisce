from setuptools import setup, find_namespace_packages

setup(
    name='capisce',
    version='0.1.1',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True
)
