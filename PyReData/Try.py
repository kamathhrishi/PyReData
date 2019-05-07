from main import PyReData
import pandas as pd

lol=PyReData()

page=lol.page("BED")

data={'a':[1,2,3,4],'b':[1,2,3,4]}

pd=pd.DataFrame(data)

page.addtable(pd)

page.compile()