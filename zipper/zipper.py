import zipfile
import re
from .exceptions import NotValidContent

pattern = re.compile(r'(\\|\.)+.+')


def open(path_zip):
    return zipfile.ZipFile(path_zip, "r")


def get_all_files_name(file):
    return file.namelist()


def extract_all_files(file, path="/tmp/zipper"):
    _validate(file)
    files_name = get_all_files_name(file)
    file.extractall(path)
    return ["{}/{}".format(path, name) for name in files_name]


def close(file):
    try:
        file.close()
    except Exception as e:
        raise e


def _validate(file):
    indeces = [name for name in get_all_files_name(file) if pattern.match(name)]
    if len(indeces) > 0:
        raise NotValidContent()
