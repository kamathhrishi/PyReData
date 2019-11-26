from PyReData.exceptions import IdentifierError


class Stylesheet:
    def __init__(self):

        self.css = {}
        self.code = ""

    def write(self, attribute, name=None, Class=None, ID=None):

        if ID:

            self.css["#" + ID] = attribute

        elif Class:

            self.css["." + Class] = attribute

        elif name:

            self.css[name] = attribute

        else:

            raise IdentifierError("No identifier was given")

    def generate(self):

        for element in self.css.keys():

            line = ""
            line += element
            line += "{"
            for attribute in self.css[element]:

                line += attribute[0]
                line += ":"
                line += attribute[1]
                line += ";"

            line += "}"

            self.code += line
            self.code += "\n"

        return self.code
