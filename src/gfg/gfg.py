""" This is a simple config loader and writer for the glogger app. """
from pathlib import Path
import tomllib, tomli_w 


def loads(target) -> dict:
    where = Path(target)
    with where.open("r", encoding="utf-8") as fs:
        return tomllib.loads(fs.read())

def dumps(data, target) -> None:
    where = Path(target)
    with where.open("w", encoding="utf-8") as fs:
        tomli_w.dumps(data, fs)


