import ops


class Stack:

    """Class used to maintain the stack which stores operations and data.
      
       Args:
            
            init[List]: Initialize stack with giveb components/items
            name[str]:  name pf the webpage
    
    """

    def __init__(self, type, init=[], name=""):

        self.stack = []
        self.code = ""
        self.name = name
        self.type = type

    def writestack(self, component):

        line = self.write(component)
        self.code += line

        print(self.code)

    def write(self, component):

        line = ""
        line += "\n"

        line += "<" + component.obj

        if component.attributes:
            for attr in component.attributes:

                line += "attr"

        line += ">"
        line += "\n"

        line += component.content
        if component.child:

            for child in component.child:

                line += self.write(child)
                line += "\n"

                line += "\n"

        line += "\n"
        line += "</" + component.obj + ">"


        return line

    def write_stack(self):

        file = open(self.name + "." + self.type, "w")
        file.write(self.code)
        file.close()
