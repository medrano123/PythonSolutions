#Giovanni Medrano


# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes

def sub_sets_boxes(box_list, sub_set, lowest):
    x = []
    highest = len(box_list)

    if lowest == highest:
        if len(sub_set) > 1:
            for i in range(len(sub_set) - 1):
                if does_fit(sub_set[i], sub_set[i + 1]) is False:
                    x.append(False)
            if False not in x:
                return [sub_set]
        return []


    else:
        y = sub_set[:]
        sub_set.append(box_list[lowest])
        return sub_sets_boxes(box_list, sub_set, lowest + 1) + sub_sets_boxes(box_list, y, lowest + 1)


# returns True if box1 fits inside box2

def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]


def main():
    # read the number of boxes
    in_file = open('boxes.in', 'r')
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)
    # create an empty list for the boxes
    box_list = []
    # read the boxes from the file
    for i in range(num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)
    # close the file
    in_file.close()
    # print to make sure that the input was read in correctly
    # print(box_list)
    # print()
    # sort the box list
    box_list.sort()
    # print the box_list to see if it has been sorted.
    # print(box_list)
    # print()
    sub_set = []
    lowest = 0
    subsets = sub_sets_boxes(box_list, sub_set, lowest)
    largest = len(subsets[0])
    line1 = 0
    for i in range(len(subsets)):
        if (len(subsets[i]) > largest):
            largest = len(subsets[i])
            line1 = largest
            if largest == 0:
                print(1)

    line2 = 0
    for i in range(len(subsets)):
        if len(subsets[i]) == largest:
            line2 += 1
    #            for j in subsets[i]:
    #                print(j)
    #            print()
    print(line1)
    print(line2)


if __name__ == "__main__":
    main()
