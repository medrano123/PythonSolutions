# Giovanni Medrano

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    index = 0
    path = len(s) - 1

    for i in range(path, -1, -1):
        letter = ord(s[i]) - 96
        index = index + (letter * (26 ** i))
    step = const - (index % const)

    return step


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(string, hash_list):
    the_index = hash_word(string, len(hash_list))
    the_step = step_size(string, (26 // 2))
    while hash_list[the_index] != '':
        the_index = (the_index + the_step) % len(hash_list)
    hash_list[the_index] = string


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(string, hash):
    index = hash_word(string, len(hash))
    the_step = step_size(string, (26 // 2))

    while hash[index] != '':
        if hash[index] == string:
            yes = True
            return yes
        else:
            index = (the_step + index) % len(hash)
    no = False
    return no


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    string = s[:]
    if find_word(s, hash_memo):
        return True

    elif find_word(s, hash_table):
        for i in range(0, len(string)):
            string_new = s[:i] + s[i + 1:]

            if is_reducible(string_new, hash_table, hash_memo):
                insert_word(string_new, hash_memo)
                return True

    else:
        return False


def main():
    # create an empty word_list
    word_list = []
    # open the file words.txt
    words = open('words.txt', 'r')
    # read words from words.txt and append to word_list
    continues = True
    while continues:
        word = words.readline().strip('\n')
        if word == '':
            continues = False
        else:
            word_list.append(word)
    # close file words.txt
    words.close()
    # find length of word_list
    len_list = len(word_list)

    # determine prime number N that is greater than twice
    # th9e length of the word_list
    n = (2 * len_list)
    k = 1

    # create an empty hash_list
    hash_list = []
    # populate the hash_list with N blank strings
    hash_list = ['' for k in range(n)]

    # hash each word in word_list into hash_list
    # for collisions use double hashing

    for the_word in word_list:
        insert_word(the_word, hash_list)

    # create an empty hash_memo of size M
    hash_memo = []

    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    m = int(.2 * len(word_list))

    # populate the hash_memo with M blank strings
    hash_memo = ['' for index in range(m)]
    insert_word('i', hash_memo)
    insert_word('o', hash_memo)
    insert_word('a', hash_memo)

    # create an empty list reducible_words
    redu_words = []

    for i in word_list:
        redu_word = is_reducible(i, hash_list, hash_memo)
        if redu_word:
            redu_words.append(i)

    # print out the reducible words of length 10
    for x in redu_words:
        if len(x) == 10:
            print(x)


if __name__ == "__main__":
    main()
