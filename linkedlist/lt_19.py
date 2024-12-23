class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not  head:
            return []
        dummy = ListNode(0, head)

        slow , fast,  = dummy , head
        for i in range(0, n):
            if fast:
                fast = fast.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        if slow.next is not None:
            slow.next= slow.next.next
           
        return dummy.next


def list_to_linked_list(elements):
    """Convert a list into a linked list."""
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    """Convert a linked list back to a list."""
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    return elements


if __name__ == "__main__":
    # Test cases in list format
    test_cases = [
        ([1, 2, 3, 4, 5], 2),  # Input: list, n
        ([1], 1),
        ([1, 2], 1),
    ]

    solution = Solution()
    for case in test_cases:
        input_list, n = case
        head = list_to_linked_list(input_list)
        updated_head = solution.removeNthFromEnd(head, n)
        result = linked_list_to_list(updated_head)
        print(f"Input: {input_list}, n={n} -> Output: {result}")
