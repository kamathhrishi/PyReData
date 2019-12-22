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
        header_style=None,
        header_id=None,
        header_class=None,
        row_attributes=None,
        row_style=None,
        row_id=None,
        row_class=None,
        data_attributes=None,
        data_style=None,
        data_id=None,
        data_class=None,
        style=None,
        stylesheet=None,
        centerize=False,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        if type(row_id) == str:

            row_id = [row_id]

        if type(row_class) == str:

            row_class = [row_class]

        if type(data_id) == str:

            data_id = [data_id]

        if type(data_class) == str:

            data_class = [data_class]

        if "table" in instance.content:

            instance.content["table"] += 1

        else:

            instance.content["table"] = 1

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        Table = Node(
            "table",
            attributes=attributes,
            stylesheet=stylesheet,
            style=style,
            id=id,
            Class=None,
            centerize=centerize,
        )

        columns = []

        if header_attributes is None:

            header_attributes = row_attributes

        for headers in data:

            columns.append(headers)

        thead = Node("thead")
        print(id)
        header = Node("tr", attributes=row_attributes, id=id[0] + "-" + "row")

        for head in columns:

            header.add(
                Node(
                    "th",
                    attributes=header_attributes,
                    style=header_style,
                    stylesheet=stylesheet,
                    content=str(head),
                    id=id[0] + "-" + "head",
                )
            )

        thead.add(header)
        Table.add(thead)

        for index in data.index:
            row = Node(
                "tr",
                attributes=row_attributes,
                style=row_style,
                stylesheet=stylesheet,
                Class=Class,
                id=[id[0] + "-" + "rows"],
            )
            for column in list(data):

                row.add(
                    Node(
                        "td",
                        attributes=data_attributes,
                        content=str(data[column][index]),
                        style=data_style,
                        stylesheet=stylesheet,
                        id=[id[0] + "-" + "data"],
                    )
                )

            Table.add(row)

        return Table

    def plot(
        self,
        instance,
        plot,
        id=None,
        Class=None,
        centerize=False,
        stylesheet=None,
        style=None,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        if not os.path.exists("plots"):
            os.makedirs("plots")

        if "plot" in instance.content:

            instance.content["plot"] += 1

        else:

            instance.content["plot"] = 1

        path = "plots/" + str(instance.content["plot"]) + ".png"
        plot.savefig(path)

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        image = self.image(
            instance,
            path,
            id=id,
            Class=Class,
            centerize=centerize,
            style=style,
            stylesheet=stylesheet,
        )

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

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        if "img" in instance.content:

            instance.content["img"] += 1

        else:

            instance.content["img"] = 1

        if attributes is None:

            attributes = []

        attributes.append(["src", path])

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        image = Node(
            "img",
            name=name,
            attributes=attributes,
            id=id,
            Class=Class,
            centerize=centerize,
            stylesheet=stylesheet,
            style=style,
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

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        if "div" in instance.content:

            instance.content["img"] += 1

        else:

            instance.content["img"] = 1

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        container = Node(
            "div",
            name=name,
            attributes=attributes,
            id=id,
            Class=Class,
            centerize=centerize,
            stylesheet=stylesheet,
            style=style,
        )

        return container

    def image_gallery(
        self,
        instance,
        img,
        nrows=3,
        ncols=3,
        attributes=[],
        Class=None,
        id=None,
        centerize=False,
        style=None,
        stylesheet=None,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        class_name = ["container-fluid"]

        for name in Class:

            class_name.append(name)

        container_fluid = self.container(
            instance,
            Class=class_name,
            id=id,
            attributes=attributes,
            centerize=centerize,
        )

        for n_row in range(0, nrows):

            row = self.row(instance, cols=ncols)
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
        Class=None,
        id=None,
        nrows=3,
        ncols=3,
        attributes=[],
        style=None,
        stylesheet=None,
    ):

        class_name = ["container-fluid"]

        for name in Class:

            class_name.append(name)

        container_fluid = self.container(Class=class_name, attributes=attributes)

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
        instance,
        cols=1,
        attributes=None,
        id=None,
        Class="row",
        header=None,
        style=None,
        stylesheet=None,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        container = Node("div", attributes=attributes, id=id, Class=["row"])

        for i in range(0, cols):

            container.add(self.column(instance))

        return container

    def attribute_plot(
        self,
        instance,
        data,
        Class=None,
        id=None,
        centerize=False,
        style=None,
        stylesheet=None,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        plots = []

        for key in data.keys():

            if key != "index":

                ax = sns.distplot(data[key], kde=False, rug=True)
                fig = ax.get_figure()
                plots.append(self.plot(instance, fig))

        return self.image_gallery(
            instance,
            plots,
            stylesheet=stylesheet,
            Class=Class,
            id=id,
            style=style,
            centerize=centerize,
        )

    def column(
        self,
        instance,
        attributes=None,
        id=None,
        Class="col",
        header=None,
        style=None,
        stylesheet=None,
    ):

        if type(id) == str:

            id = [id]

        if type(Class) == str:

            Class = [Class]

        container = Node("div", attributes=attributes, id=id, Class=["col"])

        if not stylesheet:

            if instance.def_stylesheet:

                stylesheet = instance.def_stylesheet

        return container

    def navbar(self, attributes=None, id=None, Class=None, stylesheet=None):

        pass
