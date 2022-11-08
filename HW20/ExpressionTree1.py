
#  Giovanni Medrano


import sys

class Node(object):

    def __init__(self, data):

        #initiate

        empty = None
        not_in = False

        self.data = data
        self.left_node = empty
        self.right_node = empty
        self.parental = empty
        self.been = not_in


class Tree(object):
    def __init__(self):

        empty = None
        self.root = empty

    def create_tree(self, expression):

        stack1 = Stack()
        expression = expression.split()
        operators = ['*', '/', '+', '-', '%', '//', '**']
        empty = None

        self.root = Node(empty)
        current = self.root

        for i in expression:

            if i == '(':
                n_node = Node(empty)
                current.left_node = n_node
                stack1.push(current)
                current = current.left_node

            elif i in operators:
                current.data = i
                stack1.push(current)

                n_node = Node(empty)

                current.right_node = n_node
                current = current.right_node

            elif i == ')':
                if stack1.size() != 0:
                    current = stack1.pop()

            else:
                current.data = i
                current = stack1.pop()

    def evaluate(self, Node1):
        empty = None
        operators = ['*', '/', '+', '-', '%', '//', '**']

        if Node1.left_node is empty and Node1.right_node is empty:
            return Node1.data
        else:
            result = eval(str(self.evaluate(Node1.left_node)) + Node1.data + str(self.evaluate(Node1.right_node)))
            result = float(result)
            return result

    def pre_order(self, Node1):
        empty = None
        if Node1 is not empty:

            print(Node1.data, end=' ')

            self.pre_order(Node1.left_node)
            self.pre_order(Node1.right_node)

    def post_order(self, Node1):
        empty = None

        if Node1 is not empty:

            self.post_order(Node1.left_node)
            self.post_order(Node1.right_node)

            print(Node1.data, end=' ')

class Stack(object):

    #initiate
    def __init__(self):
        self.the_stack = []

    # add item
    def push(self, item):
        self.the_stack.append(item)

    # remove item
    def pop(self):
        return self.the_stack.pop()

    # check item
    def peek(self):
        return self.the_stack[-1]

    # check stack
    def is_empty(self):
        return len(self.the_stack) == 0

    # return number
    def size(self):
        return len(self.the_stack)

def main():
    # read infix expression
    line = sys.stdin.readline()
    expression = line.strip()
    the_Tree = Tree()
    # create the tree
    the_Tree.create_tree(expression)
    print(expression, end='')
    print(' =', the_Tree.evaluate(the_Tree.root))

    print()
    print('Prefix Expression: ', end='')
    the_Tree.pre_order(the_Tree.root)

    print()
    print()
    # print the postfix

    print('Postfix Expression: ', end='')
    the_Tree.post_order(the_Tree.root)
    print()

if __name__ == "__main__":
    main()
