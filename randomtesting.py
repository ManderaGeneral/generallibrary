import pickle

from generallibrary import *



from generalfile import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option("precision", 2)

# path = Path("C:/Users/Mandera/Desktop/analyzetest/df.tsv")
# path.spreadsheet.write(df, overwrite=True)
# path.open_folder()



aggregations = {
    "Klick": "mean",
    "Kr": "mean",
    "Klick/Kr": "mean",
}


def scatter(df, x, y, *group):
    print("\n", df)

    plt.figure(f"{y} genom {x} - {', '.join(group) or 'Alla'}")

    if group:
        df = df.groupby(list(group), as_index=True).aggregate(aggregations)
        for i, series in df.iterrows():
            plt.scatter(series[x], series[y], pow(series[y] / series[x], 3) * 10, label=series.name)
        plt.legend()

    else:
        plt.scatter(df[x], df[y], pow(df[y] / df[x], 3) * 10)


    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim(0, 100)
    plt.ylim(0, 100)



entries = combine(
    Fras=("Klocka", "Ur"),
    Plats=("Sverige", "Stockholm"),
    Dag=("12/5-21", "13/5-21", "14/5-21"),
)

df = pd.DataFrame(entries)
df["Klick"] = np.random.randint(1, 70, size=len(df))
df["Kr"] = df["Klick"] * np.random.randint(4, 13, size=len(df)) / 10
df["Klick/Kr"] = df["Klick"] / df["Kr"]



scatter(df, "Kr", "Klick")
# scatter(df, "Kr", "Klick", "Fras")
# scatter(df, "Kr", "Klick", "Plats")
scatter(df, "Kr", "Klick", "Fras", "Plats")
scatter(df, "Kr", "Klick", "Dag")


plt.show()

































































# from generalpackager import Packager
# Packager().graph()

# class A(NetworkDiagram):
#     def __init__(self, x):
#         self.x = x
#
#     def __repr__(self):
#         return str(self.x)

# process = A("generalprocess")
# vector = A("generalvector")
# neural = A("generalneural")
# neat = A("generalneat")
# gui = A("generalgui")
# draw = A("generaldraw")
# stock = A("generalstock")
# analyze = A("generalanalyze")
# actioneer = A("generalactioneer")
#
# process.add_node(stock)
# process.add_node(analyze)
# process.add_node(stock)
#
# vector.add_node(draw)
# vector.add_node(gui)
#
# neural.add_node(neat)
#
# neat.add_node(actioneer)
#
# gui.add_node(analyze)
# gui.add_node(draw)
# gui.add_node(neural)
# gui.add_node(neat)
# gui.add_node(actioneer)
# gui.add_node(stock)
#
# draw.add_node(neural)
# draw.add_node(neural)
#
# stock.add_node(actioneer)
#
# analyze.add_node(stock)
# analyze.add_node(neural)
#
# actioneer.graph()


# Must be missing something, blocked nodes might not be right


# 3 Triangles in grid
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# e = d.add_node("e")
# a.add_node(c)
# b.add_node(d)
# b.add_node(e)


# Square with triangle inside
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# d.add_node(a)
# e = a.add_node("e")
# e.add_node(d)


# Pentagon with square inside
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# e = d.add_node("e")
# e.add_node(a)
# f = e.add_node("f")
# f.add_node(c)


# 3 Triangles with 1 center node  HERE **
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# c.add_node(a)
# a.add_node(d)
# b.add_node(d)
#
# a.graph()



# loops = a.get_loops()
# small = loops[0]
# big = loops[1]
# assert len(small.nodes) < len(big.nodes)

# big.add_node(child=small)
# print(big.unavailable_nodes())
# print(small.unavailable_nodes())
# print(big.all_nodes())

# print(big.can_contain(small))
# print(small.can_contain(big))


# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# c.add_node(a)
#
# d = c.add_node("d")
# d.add_node(a)
#
#
# print(a.graph())



