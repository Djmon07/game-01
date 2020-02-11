import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="game-01"
    version="0.0.1",
    author="Daniel",
    author_email="djmonwork@gmail.com",
    url="https://github.com/Djmon07/game-1",
    description="Start to a new adventure game just waiting to be descovered",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
