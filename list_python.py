def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers+= x
    return sum_numbers
print(sum_list([1,2,-8]))

# python program to multiply all the items in a list

def multiply_list(items):
    tot=1
    for x in items:
        tot *=x
    return tot
print(multiply_list([1,2,-8]))

# python program to get the largest number from a list

def max_num_in_list(list):
    max=list[0]
    for a in list:
        if a > max:
            max=a
    return max
print(max_num_in_list([1,2,-8,0]))

# python a program to get the smallest number from a list.

def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min=a
    return min
print(smallest_num_in_list([1,2,-8,0]))

# python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of string.

def match_words(words):
    ctr=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))

# python program to get a list,sorted in increasing order by the
# last element in each tuple from a given list of non-empty tuples.

def last(n): return n[-1]
def sort_list_last(tuples):
    return sorted(tuples, key=last)
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

# python program to remove duplicates from list.

a=[10,20,30,20,10,50,60,40,80,50,40]

dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)

# python program to check a list is empty or not.

l=[]
if not l:
    print("list is empty")

#python program to clone or copy a list.

original_list=[10,22,44,23.4]
new_list=list(original_list)
print(original_list)
print(new_list)
