from itertools import count
#Write your implementation here
def sum(a, b):
    sum = a + b
    return sum

def isletter(char):
    result = char.isalpha() #Check if is alphabetic return boolean
    return result

def count_instances(phrase):
    phrase = phrase.lower() #All characters to lower case
    my_dyct = {}
    for letter in phrase:
      if letter.isalpha():  #Check if is alphabetic
        my_dyct[letter] = phrase.count(letter)
    return my_dyct

def reverse_words(phrase):
    reverse_phrase = []
    split_phrase = phrase.split(" ",)[::-1]
    for index in split_phrase:
      reverse_phrase.append(index)
    reverse_phrase = " ".join(reverse_phrase)
    return reverse_phrase

def reverse_chars_in_odd_words(phrase):
    split_phrase = phrase.split(" ",)
    for index in range(len(split_phrase)):
      if index % 2 != 0:
        split_phrase[index] = split_phrase[index][::-1]
      odd_words = " ".join(split_phrase)
    return odd_words

def get_children(tree, parent):
    children_list = []
    for index in range(len(tree)):
      if tree[index][0] == parent:
        children_list.append(tree[index][1])
    return children_list

def get_increment(lst):
    increment_list = []
    for index in range(len(lst),1,-1):
      increment = lst[index-1] - lst[index-2]
      increment_list.append(increment)
    for index in range(1,len(increment_list)):
      if increment_list[index] == increment_list[index-1]:
        increment = increment_list[0]
      else:
        increment = -1
        break
    return increment

