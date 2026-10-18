class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        
        # Sentinel head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes an arbitrary node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node: Node) -> None:
        """Inserts a node right before the tail (marks as most recently used)."""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
            return
        
        # Evict the least recently used item if at capacity
        if len(self.key_to_node) >= self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.key_to_node[lru_node.key]
        
        # Insert the new node
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        self._add_to_tail(new_node)