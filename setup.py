import setuptools
from bettercaptcha import __version__, __homepage__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bettercaptcha",
    version=__version__,
    author=__author__,
    author_email="magicafreak@noircoding.de",
    description="Captcha illustrator with Pillow and Numpy for Python 3.6 or higher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__homepage__,
    packages=['bettercaptcha'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["Pillow"],
    extras_require={"distortion": ["numpy"]},
    python_requires='>=3.6',
)
