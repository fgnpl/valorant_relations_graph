import networkx as nx
from pyvis.network import Network
import pandas as pd
from IPython.display import display, HTML


global graph
graph = nx.MultiDiGraph()


def add_connection(name, target, status, direction, color=None, g=graph):
    if color is None:
        if status == "Friends":
            color = "#5DFA57"
        elif status == "Enemies":
            color = "#6C64FA"
        elif status == "Neutral":
            color = "#FAE889"
        elif status == "Love":
            color = "#F982C4"

    if direction == "Undirected":
        g.add_edge(target, name, color=color)
    g.add_edge(name, target, color=color)


def add_person(name, g=graph):
    g.add_node(name, title=name)


def get_adjacent(name, pr=True, g=graph):
    s = set()
    for edge in g.edges.data():
        if name in edge:
            if edge[0] == name:
                s.add(edge[1])
            else:
                s.add(edge[0])
    if pr:
        print(f"Neighbors of {name}:", ', '.join(s))
    return list(s)


def create_subgraph(name):
    s = get_adjacent(name, False)
    global subgraph
    subgraph = nx.MultiDiGraph()
    add_person(name, subgraph)
    for el in s:
        add_person(el, subgraph)
        for edge in graph.edges.data():
            if el in edge and name in edge:
                if edge[0] == name:
                    subgraph.add_edge(name, el, color=edge[2]["color"])
                else:
                    subgraph.add_edge(el, name, color=edge[2]["color"])


data = pd.read_excel(r".\dataset.xlsx")

for index, row in data.iterrows():
    name = row["Name"].strip()
    target = row["Target"].strip()
    status = row["Status"].strip()
    direction = row["Direction"].strip()

    if name not in graph:
        add_person(name)
    if target not in graph:
        add_person(target)

    add_connection(name, target, status, direction)

nt = Network('1080px', '1920px', notebook=True, directed=True, bgcolor="#222222", font_color="white", cdn_resources='remote')
nt.repulsion(node_distance=250, spring_length=200)
nt.from_nx(graph)
html = nt.generate_html()
with open("nx.html", mode='w', encoding='utf-8') as fp:
        fp.write(html)
display(HTML(html))


print('Enter "exit" to terminate the program', end="\n\n")

print("Enter a command:")
command = input()
while command != "exit":
    nt = Network('1080px', '1920px', notebook=True, directed=True, bgcolor="#222222", font_color="white")
    nt.repulsion(node_distance=250, spring_length=200)
    if "show_graph" not in command:
        try:
            eval(command)
        except:
            print("Command is invalid")
    if "create_subgraph" in command:
        nt.from_nx(subgraph)
    else:
        nt.from_nx(graph)
    with open("nx.html", mode='w', encoding='utf-8') as fp:
        fp.write(html)
    display(HTML(html))
    print("Enter a command:")
    command = input()