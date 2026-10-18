class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # head <-> 1 <-> 2 <-> tail

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.num_items = 0
        self.key_to_node = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        target = self.key_to_node[key]

        target.prev.next = target.next
        target.next.prev = target.prev
        target.prev = self.tail.prev
        target.next = self.tail
        target.prev.next = target
        self.tail.prev = target

        return target.val


    def put(self, key: int, value: int) -> None:
        # if key exists, update it's value
        if key in self.key_to_node:
            self.get(key)
            self.key_to_node[key].val = value
            return

        # otherwise, add new node to tail
        new_node = Node(key, value)

        new_node.next = self.tail
        new_node.prev = self.tail.prev
        new_node.prev.next = new_node
        self.tail.prev = new_node
        self.num_items += 1
        self.key_to_node[key] = new_node

        # remove from head if capacity reached and remove from dictionary
        if self.num_items > self.capacity:
            del_key = self.head.next.key
            del self.key_to_node[del_key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.num_items -= 1
            
        return
    
    