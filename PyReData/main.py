from PyReData.ops import Item
from PyReData.stack import Stack
from PyReData.widgets import Widgets
from PyReData.page import Page


class PyReData:
    """
       The main class to be used to interact with the componenets of PyReData. 
       It gives access to pages , ops and widgets from PyReData. Pages represent an
       individual HTML page. Ops are a fundamental datatype PyReData works on.
       Item under Ops represent an single HTML tag with content and possible children 
       (other items) under it. Widgets are items put togheter to form usable code snippets
       users could use for developing their web report.
    """

    def __init__(self):

        self.page = Page
        self.ops = Item
        self.widgets = Widgets
