class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and value < node.left.value:
            self._right_rotate(node)
        if balance < -1 and value > node.right.value:
            self._left_rotate(node)
        if balance > 1 and value > node.left.value:
            self._left_rotate(node.left)
            self._right_rotate(node)
        if balance < -1 and value < node.right.value:
            self._right_rotate(node.right)
            self._left_rotate(node)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.value, end=" ")
            self._inorder_traversal(node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.value, end=" ")

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node.value = self._min_value(node.right)
            node.right = self._delete(node.value, node.right)
        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value
