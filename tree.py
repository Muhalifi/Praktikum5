class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def traverse(self, node):
        print(node.data)
        for child in node.children:
            self.traverse(child)

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat pohon
    tree = Tree("A")

    # Menambahkan anak-anak untuk simpul A
    node_B = TreeNode("B")
    node_C = TreeNode("C")
    node_D = TreeNode("D")

    tree.root.add_child(node_B)
    tree.root.add_child(node_C)
    tree.root.add_child(node_D)

    # Menambahkan anak-anak untuk simpul B
    node_E = TreeNode("E")
    node_F = TreeNode("F")

    node_B.add_child(node_E)
    node_B.add_child(node_F)

    # Menambahkan anak-anak untuk simpul C
    node_G = TreeNode("G")
    node_H = TreeNode("H")

    node_C.add_child(node_G)
    node_C.add_child(node_H)

    # Menambahkan anak-anak untuk simpul D
    node_I = TreeNode("I")

    node_D.add_child(node_I)

    # Melakukan penelusuran pohon
    print("Traversal:")
    tree.traverse(tree.root)