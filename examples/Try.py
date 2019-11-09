import PyReData
import pandas as pd
from PyReData.main import PyReData
from PyReData.ops import Item
import matplotlib.pyplot as plt

import pandas as pd

lol = PyReData()

page = lol.page("LOL", style="background:rgb(236, 236, 221)")


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

container.add(image)
page.render(container, "NAME")
page.compile()
