class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    # head <-> 1 <-> 2 <-> tail

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}
        self.capacity = capacity
        self.num_items = 0


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        # head <-> 1 <-> 2 <-> tail
        target = self.key_to_node[key]
        target.prev.next = target.next
        target.next.prev = target.prev
        target.prev = self.head
        target.next = self.head.next
        self.head.next = target
        target.next.prev = target

        return self.key_to_node[key].value


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            target = self.key_to_node[key]
            target.value = value
            self.get(key)
            return
        
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
       
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.num_items += 1

        if self.num_items > self.capacity:
            remove_key = self.tail.prev.key
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.num_items -= 1
            del self.key_to_node[remove_key]

        return 
    
            
       