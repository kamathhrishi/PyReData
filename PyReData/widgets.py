from PyReData.ops import Item
import os


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
        centerize=False,
    ):

        Table = Item(
            "table", attributes=attributes, id=id, Class=None, centerize=centerize
        )

        columns = []

        if header_attributes is None:

            header_attributes = row_attributes

        for headers in data:

            columns.append(headers)

        head = Item("thead")
        header = Item("tr", attributes=row_attributes)

        for head in columns:

            header.add(Item("th", attributes=header_attributes, content=str(head)))

        head.add(header)
        Table.add(head)

        for index in data.index:
            row = Item("tr", attributes=row_attributes, Class=Class)
            for column in list(data):

                row.add(
                    Item(
                        "td",
                        attributes=data_attributes,
                        content=str(data[column][index]),
                    )
                )

            Table.add(row)

        return Table

    def plot(self, instance, plt):

        if not os.path.exists("plots"):
            os.makedirs("plots")

        path = "plots/" + str(instance.images) + ".png"
        plt.savefig(path)
        instance.images += 1

        image = self.image(path)

        return image

    def image(self, path, name="", attributes=None, id=None, Class=None):

        attributes = []
        attributes.append(["src", path])
        image = Item("img", attributes=attributes, id=id, Class=Class)

        return image

    def container(self, attributes=None, id=None, Class=None, header=None):

        container = Item("div", attributes=attributes, id=id, Class=Class)

        return container

    def navbar(self, attributes=None, id=None, Class=None):

        pass
