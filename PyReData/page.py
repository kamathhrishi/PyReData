from PyReData.ops import Node
from PyReData.stack import Stack
from PyReData.widgets import Widgets


class Page:

    """The main class to be used to interact the componenets of PyReData"
    
       Args:
            
            name[str]: Name of the page
            template:  Template of the given webpage
            
    """

    def __init__(self, name, template="", style="", stylesheets=[], scripts=[]):

        self.name = name
        self.stack = Stack("html", name=self.name)
        self.template = []
        self.stylesheets = stylesheets
        self.scripts = scripts

        attributes = []
        if style:

            attributes = [["style", style]]

        self.widgets = Widgets()
        self.html = Node("html")
        self.head = Node("head")
        self.body = Node("body", attributes=attributes)
        title = Node("title", content="Hello Wo")
        self.html.add(self.head)
        self.html.add(self.body)
        self.head.add(title)
        self.init_head()

    def print_stack(self):

        for node in self.stack:

            print(node)

    def load_template(self):

        """Loads template for given webpage"""

        pass

    def init_head(self):
        """Initializes head of given webpage"""

        for style in self.stylesheets:

            self.head.add(
                Node("link", attributes=[["rel", "stylesheet"], ["href", style]])
            )

        for link in self.scripts:

            self.head.add(Node("script", attributes=[["src", link]]))

    def addtable(self, data):

        man = self.widgets
        self.stack.writestack(man.table(data))

    def render(self, element, name, id="", Class="", content="", attributes=""):

        """Renders element on the webpage
        
        Args:
            
            element[Container,Item]: The element to be rendered.
            name[str]: Name given to the element
            
        """
        print("Writing")
        self.body.add(element)

    def compile(self):

        """Writes the stack as a HTML file"""

        self.stack.writestack(self.html)
