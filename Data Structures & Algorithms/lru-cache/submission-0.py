class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        # Dummy nodes: head <-> MRU <-> ... <-> LRU <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Disconnects an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node) -> None:
        """Inserts a node right after the dummy head (MRU position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        # Move accessed node to MRU position
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
            return

        # Evict LRU node if at capacity
        if len(self.node_map) == self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.node_map[lru_node.key]

        new_node = Node(key, value)
        self.node_map[key] = new_node
        self._add_to_head(new_node)