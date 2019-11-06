from ops import Item


class Widgets:
    def __init__(self):

        pass

    def table(
        self,
        data,
        name="",
        attributes=None,
        id=None,
        Class=None,
        header_attributes=None,
        header_id=None,
        header_class=None,
        row_attributes=None,
        row_id=None,
        row_class=None,
        data_attributes=None,
        data_id=None,
        data_class=None,
    ):

        Table = Item("table", attributes=attributes, id=id, Class=None)

        columns = []

        for headers in data:

            columns.append(headers)

        for index in range(0, len(data)):

            row = Item("tr", attributes=row_attributes, Class=Class)

            for column in columns:

                row.add(
                    Item(
                        "td",
                        attributes=data_attributes,
                        content=str(data[column][index]),
                    )
                )

            Table.add(row)

        return Table

    def image(self, path, name="", attributes=None, id=None, Class=None):

        attributes = []
        attributes.append(["src", path])
        image = Item("img", attributes=attributes, id=id, Class=Class)

        return image

    def container(self, attributes=None, id=None, Class=None, header=None):

        container = Item("div", attributes=attributes, id=id, Class=Class)

        return container
