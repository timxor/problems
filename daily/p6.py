"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

"""

# 4 x 10 gigbit connections

# bitwise xor vs logical xor
#
# 0 xor 1 = 1/true
# 0


# prev=x
# next=y
# xor= x ^ y