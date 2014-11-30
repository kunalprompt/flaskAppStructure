from setuptools import setup, find_packages

setup(
    name='blog',
    version='1.0',
    description = "Complete blog with social user authentication - flask & mongodb.",
    author = "Kunal Sharma",
    author_email = "",
    url = "",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)