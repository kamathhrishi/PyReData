
from ops import Item

class Widgets:
    
    def __init__(self):
        
        pass
    
    def table(self,table,name=""):
        
        Table=Item("table")
        
        columns=[]
        
        data=[]
        
        for headers in table:
            
            columns.append(headers)
        
        for column in columns:
            
            for row in table[column]:
                
                data.append()
                
            
        """for i in table:
            
            row=Item("tr")
            
            for j in table[i]:
                
                row.add(Item("td",content=str(j)))
                
            Table.add(row)"""
            
        return Table
                
                
                