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


def remove_nth_from_end_with_linkedlist(head: ListNode, n: int) -> ListNode:
    p1, p2 = head, head
    for i in range(n):
        if not p2:
            return None
        #
        p2 = p2.next
    #
    if not p2:
        head = head.next
        return head
    #
    while p2.next:
        p2 = p2.next
        p1 = p1.next
    #

    p1.next = p1.next.next
    return head
#


def remove_nth_from_end(l: List[int], n: int) -> List[int]:
    """
    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.

    Follow up:
    Could you do this in one pass?

    >>> remove_nth_from_end([1], 1)

    >>> remove_nth_from_end([1,2,3,4,5], 2)
    [1, 2, 3, 5]
    """
    head = build_linked_list_from_list(l)
    res = remove_nth_from_end_with_linkedlist(head, n)
    return build_list_from_linked_list(res)
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
