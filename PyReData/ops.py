class Item:

    """Items are a fundamental datatype of PyReData. A single HTML tag could be considered an item.
        Item could be charecterized by its HTML attributes , ID and class. It could further have 
        child items , say to images , text and divs inside a div"""

    def __init__(self, obj, name="", id="", Class="", content="", attributes=[]):

        self.obj = obj
        self.child = []
        self.name = name
        self.id = id
        self.Class = Class
        self.attributes = attributes
        self.content = content

    def add(self, item):

        self.child.append(item)
