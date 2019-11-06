import PyRData
from main import PyReData
from PyRData import App
from PyRData import Page
from PyRData import Generate_Page
from PyRData import Plots
from PyRData import Stylesheet

import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

File = "diabetes.csv"

Data = pd.read_csv(File)

Positives = Data[Data["Outcome"] == 1]
Negatives = Data[Data["Outcome"] == 0]

print("\n")
print("\n")
print("\n")

lol = PyReData()

page = lol.page("LOL")


App1 = App("Analysis of Diabetes Mellitus")
Pg1 = Page(App1, "App", style="background:rgb(236, 236, 221);")

St = Stylesheet(Pg1)
style_link = St.CreateStyleSheet(Name="Custom")
Pg1.Add_StyleSheet(style_link)

Pg1.AddDiv(
    "Wrapper",
    style="border:1px solid black;width:1400px;background:white;margin-left:120px;padding-left:50px;",
)
Pg1.AddTitle(style="text-align:center;font-family:'Averia Sans Libre';", Div="Wrapper")
Pg1.Add_StyleSheet("https://fonts.googleapis.com/css?family=Averia Sans Libre")
Pg1.Add_StyleSheet("https://fonts.googleapis.com/css?family=Caveat Brush")
Pg1.AddBreak(Div="Wrapper")
Pg1.AddDiv(
    "Abstract",
    Div="Wrapper",
    style="background:rgb(235, 235, 224);padding:10px;width:1250px;",
    centerize=True,
)
Pg1.Header(
    "h3", "<u>Abstract</u>", Div="Abstract", centerize=True, style="margin-right:10px"
)
Pg1.AddText(
    """The population for this study was the Pima Indian population near
Phoenix, Arizona. That population has been under continuous
study since 1965 by the National Institute of Diabetes and
Digestive and Kidney Diseases because of its high incidence rate
of diabetes.Each community resident over 5 years of age
was asked to undergo a standardized examination every two years,
which included an oral glucose tolerance test. Diabetes was
diagnosed according to World Health Organization Criteria;
that is, if the 2 hour post-load plasma glucose was at least 200
mg/dl (11.1 mmol/l) at any survey examination or if the Indian
Health Service Hospital serving the community found a glucose
concentration of at least 200 mg/dl during the course of routine
medical care. In addition to being a familiar database to the
investigators, this data set provided a well validated data resource
in which to explore prediction of the date of onset of diabetes in a
longitudinal manner.
""",
    Div="Abstract",
    style="text-align:justify;margin:20px;",
)
Pg1.AddBreak(Div="Wrapper")
Pg1.AddImg(
    "PIMA.png",
    Div="Wrapper",
    centerize=True,
    style="height:250px;width:400px;border-radius:10px;",
)
Pg1.AddBreak(Div="Wrapper")
Attributes = [
    "<b>Pregnancies:</b> Number of times pregnant",
    "<b>Glucose:</b> Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
    "<b>BloodPressure:</b> Diastolic blood pressure (mm Hg)",
    "<b>SkinThickness:</b> Triceps skin fold thickness (mm)",
    "<b>Insulin:</b> 2-Hour serum insulin (mu U/ml)",
    "<b>BMI: </b> Body mass index (weight in kg/(height in m)^2)",
    "<b>DiabetesPedigreeFunction:</b> Diabetes pedigree function",
    "<b>Age:</b>Age (years)",
    "<b>Outcome:</b>Class variable (0 or 1)",
]

Pg1.Header("h2", "<u>Dataset Attributes</u>", Div="Wrapper", centerize=True)
Pg1.AddText("The following are the attributes of the dataset", Div="Wrapper")
Pg1.Create_List(Attributes, Div="Wrapper")
Pg1.Header("h2", "<u>Sample Data</u>", Div="Wrapper", centerize=True)
Pg1.AddText("The below table shows a sample of data columns and rows", Div="Wrapper")
Pg1.AddTable(
    Data.head(n=5),
    Div="Wrapper",
    Header_Style="border:1px solid black;",
    style="border:1px solid black;",
    centerize=True,
    Row_Style="border:1px solid black;",
    Col_Style="border:1px solid black;",
)
Pg1.AddBreak(Div="Wrapper")
Pg1.Header("h2", "Visualizations", Div="Data Stats", centerize=True)
Pg1.Header(
    "h2", "<u><b>Distribution of Variables</b></u>", Div="Wrapper", centerize=True
)
Pg1.Header("h3", "By Frequency", Div="Wrapper", centerize=True)
Pg1.Header(
    "h4",
    "Positive Outcomes",
    Div="Wrapper",
    style="margin-right:800px",
    centerize=False,
)
PL = Plots(Pg1)
PL.RenderPlot

