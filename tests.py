"""Tests for linked list."""

import linked_list

import unittest


class TestNode(unittest.TestCase):
    """Test node class."""

    def test_node(self):
        """Test Node creation."""
        node = linked_list.Node("A")
        self.assertEqual(node.data, "A")


if __name__ == "__main__":
    unittest.main()
