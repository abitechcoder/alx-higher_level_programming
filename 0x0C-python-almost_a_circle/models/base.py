#!/usr/bin/python3
class Base:
    """
    A class representing Base class

    Attributes
    ----------
    __nb_objects : int
        The private instance attribute
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Parameters
        ----------
        id : int
            The argument value passed to init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
