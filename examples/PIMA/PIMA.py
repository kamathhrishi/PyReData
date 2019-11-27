import PyReData
import pandas as pd
from PyReData.main import PyReData
from PyReData.ops import Node
from PyReData.stylesheets import Stylesheet
import matplotlib.pyplot as plt
import seaborn as sns

lol = PyReData()

File = "pima-indians-diabetes.csv"

Data = pd.read_csv(File)

Positives = Data[Data["Outcome"] == 1]
Negatives = Data[Data["Outcome"] == 0]

widgets = lol.widgets()

lol = PyReData()

styles = Stylesheet(name="Styles")


page = lol.page(
    "PIMA",
    stylesheets=[
        "http://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
        "Styles.css",
    ],
    scripts=[
        "http://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
        "http://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js",
        "http://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
    ],
)

jumbotron = widgets.container(
    page,
    Class=["jumbotron", "bg-dark"],
    id=["YAAS"],
    attributes=["style", "color:white"],
)
jumbotron.add(Node("p", content="HELLO WORLD"))

Data = Data.reset_index()
pd = Data.head(n=5)

container = widgets.container(
    page,
    name="container",
    attributes=[
        "style",
        "border:1px solid black;margin-left:100px;margin-right:100px;",
    ],
)

container.add(jumbotron)

container.add(
    widgets.image(
        page,
        "image.jpeg",
        stylesheet=styles,
        style=[["border", "10px solid black"], ["border-radius", "5px"]],
        id=["LOL"],centerize=True
    )
)

ax = sns.pairplot(Data, aspect=0.8)

container.add(widgets.plot(page, ax, centerize=True))

fig = plt.figure()
plt.plot([1, 4, 3, 3, 5], [1, 3, 4, 5, 4])
plt.show()
plt.close()

container.add(widgets.plot(page, fig))

container_fluid = widgets.container(page, Class=["container-fluid"])

container.add(widgets.attribute_plot(page, Data, centerize=True))

container.add(Node("br"))

container.add(
    widgets.table(
        page,
        pd,
        attributes=["style", "border:1px solid black;width:65%"],
        data_attributes=["style", "border:1px solid black;border-collapse: collapse;"],
        centerize=True,
        Class=["table table-bordered"],
        id=["YAAS"],
    )
)

container.add(Node("br"))
container.add(Node("br"))
container.add(Node("br"))

print("STYLESHEET")

print(styles.css)
print(styles.generate())

styles.compile()


page.render(container, "NAME")


page.compile()
