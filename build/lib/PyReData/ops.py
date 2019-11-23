class Node:

    """Node are a fundamental datatype of PyReData. A single HTML tag could be considered an node.
        Node could be charecterized by its HTML attributes , ID and class. It could further have 
        child node , say to images , text and divs inside a div"""

    def __init__(
        self, obj, name="", id="", Class="", content="", attributes=[], centerize=False
    ):

        self.obj = obj
        self.child = []
        self.name = name
        self.id = id
        self.Class = Class
        self.attributes = attributes
        self.content = content
        self.centerize = centerize

    def add(self, item):

        self.child.append(item)

    def __str__(self):

        string = ""

        string += "NAME: " + self.name

        for child in self.attributes:

            string += "->"
            string += "\n"
            string += self.name

        return string


class Element:

    """Elements are used used to represent CSS tags"""

    def __init__(self, name, type, attributes=[], Class=False, Id=True, param=""):

        pass

    def __str__(self):

        pass
