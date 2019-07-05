"""Linked List Implementation."""


class Node(object):
    """Node Class."""

    def __init__(self, data=None):
        """Initialize Node."""
        self.data = data
        self.next = None
