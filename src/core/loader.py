"""Loader module contains functions for loading and saving stl files.
"""
from csg.core import CSG
from os.path import splitext
import utils

def load_stl(file):
    return CSG.readSTL(file)


def save_stl(result, path):
    filename, extension = splitext(path)
    result.saveSTL('intersect.stl')
