from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    #
#


def build_linked_list_from_list(l: List) -> ListNode:
    head, curr = None, None
    for i in l:
        if not head:
            head = ListNode(i)
            curr = head
        else:
            curr.next = ListNode(i)
            curr = curr.next
        #
    #
    return head
#


def build_list_from_linked_list(p: ListNode) -> List:
    l = list()
    while p:
        l.append(p.val)
        p = p.next
    #
    return l
#


def add_two_numbers_from_list(l1: List, l2: List) -> ListNode:
    """
    >>> add_two_numbers_from_list([2,4,6], [5,6,4,9])
    [7, 0, 1, 0, 1]


    """

    h = add_two_numbers(build_linked_list_from_list(l1),
                        build_linked_list_from_list(l2))
    return build_list_from_linked_list(h)
#


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

    """

    head, carry = None, 0

    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        s = v1 + v2 + carry
        if s > 9:
            carry = 1
            s = s - 10
        else:
            carry = 0
        #
        node = ListNode(s)
        if not head:
            head = node
            curr = head
        else:
            curr.next = node
            curr = node
        #
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    #
    if carry:
        node = ListNode(1)
        curr.next = node
    #
    return head
#


def add_two_numbers_2(l1: ListNode, l2: ListNode) -> ListNode:
    h, carry = None, 0
    while l1 or l2:
        if not l1:
            v = l2.val
            s, carry = (0, 1) if v==9 and carry==1 else (v+carry, 0)
            l2 = l2.next
        elif not l2:
            v = l1.val
            s, carry = (0, 1) if v==9 and carry==1 else (v+carry, 0)
            l1 = l1.next
        else:
            s = l1.val + l2.val + carry
            s, carry = (s-10, 1) if s>9 else (s, 0)
            l1 = l1.next
            l2 = l2.next
        #
        curr = ListNode(s)
        if not h:
            h = curr
            prev = curr
        else:
            prev.next = curr
            prev = curr
        #
    #
    if carry:
        curr = ListNode(1)
        prev.next = curr
    #
    return h
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
