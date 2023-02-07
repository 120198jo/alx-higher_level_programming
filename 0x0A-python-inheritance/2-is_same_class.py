#!/usr/bin/python3
""" Function must return True if the object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Return True if the object is an instance of a class otherwise False
    """
    return type(obj) == a_class
