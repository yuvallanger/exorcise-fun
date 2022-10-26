from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="exorcise_fun",
    version="0.0.0",
    description="Exorcise emojis from command line tools.",
    long_description=readme,
    author="Yuval Langer",
    author_email="yuvallangerontheroad@gmail.com",
    url="https://codeberg.org/yuvallangerontheroad/exorcise-fun",
    license=license,
    entry_points={
        "console_scripts": [
            "exorcise-fun=exorcise_fun.exorcise_fun:main",
            "black=exorcise_fun.stand_in:main",
        ],
    },
    packages=["exorcise_fun"],
)
