from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur is not None:
            print(f"Reversing node with value: {cur.val}")
            post = cur.next
            cur.next = prev
            prev = cur
            cur = post   
        return prev


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
        [1, 2, 3, 4, 5],  # Example linked list
        [1],
        [],
    ]

    solution = Solution()
    for case in test_cases:
        head = list_to_linked_list(case)
        print(f"Original List: {case}")
        reversed_head = solution.reverseList(head)
        result = linked_list_to_list(reversed_head)
        print(f"Reversed List: {result}\n")
