

# Giovanni Medrano

import sys

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # the Constructor

    def __init__(self):
        self.first = None
        self.last = None
        self.num_links = 0

    # Insert an element (value) in the list
    def insert(self, data):

        begin_nlink = Link(data)

        if self.first is None:
            self.last = begin_nlink

        begin_nlink.next = self.first
        self.last.next = begin_nlink
        self.first = begin_nlink
        self.num_links += 1

    # Find the link with the given data (value)
    def find(self, data):
        c = self.first


        if c is None:
            return None

        while c.data != data:
            if c.next is None:
                return None

            else:
                c = c.next

        return c

    # Delete a link with a given data (value)
    def delete(self, data):
        #initiate
        p = self.first
        c = self.first

        if c is None:
            return None

        while c.data != data:
            if c.next is None:
                return None

            else:
                p = c
                c = c.next
                
        if c == self.first:
            self.first = self.first.next



        else:
            p.next = c.next
        return c

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        p = start
        c = start
        path = n - 1
        for x in range(path):
            p = c
            c = c.next
        if self.last == c:
            self.last = p
        p.next = c.next
        self.num_links -= 1

        print(c.data)
        return c.next

    # Return a string representation of a Circular List
    def __str__(self):
        c = self.first
        l = self.last
        x = 0
        while c != self.last:
            if x % 10 == 0:
                print()
            print(c.data, end='  ')
            c = c.next
            x = x + 1
        print(c.data)
        print()


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    soldiers = int(line)
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    begin_count = int(line)
    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim = int(line)

    the_circle = CircularList()




    for x in range(soldiers, 0, -1):
        the_circle.insert(x)
    start_pos = the_circle.find(begin_count)
    while the_circle.num_links > 0:
        start_pos = the_circle.delete_after(start_pos, elim)


if __name__ == "__main__":
    main()
