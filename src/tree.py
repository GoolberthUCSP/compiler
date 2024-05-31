class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Node(value))

    def traverse(self):
        print(self.value)
        if self.children:
            for child in self.children:
                child.traverse()

root = Node(25)
root.add_child(31)

child = root.children[0]
child.add_child(32)

root.traverse()