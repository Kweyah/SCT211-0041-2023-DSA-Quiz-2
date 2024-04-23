def detectCycle(head):
    slow = head
    fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Find beginning of cycle
    if fast and fast.next:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    return None
