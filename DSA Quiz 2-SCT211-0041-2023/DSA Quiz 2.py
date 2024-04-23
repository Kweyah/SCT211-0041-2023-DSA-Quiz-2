def hasCycle(head):
    slow, fast = head, head

    # Move slow pointer by one step and fast pointer by two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast meet, there is a cycle
        if slow == fast:
            return True

    # If we reach here, there is no cycle
    return False
