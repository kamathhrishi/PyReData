class Node:
    """Node are a fundamental datatype of PyReData. A single HTML tag could be considered an node.
        Node could be charecterized by its HTML attributes , ID and class. It could further have 
        child node , say to images , text and divs inside a div"""

    def __init__(
        self,
        obj,
        name="",
        id="",
        Class="",
        content="",
        attributes=[],
        centerize=False,
        stylesheet=None,
        style=None,
    ):

        self.obj = obj
        self.child = []
        self.name = name
        self.id = id
        self.Class = Class
        self.attributes = attributes
        self.content = content
        self.centerize = centerize
        self.stylesheet = stylesheet
        self.style = style

        if self.stylesheet:

            if self.id is not None:

                self.stylesheet.write(self.style, ID=id)

            elif self.Class is not None:

                self.stylesheet.write(self.style, Class=self.Class)

    def add(self, item):
        """Adds an item as child of current node.
           
        Args:
            
            item[datatypes?]: The item to be made as child"""

        self.child.append(item)

    def __str__(self):
        """String representation of node indicating the current node and the children"""

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
