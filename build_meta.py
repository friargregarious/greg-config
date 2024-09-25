from src.gfg import loads, dumps
from pathlib import Path

HERE = Path(__file__).parent


# enter your project info here for Package meta-data.
NAME = 'greg-config'
DESCRIPTION = "Greg's Simple config loader and writer for TOML"
URL = "https://github.com/friargregarious/greg-config"
URLS = {
    "Bug Reports": "https://github.com/friargregarious/greg-config/issues",
    "Funding": "https://paypal.me/friargreg?country.x=CA&locale.x=en_US",
    "Say Thanks!": "https://mastodon.social/@gregarious",
    }

AUTHOR = "Gregory Denyes"
EMAIL = "greg.denyes@gmail.com"
VERSION = __version__
REQUIRES_PYTHON = '>=3.11.0'








LICENSE = (HERE / "LICENSE.txt").open(encoding="utf-8").read()
DESCRIPTION = (HERE / "README.md").open(encoding="utf-8").read()

REQUIRES = list((HERE / "requirements.txt").open(encoding="utf-8").readlines())

para = {
    "name": project,
    "author": author,
    "author_email": author_email
    
}

pyproj = {}
pyproj["build-system"] = {}
pyproj["build-system"]["requires"] = ["setuptools", "wheel"]
pyproj["build-system"]["build-backend"] = "setuptools.build_meta"

# with open("pyproject.toml", "w") as f:
#     dumps(pyproj, f)

if __name__ == "__main__":

    print(REQUIRES)