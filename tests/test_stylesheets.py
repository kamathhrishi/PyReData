from PyReData.stylesheets import StyleSheet
from PyReData.exceptions import IdentifierError

import pytest


def test_styleName():

    sheet1 = StyleSheet()
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], name="h1")
    assert sheet1.generate() == "h1{color:yellow;font-weight:bold;}\n"


def test_styleID():

    sheet1 = StyleSheet()
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], ID="h1")
    assert sheet1.generate() == "#h1{color:yellow;font-weight:bold;}\n"


def test_styleClass():

    sheet1 = StyleSheet()
    sheet1.write([["color", "yellow"], ["font-weight", "bold"]], Class="h1")
    assert sheet1.generate() == ".h1{color:yellow;font-weight:bold;}\n"


def test_noidentifier():

    with pytest.raises(IdentifierError):

        sheet1 = StyleSheet()
        sheet1.write([["color", "yellow"], ["font-weight", "bold"]])
