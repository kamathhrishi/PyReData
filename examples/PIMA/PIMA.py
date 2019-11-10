import PyReData
import pandas as pd
from PyReData.main import PyReData
from PyReData.ops import Item
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
        "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    ],
    scripts=[
        "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js",
        "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
    ],
)

jumbotron = widgets.container(
    Class=["jumbotron", "bg-dark"], id=["YAAS"], attributes=[["style", "color:white"]]
)
jumbotron.add(Item("p", content="HELLO WORLD"))

Data = Data.reset_index()
pd = Data.head(n=5)

container = widgets.container(
    attributes=[
        ["style", "border:1px solid black;margin-left:100px;margin-right:100px;"]
    ]
)

container.add(jumbotron)

ax = sns.distplot(Data["age"])
fig = ax.get_figure()

container.add(widgets.plot(lol, fig))

fig = plt.figure()
plt.plot([1, 4, 3, 3, 5], [1, 3, 4, 5, 4])
plt.show()
plt.close()


container.add(widgets.plot(lol, fig))

container_fluid = widgets.container(Class=["container-fluid"])

image = widgets.image(
    "Image.jpeg",
    id=["LOL"],
    Class=["LOL"],
    attributes=[["height", "200"], ["width", "300"], ["style", "margin:5px"]],
)


container.add(
    widgets.image_gallery(
        lol,
        [
            image,
            image,
            image,
            image,
            image,
            image,
            image,
            image,
            image,
            image,
            image,
            image,
        ],
        attributes=[["style", "margin-left:270px"]],
    )
)

container.add(Item("br"))

container.add(
    widgets.table(
        pd,
        attributes=[["style", "border:1px solid black;width:65%"]],
        data_attributes=[
            ["style", "border:1px solid black;border-collapse: collapse;"]
        ],
        centerize=True,
        Class=["table table-bordered"],
        id=["YAAS"],
    )
)

page.render(container, "NAME")
page.compile()
