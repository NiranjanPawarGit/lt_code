from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2

        if list1.val <= list2.val:
            new_head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            new_head = list2
            cur1 = list1
            cur2 = list2.next
        cur3 = new_head

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur3.next = cur1
                cur3 = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur3 = cur2
                cur2 = cur2.next

        if cur1 is None and cur2:
            while cur2:
                cur3.next = cur2
                cur3 = cur2
                cur2 = cur2.next

        if cur2 is None and cur1:
            while cur1:
                cur3.next = cur1
                cur3 = cur1
                cur1 = cur1.next
        return new_head


def list_to_linked_list(items):
    """Convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    """Convert a linked list back to a list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
    ]

    solution = Solution()
    for list1_vals, list2_vals in test_cases:
        list1 = list_to_linked_list(list1_vals)
        list2 = list_to_linked_list(list2_vals)
        print(f"List1: {list1_vals}, List2: {list2_vals}")
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        print(f"Merged List: {result}\n")
