import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Flaskr"
    version="0.0.1",
    author="Joseph Zimmerman",
    author_email="joeyzimmerman17@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
