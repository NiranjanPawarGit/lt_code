# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper to create a linked list from a list
    @staticmethod
    def from_list(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper to convert linked list to list
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorder list as per LeetCode 143.
        Modify the list in-place without returning anything.
        """
        if not head:
            return
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        cur = slow
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            
        first = head
        second = prev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            
        


# Test harness
if __name__ == "__main__":
    # Example input
    # input_list = [1, 2, 3, 4]
    #input_list = [1, 2, 3, 4, 5]
    #input_list = [1, 2, 3, 4, 5, 6]
    input_list = [1, 2]
    head = ListNode.from_list(input_list)

    # Run the solution
    sol = Solution()
    sol.reorderList(head)

    # Output the result
    output_list = head.to_list()
    print("Reordered List:", output_list)
