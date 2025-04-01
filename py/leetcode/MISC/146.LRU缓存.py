class DLinkNode:
    def __init__(self, key=0, value=0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value


# 使用双链表
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.cap:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
