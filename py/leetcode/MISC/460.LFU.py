from collections import defaultdict


class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.value = val
        self.freq = 1
        self.prev = None
        self.next = None


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}

        def new_list():
            dummy = Node()
            dummy.next = dummy
            dummy.prev = dummy
            return dummy

        self.freq_to_dummy = defaultdict(new_list)

    def _get_node(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self._remove(node)
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:
            # empty
            del self.freq_to_dummy[node.freq]
            if self.min_freq == node.freq:
                self.min_freq += 1
        node.freq += 1
        # not the same
        self._push_front(self.freq_to_dummy[node.freq], node)
        return node

    def _remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def _push_front(self, dummy, x):
        x.prev = dummy
        x.next = dummy.next
        dummy.next.prev = x
        dummy.next = x

    def get(self, key):
        node = self._get_node(key)
        return node.value if node else -1

    def put(self, key, value):
        node = self._get_node(key)
        if node:
            node.value = value
            return
        if len(self.key_to_node) == self.capacity:
            dummy = self.freq_to_dummy[self.min_freq]
            back = dummy.prev
            del self.key_to_node[back.key]
            self._remove(back)
            if dummy.prev == dummy:
                del self.freq_to_dummy[self.min_freq]
        self.key_to_node[key] = node = Node(key, value)
        self._push_front(self.freq_to_dummy[1], node)
        self.min_freq = 1
