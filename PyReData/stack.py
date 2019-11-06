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
        self.write_stack()

    def write_css(self, component, attributes, id=False, Class=False):

        line = ""

        if id:

            line += "#"

        if Class:

            line += "."

        line += component
        line += "{"

        for attr in attributes:

            line += attr[0]
            line += ":"
            line += attr[1]
            line += " "

        line += "}"

        return line

    def write(self, component):

        line = ""
        line += "\n"

        line += "<" + component.obj
        line += " "

        if component.attributes:

            for attr in component.attributes:

                print(attr)

                line += attr[0]
                line += "="
                line += "'"
                line += attr[1]
                line += "'"

        if component.id:

            line += " "
            line += "id="
            line += "'"
            line += component.id
            line += "'"

        if component.Class:

            line += " "
            line += "class="
            line += "'"
            line += component.Class
            line += "'"

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

        print("Writing stack")
        file = open(self.name + "." + self.type, "w")
        file.write(self.code)
        file.close()
