from main import PyReData
import pandas as pd

lol = PyReData()

page = lol.page("LOL")

data = {"a": [1, 2, 3, 4, 5], "b": [2, 4, 6, 8, 10], "c": [3, 6, 9, 12, 15]}

pd = pd.DataFrame(data)

widgets = lol.widgets()

page.render(widgets.table(data), "random")

page.compile()
