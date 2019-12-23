
from typing import List

def validate_names(id:[List,str],Class:[List,str]):
    
    if(type(id)==str):
        
        id=[id]
    
    if(type(Class)==str):
        
        Class=[Class]
        
    return id,Class