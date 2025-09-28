import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Recursive addition of edges and positions for drawing"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, plot_title):
    """Draw a tree"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(plot_title, fontsize=14)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=3000, node_color=colors, font_size=12)
    plt.show()


def simple_color_gradient(steps=10, cmap_name='viridis', max_value=0.5):
    """
    Generates a color gradient using Matplotlib's built-in colormaps.
    Returns a list of 16-bit (HEX) colors.
    """
    # get a color map object
    cmap = plt.cm.get_cmap(cmap_name)

    colors = [mcolors.to_hex(cmap((i / steps) * max_value))
              for i in range(steps)]

    colors.reverse()

    return colors


def dfs_iterative(root, node_count=6):
    """Traversing the tree in depth."""
    if not root:
        return

    color_map = simple_color_gradient(steps=node_count)

    visited = set()
    visited_count = 0
    stack = [root]

    while stack:
        current_node = stack.pop()

        # check already visited nodes to to prevent reprocessing
        if current_node in visited:
            continue
        visited.add(current_node)

        # change node color according to its order
        if visited_count < len(color_map):
            current_node.color = color_map[visited_count]
        visited_count += 1

        # add nodes in reverse order (to guarantee LIFO)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


def bfs_iterative(root, node_count=6):
    """Traversing the tree in width."""
    if not root:
        return

    color_map = simple_color_gradient(steps=node_count)

    visited = set()
    visited_count = 0
    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        # check already visited nodes to to prevent reprocessing
        if current_node in visited:
            continue
        visited.add(current_node)

        # change node color according to its order
        if visited_count < len(color_map):
            current_node.color = color_map[visited_count]
        visited_count += 1

        # We add descendants from left to right
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # visualization of the depth traversal (DFS)
    dfs_iterative(root)
    draw_tree(root, "DFS")

    # visualization of the width traversal (BFS)
    bfs_iterative(root)
    draw_tree(root, "BFS")
