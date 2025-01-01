class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def build_multilevel_doubly_linked_list(values):
    """Helper function to create a multilevel doubly linked list from a nested list."""
    if not values:
        return None

    dummy = Node(0)
    current = dummy
    stack = []

    for val in values:
        if val is None:  
            current = stack.pop()
        else:
            new_node = Node(val)
            current.next = new_node
            new_node.prev = current
            current = new_node
            if isinstance(val, list):
                stack.append(current)
                current.child = build_multilevel_doubly_linked_list(val)

    return dummy.next

def print_doubly_linked_list(head):
    """Helper function to print a doubly linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        """
        Implement the logic to flatten the multilevel doubly linked list.
        """
        if not head:
            return head
        cur = head
        while cur:
            if cur.child:
                childlist = self.flatten(cur.child)
                cur.child = None
                nextparent = cur.next
                cur.next = childlist
                childlist.prev = cur
                present = childlist
                while present:
                    if present.next is None:
                        if nextparent:
                            present.next = nextparent
                            nextparent.prev = present
                        else:
                            present.next = None
                        break
                    present = present.next
            
            cur = cur.next
        return head
            
        

if __name__ == "__main__":
    values = [1, 2, 3, [4, 5, 6], 7, [8, 9]]  # Nested list to create the multilevel doubly linked list

    head = build_multilevel_doubly_linked_list(values)

    print("Original list:")
    print_doubly_linked_list(head)

    solution = Solution()
    flat_head = solution.flatten(head)

    print("Flattened list:")
    print_doubly_linked_list(flat_head)
