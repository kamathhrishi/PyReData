import PyReData.ops


class Stack:
    """Class used to maintain the stack which stores operations and data.
      
       Args:
            
            init[List]: Initialize stack with giveb components/items
            name[str]:  name pf the webpage
    
    """

    def __init__(self, type, init=[], name="", stylesheet=None, style=None):

        self.stack = []
        self.code = ""
        self.name = name
        self.type = type
        self.stylesheet = stylesheet
        self.style = style

    def writestack(self, component):

        line = self.write(component)
        self.code += line
        self.write_stack()

    def write(self, component):

        line = ""
        line += "\n"

        if component.centerize:

            line += "<center>"

        line += "<" + component.obj
        line += " "

        if component.id:

            line += " "
            line += "id="
            line += '"'

            for id_no in range(0, len(component.id)):

                line += component.id[id_no]

                if id_no != (len(component.id) - 1):

                    line += " "

            line += '"'

        line += " "

        if component.Class:

            line += " "
            line += "class="
            line += '"'

            for id_no in range(0, len(component.Class)):

                line += component.Class[id_no]

                if id_no != (len(component.Class) - 1):

                    line += " "

            line += '"'

        line += " "

        if component.attributes and isinstance(component.attributes[0], list):

            for attr in component.attributes:

                line += attr[0]
                line += "="
                line += '"'
                line += attr[1]
                line += '"'
                line += " "

        elif component.attributes and isinstance(component.attributes[0], str):

            line += component.attributes[0]
            line += "="
            line += '"'
            line += component.attributes[1]
            line += '"'
            line += " "

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

        if component.centerize:

            line += "</center>"

        return line

    def write_stack(self):

        print("Writing stack")
        file = open(self.name + "." + self.type, "w")
        file.write(self.code)
        file.close()
