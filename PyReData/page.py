from PyReData.ops import Item
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
        self.html = Item("html")
        self.head = Item("head")
        self.body = Item("body", attributes=attributes)
        title = Item("title", content="Hello Wo")
        self.html.add(self.head)
        self.html.add(self.body)
        self.head.add(title)
        self.init_head()

    def load_template(self):

        """Loads template for given webpage"""

        pass

    def body(self):

        """Initializes body of given webpage"""

        body_stack.append()

    def init_head(self):
        """Initializes head of given webpage"""

        for style in self.stylesheets:

            self.head.add(
                Item("link", attributes=[["rel", "stylesheet"], ["href", style]])
            )

        for link in self.scripts:

            self.head.add(Item("script", attributes=[["src", link]]))

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
