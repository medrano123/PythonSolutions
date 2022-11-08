# Giovanni Medrano

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(string):
    # set initial conditions


    dict = {}
    dict['0'] = 0
    dict['1'] = 1
    dict['2'] = 2
    dict['3'] = 3
    dict['4'] = 4
    dict['5'] = 5
    dict['6'] = 6
    dict['7'] = 7
    dict['8'] = 8
    dict['9'] = 9
    dict['a'] = 10
    dict['b'] = 11
    dict['c'] = 12
    dict['d'] = 13
    dict['e'] = 14
    dict['f'] = 15
    dict['g'] = 16
    dict['h'] = 17
    dict['i'] = 18
    dict['j'] = 19
    dict['k'] = 20
    dict['l'] = 21
    dict['m'] = 22
    dict['n'] = 23
    dict['o'] = 24
    dict['p'] = 25
    dict['q'] = 26
    dict['r'] = 27
    dict['s'] = 28
    dict['t'] = 29
    dict['u'] = 30
    dict['v'] = 31
    dict['w'] = 32
    dict['x'] = 33
    dict['y'] = 34
    dict['z'] = 35
    dict['*'] = 36
    dict[''] = 37

    the_list = []
    count = 0
    longest_word = 0
    list_pad = []

    for i in string:
        if (len(i) > longest_word):
            longest_word = len(i)

    for j in string:
        new_list = ['*' * (longest_word - len(j))]
        list_pad.append(j + ''.join(new_list))

    for k in range(38):
        the_list.append(Queue())

    val = 2
    while (count != val):
        path = longest_word - 1

        for i in range(path, -1, -1):

            for j in list_pad:
                sol = dict[j[i]]
                the_list[sol].enqueue(j)

            while not the_list[36].is_empty():
                the_list[37].enqueue(the_list[36].dequeue())


            for k in range(36):
                while not the_list[k].is_empty():
                    the_list[37].enqueue(the_list[k].dequeue())

            next_word = []

            while not the_list[37].is_empty():
                next_word.append(the_list[37].dequeue())
            list_pad = next_word

        count += 1

        return [e.strip('*') for e in list_pad]


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # print word_list
    # print(word_list)
    max_word = max(word_list)
    min_word = min(word_list)
    # print(max_word)
    # print(min_word)

    # use radix sort to sort the word_list
    final_list = radix_sort(word_list)

    # print the sorted_list
    print(final_list)


if __name__ == "__main__":
    main()
