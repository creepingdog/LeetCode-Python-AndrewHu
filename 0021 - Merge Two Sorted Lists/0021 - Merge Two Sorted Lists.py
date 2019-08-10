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
    if not p:
        return None
    #
    l = list()
    while p:
        l.append(p.val)
        p = p.next
    #
    return l
#


def merge_two_lists_linked_list(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    #
    if not l2:
        return l1
    #

    head = ListNode(None)
    c1, c2, c = l1, l2, head

    while c1 and c2:
        if c1.val <= c2.val:
            c.next = c1
            c1 = c1.next
        else:
            c.next = c2
            c2 = c2.next
        #
        c = c.next
    #
    if not c1:
        c.next = c2
    elif not c2:
        c.next = c1
    #
    return head.next
#


def merge_two_lists(l1: List[int], l2: List[int]) -> ListNode:
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

    >>> merge_two_lists([1,2,4], [1,3,4])
    [1, 1, 2, 3, 4, 4]
    >>> merge_two_lists([2], [1])
    [1, 2]
    """

    l1 = build_linked_list_from_list(l1)
    l2 = build_linked_list_from_list(l2)
    res = merge_two_lists_linked_list(l1, l2)
    return build_list_from_linked_list(res)
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
