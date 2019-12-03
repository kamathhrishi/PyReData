from PyReData.stylesheets import Stylesheet
from PyReData.exceptions import IdentifierError
from PyReData.page import Page
from PyReData.widgets import Widgets

import pytest


def test_styleName():

    sheet1 = Stylesheet(name="Styles")
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], name="h1")
    assert sheet1.generate() == "h1{color:yellow;font-weight:bold;}\n"


def test_styleID():

    sheet1 = Stylesheet(name="Styles")
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], ID="h1")
    assert sheet1.generate() == "#h1{color:yellow;font-weight:bold;}\n"


def test_styleClass():

    sheet1 = Stylesheet(name="Styles")
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], Class="h1")
    assert sheet1.generate() == ".h1{color:yellow;font-weight:bold;}\n"


def test_noidentifier():

    with pytest.raises(IdentifierError):

        sheet1 = Stylesheet(name="Styles")
        sheet1.write([["color", "yellow"], ["font-weight", "bold"]])


def test_defaultStylesheet():

    styles = Stylesheet(name="Styles")

    page = Page("Test", def_stylesheet=styles)

    widgets = Widgets()
    container = widgets.container(page)

    container.add(
        widgets.image(
            page,
            "image.jpeg",
            style=[["border", "10px solid black"], ["border-radius", "5px"]],
            id=["image"],
        )
    )

    assert styles.generate() == "#image{border:10px solid black;border-radius:5px;}\n"
    
def test_defaultStylesheet_cont():

    styles = Stylesheet(name="Styles")

    page = Page("Test", def_stylesheet=styles)

    widgets = Widgets()
    cont_lol= widgets.container(
    page,
    name="container",
    attributes=[
        "style",
        "border:1px solid black;margin-left:100px;margin-right:100px;",
    ],
    style=[["border", "10px solid black"], ["border-radius", "5px"]]
    )
    
    print(styles.generate())

    assert styles.generate() == "#image{border:10px solid black;border-radius:5px;}\n"
    
test_defaultStylesheet_cont()

