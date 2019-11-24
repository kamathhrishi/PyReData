import PyReData
import pandas as pd
from PyReData.main import PyReData
from PyReData.ops import Node
import matplotlib.pyplot as plt
import seaborn as sns

lol = PyReData()

File = "pima-indians-diabetes.csv"

Data = pd.read_csv(File)

"""# 1. Number of times pregnant
# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. Diastolic blood pressure (mm Hg)
# 4. Triceps skin fold thickness (mm)
# 5. 2-Hour serum insulin (mu U/ml)
# 6. Body mass index (weight in kg/(height in m)^2)
# 7. Diabetes pedigree function
# 8. Age (years)
# 9. Class variable (0 or 1)"""

Positives = Data[Data["Outcome"] == 1]
Negatives = Data[Data["Outcome"] == 0]

widgets = lol.widgets()

lol = PyReData()

page = lol.page(
    "PIMA",
    stylesheets=[
        "http://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    ],
    scripts=[
        "http://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
        "http://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js",
        "http://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
    ],
)

jumbotron = widgets.container(
    Class=["jumbotron", "bg-dark"], id=["YAAS"], attributes=["style", "color:white"]
)
jumbotron.add(Node("p", content="HELLO WORLD"))

Data = Data.reset_index()
pd = Data.head(n=5)

container = widgets.container(
    name="container",
    attributes=[
        "style",
        "border:1px solid black;margin-left:100px;margin-right:100px;",
    ],
)

container.add(jumbotron)

ax = sns.pairplot(Data, aspect=0.8)

container.add(widgets.plot(page, ax, centerize=True))

fig = plt.figure()
plt.plot([1, 4, 3, 3, 5], [1, 3, 4, 5, 4])
plt.show()
plt.close()

container.add(widgets.plot(page, fig))

container_fluid = widgets.container(Class=["container-fluid"])

container.add(widgets.attribute_plot(page, Data, centerize=True))

container.add(Node("br"))

container.add(
    widgets.table(
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

print(container)

page.render(container, "NAME")

page.compile()
