from PyReData.exceptions import IdentifierError


class Stylesheet:
    """The class is used for managing stylesheets. The style's defined in the pages could be written
       into the stylesheets automatically/manually for resusing.
       
       Args:
           
           name[str]: Name of the stylesheet"""

    def __init__(self, name: str):

        self.name = name
        self.css = {}
        self.code = ""

    def write(
        self, attribute: list, name: str = None, Class: list = None, ID: list = None
    ):
        """The method is used for writing each ID/Class tag into the stylesheet
       
         Args:
          
            attributes[list]: The attributes taken by the class or id
            name[str]: Name given to particular tag. 
            Class[list]: Class of given tag
            ID[list]: ID of given tag
            
       """

        if ID:

            str = ""
            for id in ID:

                str += id
            
            if(attribute):
              
                self.css["#" + str] = attribute

        elif Class:

            str = ""
            for Class_n in Class:

                str += Class_n
            
            if(attribute):
          
                self.css["." + str] = attribute

        elif name:
            
            if(attribute):

                self.css[name] = attribute

        else:

            raise IdentifierError("No identifier was given")

    def generate(self):
        """The method generates the stylesheet based on the tags written into self.css dictionary
        
           Returns:
               
               code[str]: The generated CSS code"""

        # Support direct attribute mentions. When user mentions 'border:1px solid black' rather than [['border','1px solid black']]

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

    def compile(self):
        """The method generates the css stylesheet based on generated css code"""

        print("Writing stack")
        file = open(self.name + ".css", "w")
        file.write(self.code)
        file.close()