plt.hist(Positives["Age"], color="r")
plt.xlabel("Age")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["Pregnancies"], color="r")
plt.xlabel("Pregnancies")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["Glucose"], color="r")
plt.xlabel("Glucose")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["BloodPressure"], color="r")
plt.xlabel("BloodPressure")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["SkinThickness"], color="r")
plt.xlabel("SkinThickness")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["Insulin"], color="r")
plt.xlabel("Insulin")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["BMI"], color="r")
plt.xlabel("BMI")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Positives["DiabetesPedigreeFunction"], color="r")
plt.xlabel("DiabetesPedigreeFunction")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

Pg1.Header(
    "h4",
    "Negative Outcomes",
    Div="Wrapper",
    style="margin-right:800px",
    centerize=False,
)


plt.hist(Negatives["Age"], color="g")
plt.xlabel("Age")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["Pregnancies"], color="g")
plt.xlabel("Pregnancies")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["Glucose"], color="g")
plt.xlabel("Glucose")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["BloodPressure"], color="g")
plt.xlabel("BloodPressure")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["SkinThickness"], color="g")
plt.xlabel("Skin Thickness")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["Insulin"], color="g")
plt.xlabel("Insulin")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["BMI"], color="g")
plt.xlabel("BMI")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

plt.hist(Negatives["DiabetesPedigreeFunction"], color="g")
plt.xlabel("DiabetesPedigreeFunction")
PL.RenderPlot(plt, Div="Wrapper")
plt.clf()

Pg1.Header("h3", "By Distribution", Div="Wrapper", centerize=True)

Pg1.Header(
    "h4",
    "Negative Outcomes",
    Div="Wrapper",
    style="margin-right:800px",
    centerize=False,
)


ax1 = sns.distplot(Negatives["Age"], color="r")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")

ax2 = sns.distplot(Negatives["Pregnancies"], color="r")
PL.RenderPlot(ax2, Type="SNS", Div="Wrapper")

ax3 = sns.distplot(Negatives["Glucose"], color="r")
PL.RenderPlot(ax3, Type="SNS", Div="Wrapper")

ax4 = sns.distplot(Negatives["BloodPressure"], color="r")
PL.RenderPlot(ax4, Type="SNS", Div="Wrapper")


ax5 = sns.distplot(Negatives["SkinThickness"], color="r")
PL.RenderPlot(ax5, Type="SNS", Div="Wrapper")


ax6 = sns.distplot(Negatives["Insulin"], color="r")
PL.RenderPlot(ax6, Type="SNS", Div="Wrapper")


ax = sns.distplot(Negatives["BMI"], color="r")
PL.RenderPlot(ax, Type="SNS", Div="Wrapper")


ax = sns.distplot(Negatives["DiabetesPedigreeFunction"], color="r")
PL.RenderPlot(ax, Type="SNS", Div="Wrapper")

Pg1.Header(
    "h4",
    "Negative Outcomes",
    Div="Wrapper",
    style="margin-right:800px",
    centerize=False,
)

ax1 = sns.distplot(Negatives["Age"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")

ax1 = sns.distplot(Negatives["Pregnancies"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")

ax1 = sns.distplot(Negatives["Glucose"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")

ax1 = sns.distplot(Negatives["BloodPressure"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")


ax1 = sns.distplot(Negatives["SkinThickness"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")


ax1 = sns.distplot(Negatives["Insulin"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")


ax1 = sns.distplot(Negatives["BMI"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")


ax1 = sns.distplot(Negatives["DiabetesPedigreeFunction"], color="g")
PL.RenderPlot(ax1, Type="SNS", Div="Wrapper")

Gen = Generate_Page(App1, Pg1)
Gen.SourceCode()
