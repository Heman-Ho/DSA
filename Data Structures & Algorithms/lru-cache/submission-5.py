class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    # head == most recently used item
    # tail == least recently used item

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = 0
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        target_node = self.key_to_node[key]
        target_node.prev.next = target_node.next
        target_node.next.prev = target_node.prev
        
        target_node.next = self.head.next
        target_node.prev = self.head
        target_node.next.prev = target_node
        self.head.next = target_node
        return target_node.value

    def put(self, key: int, value: int) -> None:
        # case: key in cache
        if key in self.key_to_node:
            self.get(key)
            self.key_to_node[key].value = value
            return
        
        # case: key not in cache -> add to cache, evict if necessary
        new_node = Node(key, value, self.head.next, self.head)
        new_node.next.prev = new_node
        self.head.next = new_node
        self.items += 1
        self.key_to_node[key] = new_node

        # evict if necessary
        if self.items > self.capacity:
            del self.key_to_node[self.tail.prev.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.items -= 1
            
        
