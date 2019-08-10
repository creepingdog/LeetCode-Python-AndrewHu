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


def swap_pairs_lined_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    #
    shadow_head = ListNode(None)
    shadow_head.next = head
    curr = shadow_head

    p1 = curr.next
    while p1 and p1.next:
        p2 = p1.next.next
        curr.next = p1.next
        curr.next.next = p1
        p1.next = p2
        curr = p1
        p1 = p2
    #
    return shadow_head.next
#


def swap_pairs(head: List[int]) -> ListNode:
    """
    Given a linked list, swap every two adjacent nodes and return its head.

    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.


    >>> swap_pairs([1,2,3,4])
    [2, 1, 4, 3]
    >>> swap_pairs([2])
    [2]
    >>> swap_pairs([2,5,9])
    [5, 2, 9]
    >>> swap_pairs([])
    []
    """
    head = build_linked_list_from_list(head)
    head = swap_pairs_lined_list(head)
    return build_list_from_linked_list(head)
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
