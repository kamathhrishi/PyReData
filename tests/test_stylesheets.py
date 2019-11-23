from PyReData.stylesheets import StyleSheet


def test_style():

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
