from node import Node
import unittest


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        # TODO 1
        """Method to delete the tree

        Args:
            None

        Returns:
            None
        """
        self.root = None

    def printTree(self):
        # TODO 1
        """Method to print the tree

        Args:
            None

        Returns:
            None
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        # TODO 1
        """Method to print the tree inorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO 2
        """Method to print the tree preorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        # TODO 2
        """Method to print the tree postorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')

class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Tree()

        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find(self):
        """
        Testing if finding nodes works properly
        """
        self.assertIsNone(self.tree._find(10, self.tree.root))

        found = self.tree._find(8, self.tree.root)
        self.assertIsNotNone(found)
        self.assertEqual(found.data, 8)
