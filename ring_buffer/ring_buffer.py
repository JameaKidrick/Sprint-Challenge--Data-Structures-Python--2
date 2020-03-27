from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if length of ringbuffer == capacity...
        if self.storage.length == self.capacity:
            # replace oldest element with new item
            self.storage.delete(self.current)
            self.storage.add_to_tail(item)
            self.current = self.current.prev
        else:
            # add new element to head
            self.storage.add_to_head(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.tail
        # # if element == None...
        while current_node != self.storage.head.prev:
        # returns each element in storage in order until it reaches tail (base)
            if current_node is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
