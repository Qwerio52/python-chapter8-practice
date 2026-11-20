# 8.5 NetworkX 复杂网络图示例
import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    nodes = [1,2,3,4,5]
    edges = [(1,2),(1,3),(2,4),(3,5),(4,5)]
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=600)
    plt.title("NetworkX Demo Graph")
    plt.show()

    print("节点：", G.nodes)
    print("边：", G.edges)
    print("节点1的邻居：", list(G.neighbors(1)))

if __name__ == "__main__":
    main()