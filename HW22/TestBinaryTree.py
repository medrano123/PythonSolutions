
# Giovanni Medrano

import sys

class Tree (object):

    def __init__(self):
        empty = None
        self.root = empty

    def is_similar(self, xNode):
        empty = None

        if xNode is empty and self.root is empty:
            yes = True
            return yes

        elif self.root is not empty and xNode is not empty:

            z = Tree()
            k = Tree()

            k.root = self.root.left_c
            z.root = self.root.right_c
            sim = k.is_similar(xNode.left_c) and self.root.data == xNode.data and z.is_similar(xNode.right_c)
            return sim
        no = False

        return no

    # Prints out all nodes at the given level
    def print_level(self, level):
        empty = None
        initial = 1
        root = self.root
        path = level - 1
        if root is not empty and level == initial:
            print(self.root.data, end=' ')
        if root is not empty:
            z = Tree()
            k = Tree()
            z.root = root.left_c
            k.root = root.right_c
            z.print_level(path)
            k.print_level(path)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        empty = None
        num_nodes = 1
        root = self.root
        if root is not empty and root.right_c is empty and root.left_c is empty :
            return 1

        elif root is not empty:

            z = Tree()
            k = Tree()
            z.root = root.left_c
            k.root = root.right_c
            num_nodes += z.num_nodes() + k.num_nodes()
            return num_nodes

        if root is empty:
            emp = 0
            return emp


    def insert(self, data):
        empty = None
        node_n = Node(data)

        if self.root is empty:
            self.root = node_n
            return
        else:
            p = self.root
            curr = self.root
            while curr is not empty:
                p = curr
                if curr.data > data :
                    curr = curr.left_c
                else:
                    curr = curr.right_c
            if p.data > data:
                p.left_c = node_n
            else:
                p.right_c = node_n

    def in_order(self, kNode):
        empty = None
        if kNode is not empty:

            self.in_order(kNode.left_c)
            print(kNode.data)
            self.in_order(kNode.right_c)


    # Returns the height of the tree

    def get_height(self):
        empty = None
        root = self.root
        if root is empty:
            return -1
        if root is not empty and root.right_c is empty and root.left_c is empty:
            return 0
        elif root is not empty:
            z = Tree()
            k = Tree()
            k.root = root.right_c
            z.root = root.left_c

            right_height = k.get_height()
            left_height = z.get_height()

            if left_height > right_height:
                lh = left_height + 1
                return lh
            else:
                rh = right_height + 1
                return rh
        else:
            return 0




class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item
    def push(self, i):
        self.stack.append(i)

    # remove an item
    def pop(self):
        return self.stack.pop()

    # check the item
    def peek(self):
        return self.stack[-1]

    # check empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements
    def size(self):
        return len(self.stack)



class Node(object):
    def __init__(self, data):
        empty = None
        self.left_c = empty
        self.right_c = empty
        self.data = data


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints


    tree1 = Tree()

    for x in tree1_input:
        tree1.insert(x)

    tree2 = Tree()

    for x in tree2_input:
        tree2.insert(x)

    tree3 = Tree()
    
    for x in tree3_input:
        tree3.insert(x)

    # Test is_similar for every combination of trees
    print(tree1.is_similar(tree2.root))
    print(tree1.is_similar(tree3.root))

    print(tree2.is_similar(tree1.root))
    print(tree2.is_similar(tree3.root))

    print(tree3.is_similar(tree1.root))
    print(tree3.is_similar(tree2.root))

    # Lets assume that tree1 and tree2 are different
    # print different levels
    tree1.print_level(2)  # assumed to print out on one line
    tree2.print_level(2)  # assumed to print out on one line

    tree1.print_level(5)  # assumed to print out on one line
    tree2.print_level(5)  # assumed to print out on one line

    # print heights
    print(tree1.get_height())
    print(tree2.get_height())

    # print num_nodes of each tree
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())
if __name__ == "__main__":
  main()