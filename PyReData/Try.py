from main import PyReData

import pandas as pd
from ops import Item

lol = PyReData()

page = lol.page("LOL", style="background:rgb(236, 236, 221)")

data = {"a": [1, 2, 3, 4, 5], "b": [2, 4, 6, 8, 10], "c": [3, 6, 9, 12, 15]}

pd = pd.DataFrame(data)

widgets = lol.widgets()

container = widgets.container(
    attributes=[
        ["style", "border:1px solid black;margin-left:100px;margin-right:100px;"]
    ]
)
image = widgets.image("Doggy.png", id="LOL", Class="LOL")
container.add(
    Item("h1", content="Hello World", attributes=[["style", "text-align:center"]])
)
container.add(
    widgets.table(data,attributes=[["style","border:1px solid black;"]],data_attributes=[["style", "border:1px solid black;border-collapse: collapse;"]])
)
container.add(image)
page.render(container, "NAME")
page.compile()
