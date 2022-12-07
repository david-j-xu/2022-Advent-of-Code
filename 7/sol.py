import math


class Node:
    def __init__(self, parent, name) -> None:
        self.children = {}
        self.files = set()
        self.parent = parent
        self.name = name
        self.size = 0


root = Node(None, "/")
pwd = root


with open("7/input.txt") as f:
    for line in f.readlines():
        if line.startswith("$ cd"):
            if line.startswith("$ cd .."):
                pwd = pwd.parent
            elif line.startswith("$ cd /"):
                pwd = root
            else:
                name = line[5:-1]
                if name not in pwd.children:
                    pwd.children[name] = Node(pwd, name)
                pwd = pwd.children[name]
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            name = line[4:-1]
            pwd.children[name] = Node(pwd, name)
        else:
            file_name = line.split(" ")[1]
            if file_name not in pwd.files:
                pwd.size += int(line.split(" ")[0])
                pwd.files.add(file_name)

running_sum = 0


def dfs(node):
    for _, child in node.children.items():
        dfs(child)

    if node.size <= 100000:
        global running_sum
        running_sum += node.size

    if node.parent:
        node.parent.size += node.size


dfs(root)

print(running_sum)

# b

min = math.inf
threshold = 30000000 - (70000000 - root.size)


def dfs(node):
    global min
    for _, child in node.children.items():
        dfs(child)

    if node.size <= min and node.size > threshold:
        min = node.size


dfs(root)

print(min)
