# Giovanni Medrano


import sys

class the_Node(object):

    def __init__(self, data):
        empty = None
        self.right_c = empty
        self.left_c = empty
        self.data = data

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        path = len(encrypt_str)
        path2 = encrypt_str[0]
        self.root = the_Node(path2)
        for x in range(1, path):
            if (ord(encrypt_str[x]) == 32 or (97 <= ord(encrypt_str[x]) <= 122)):
                self.insert(encrypt_str[x])


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, char):
        space = ''
        if self.search(char) == space:
            node_new = the_Node(char)
            empty = None
            curr = self.root
            prev = self.root
            while curr is not empty:
                if ord(curr.data) > ord(char):
                    prev = curr
                    curr = curr.left_c
                else:
                    prev = curr
                    curr = curr.right_c
            if ord(prev.data) > ord(char):
                prev.left_c = node_new
            else:
                prev.right_c = node_new

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.

    def search(self, char):
        curr = self.root
        left = '<'
        right = '>'
        if char == curr.data:
            star = '*'
            return star
        l_n_r = []
        while curr is not None:
            if ord(char) == ord(curr.data):
                return l_n_r
            elif ord(curr.data) > ord(char):
                l_n_r.append(left)
                curr = curr.left_c
            else:
                l_n_r.append(right)
                curr = curr.right_c
        space = ''
        return space


    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, string):
        curr = self.root
        empty = None
        for char in string:
            left = '<'
            right = '>'
            star = '*'
            if char == right:
                curr = curr.right_c
            elif char == left:
                curr = curr.left_c
            elif char == star:
                curr = self.root

        if curr is empty or curr.data is empty:
            return ''
        else:
            return curr.data


    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, string):

        encrypt = ''
        string = string.lower()
        path = string[:-1]
        for char in path:
            string1 = ''
            exclemation = '!'
            encrypt = encrypt + string1.join(self.search(char))
            if string1.join(self.search(char)) != string1:
                encrypt = encrypt + exclemation
        string2 = ''
        encrypt = encrypt + string2.join(self.search(string[-1]))
        return encrypt

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, string):

        decrypt = ''
        exclemation = '!'
        string = string.split(exclemation)

        for x in string:
            decrypt = decrypt + self.traverse(x)
        return decrypt


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()