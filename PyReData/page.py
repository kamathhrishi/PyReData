
from ops import Item
from stack import Stack
from widgets import Widgets 

class Page:
    
    """The main class to be used to interact the componenets of PyReData"
    
        Args:
            
            name[str]: Name of the page
            template:  Template of the given webpage
            
    """
    
    def __init__(self,name,template=""):
        
        self.name=name
        self.stack=Stack("html",name=self.name)
        self.template=[]
        self.widgets=Widgets()
        
        html=Item("html")
        head=Item("head")
        title=Item("title",content="Hello World")
        html.add(head)
        head.add(title)
        self.stack.writestack(html)
        
    def load_template(self):
        
        """Loads template for given webpage"""
        
        pass
    
    def body(self):
        
        """Initializes body of given webpage"""
        
        body_stack.append()
        
    def head(self):
        
        """Initializes head of given webpage"""
        
    def addtable(self,data):
        
        man=self.widgets
        self.stack.writestack(man.table(data))
    
    def render(self,element,name,id="",Class="",content="",attribute=""):
        
        """Renders element on the webpage
        
        Args:
            
            element[Container,Item]: The element to be rendered.
            name[str]: Name given to the element
            
        """
        
        item=Item(element,name,id=id,Class=Class,content=content,attribute=attribute)
        self.stack.write_stack(item)
    
    def compile(self):
        
        """Writes the stack as a HTML file"""
        
        self.stack.write_stack()