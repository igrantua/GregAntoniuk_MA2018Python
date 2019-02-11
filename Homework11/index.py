"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided
# codeskulptor.set_timeout(60)
WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    no_dupl_list = []
    for item in list1:
        if item not in no_dupl_list:
            no_dupl_list.append(item)
    return no_dupl_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersect_list = []
    for item in list1:
        if item in list2:
            intersect_list.append(item)
    return intersect_list


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    merge_list = []
    list1_copy = list1[:]
    list2_copy = list2[:]
    while len(list1_copy) > 0 and len(list2_copy) > 0:
        if list1_copy[0] < list2_copy[0]:
            merge_list.append(list1_copy[0])
            list1_copy.pop(0)
        else:
            merge_list.append(list2_copy[0])
            list2_copy.pop(0)

    return merge_list + list1_copy + list2_copy


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    length = len(list1)
    if length <= 1:
        return list1
    else:
        left = merge_sort(list1[: length / 2])
        right = merge_sort(list1[length / 2:])
        return merge(left, right)

# Function to generate all strings for the word wrangler game


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """

    if len(word) == 0:
        return [""]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        all_strings = []
        all_strings.extend(rest_strings)

        for string in rest_strings:
            for ind in range(len(string) + 1):
                all_strings.append(string[0:ind] + first + string[ind:])

        return all_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
#    netfile = urllib2.urlopen(codeskulptor.file2url(filename))
#    words = netfile.readlines()
#    res =[]
#    for word in words:
#        res.append(word[:-2])
#    return res
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

