from csg.core import CSG
from csg.geom import Vertex, Vector


def intersect(obj1,obj2):
    return obj1.intersect(obj2)

def union(obj1,obj2):
    return obj1.union(obj2)

def subtract(obj1,obj2):
    return obj1.subtract(obj2)
