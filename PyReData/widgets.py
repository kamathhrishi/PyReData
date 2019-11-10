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

        thead = Item("thead")
        header = Item("tr", attributes=row_attributes)

        for head in columns:

            header.add(Item("th", attributes=header_attributes, content=str(head)))

        thead.add(header)
        Table.add(thead)

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

        if attributes is None:

            attributes = []

        attributes.append(["src", path])
        image = Item("img", attributes=attributes, id=id, Class=Class)

        return image

    def container(self, attributes=None, id=None, Class=None, header=None):

        container = Item("div", attributes=attributes, id=id, Class=Class)

        return container

    def image_gallery(self, instance, img, nrows=3, ncols=3, attributes=[]):

        widgets = instance.widgets()
        container_fluid = widgets.container(
            Class=["container-fluid"], attributes=attributes
        )

        for n_row in range(0, nrows):

            row = widgets.row(cols=ncols)
            container_fluid.add(row)

        img_index = 0

        for row in range(0, nrows):

            for col in range(0, ncols):

                if img_index < len(img):

                    container_fluid.child[row].child[col] = img[img_index]
                    img_index += 1

        if len(img) > (nrows * ncols):

            print("Number of images more than rows and columns")

        return container_fluid

    def plot_gallery(self):

        pass

    def row(self, cols=1, attributes=None, id=None, Class="row", header=None):

        container = Item("div", attributes=attributes, id=id, Class=["row"])

        for i in range(0, cols):

            container.add(self.column())

        return container

    def column(self, attributes=None, id=None, Class="col", header=None):

        container = Item("div", attributes=attributes, id=id, Class=["col"])

        return container

    def navbar(self, attributes=None, id=None, Class=None):

        pass
