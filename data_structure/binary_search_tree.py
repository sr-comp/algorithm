class BSTNode:
    key = 0
    left =None
    right = None
    parent = None

    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    root = None

    def insert(self, key):
        z = BSTNode(key, None, None, None)
        if self.root == None:
            self.root = z
            return
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        if z.key < y.key:
            y.left = z
            z.parent = y
        else:
            y.right = z
            z.parent = y

    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)

    def search(self, x, key):
        if x == None:
            return x
        elif x.key == key:
            return x
        elif key < x.key:
            return self.search(x.left, key)
        else:
            return self.search(x.right, key)

    def transplant(self, u, v):
        if u == self.root:
            self.root = v
        x = u.parent
        if v != None:
            v.parent = x
        if u == x.left:
            x.left = v
        else:
            x.right = v

    def BSTMini(self, z):
        y = z
        while z != None:
            y = z
            z = z.left
        return y

    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.BSTMini(z.right)
            if y.parent == z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(5)
    t.insert(13)
    t.insert(4)
    t.insert(11)
    print('Search Result ' + str(t.search(t.root, 5).key))
    print('Minimum of Tree ' + str(t.BSTMini(t.root).key))
    t.inorder_tree_walk(t.root)
    t.delete(t.search(t.root, 4))
    print('-------------------')
    t.inorder_tree_walk(t.root)
