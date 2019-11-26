from PyReData.ops import Node
import seaborn as sns
import matplotlib.pyplot as plt
import os


class Widgets:
    def __init__(self):

        pass

    def table(
        self,
        instance,
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
        style=None,
        stylesheet=None,
        centerize=False,
    ):

        if "table" in instance.content:

            instance.content["table"] += 1

        else:

            instance.content["table"] = 1

        Table = Node(
            "table", attributes=attributes, id=id, Class=None, centerize=centerize
        )

        columns = []

        if header_attributes is None:

            header_attributes = row_attributes

        for headers in data:

            columns.append(headers)

        thead = Node("thead")
        header = Node("tr", attributes=row_attributes)

        for head in columns:

            header.add(Node("th", attributes=header_attributes, content=str(head)))

        thead.add(header)
        Table.add(thead)

        for index in data.index:
            row = Node("tr", attributes=row_attributes, Class=Class)
            for column in list(data):

                row.add(
                    Node(
                        "td",
                        attributes=data_attributes,
                        content=str(data[column][index]),
                    )
                )

            Table.add(row)

        return Table

    def css_block(self):

        pass

    def plot(self, instance, plot, centerize=False, stylesheet=None):

        if not os.path.exists("plots"):
            os.makedirs("plots")

        if "plot" in instance.content:

            instance.content["plot"] += 1

        else:

            instance.content["plot"] = 1

        path = "plots/" + str(instance.content["plot"]) + ".png"
        plot.savefig(path)

        image = self.image(instance, path, centerize=centerize)

        return image

    def image(
        self,
        instance,
        path,
        name="",
        attributes=None,
        id=None,
        Class=None,
        style=None,
        centerize=False,
        stylesheet=None,
        style_id=None,
        style_class=None,
    ):

        if "img" in instance.content:

            instance.content["img"] += 1

        else:

            instance.content["img"] = 1

        if attributes is None:

            attributes = []

        if stylesheet:

            if id is not None:

                stylesheet.write(style, ID=id[0])

            elif Class is not None:

                stylesheet.write(style, Class=Class[0])

        attributes.append(["src", path])
        image = Node(
            "img",
            name=name,
            attributes=attributes,
            id=id,
            Class=Class,
            centerize=centerize,
        )

        return image

    def container(
        self,
        instance,
        name="",
        attributes=None,
        id=None,
        Class=None,
        header=None,
        centerize=False,
        style=None,
        stylesheet=None,
    ):

        if "div" in instance.content:

            instance.content["img"] += 1

        else:

            instance.content["img"] = 1

        container = Node(
            "div",
            name=name,
            attributes=attributes,
            id=id,
            Class=Class,
            centerize=centerize,
        )

        return container

    def image_gallery(
        self,
        instance,
        img,
        nrows=3,
        ncols=3,
        attributes=[],
        centerize=False,
        style=None,
        stylesheet=None,
    ):

        container_fluid = self.container(
            instance,
            Class=["container-fluid"],
            attributes=attributes,
            centerize=centerize,
        )

        for n_row in range(0, nrows):

            row = self.row(cols=ncols)
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

    def plot_gallery(
        self,
        instance,
        img,
        nrows=3,
        ncols=3,
        attributes=[],
        style=None,
        stylesheet=None,
    ):

        container_fluid = self.container(
            Class=["container-fluid"], attributes=attributes
        )

        for n_row in range(0, nrows):

            row = self.row(cols=ncols)
            container_fluid.add(row)

        plt_index = 0

        for row in range(0, nrows):

            for col in range(0, ncols):

                if plt_index < len(img):

                    container_fluid.child[row].child[col] = self.plot(
                        instance, img[plt_index]
                    )

                else:

                    print("Number of plots more than rows and columns")
                    row = nrows
                    col = ncols

                plt_index += 1

        return container_fluid

    def row(
        self,
        cols=1,
        attributes=None,
        id=None,
        Class="row",
        header=None,
        style=None,
        stylesheet=None,
    ):

        container = Node("div", attributes=attributes, id=id, Class=["row"])

        for i in range(0, cols):

            container.add(self.column())

        return container

    def attribute_plot(
        self, instance, data, centerize=False, style=None, stylesheet=None
    ):

        plots = []

        for key in data.keys():

            if key != "index":

                ax = sns.distplot(data[key], kde=False, rug=True)
                fig = ax.get_figure()
                plots.append(self.plot(instance, fig))

        return self.image_gallery(instance, plots, centerize=centerize)

    def column(
        self,
        attributes=None,
        id=None,
        Class="col",
        header=None,
        style=None,
        stylesheet=None,
    ):

        container = Node("div", attributes=attributes, id=id, Class=["col"])

        return container

    def navbar(self, attributes=None, id=None, Class=None, stylesheet=None):

        pass
