class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "Empty"

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


def reverse_list(linked_list: LinkedList):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


def merge_sort(head: Node) -> Node:
    if not head or not head.next:
        return head

    # middle search
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(l1: Node, l2: Node) -> Node:
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    for item in [8, 4, 5, 1, 3]:
        ll.insert_at_end(item)

    print(f"Original: {ll}")

    reverse_list(ll)
    print(f"Reversed: {ll}")

    ll.head = merge_sort(ll.head)
    print(f"Sorted: {ll}")

    # merge 2 sorted lists
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    for item in [5, 25, 15, 35]:
        ll_1.insert_at_end(item)
    for item in [30, 20, 10]:
        ll_2.insert_at_end(item)

    # sort both linked lists before merging
    ll_1.head = merge_sort(ll_1.head)
    ll_2.head = merge_sort(ll_2.head)

    merged_head = merge_two_sorted_lists(ll_1.head, ll_2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print(f"Merged: {merged_list}")
