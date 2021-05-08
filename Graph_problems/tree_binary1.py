class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_item(self, val):
        if val < self.data:
            if self.left == None:
                self.left = binary_tree(val)
            self.left.add_item(val)
        elif val > self.data:
            if self.right == None:
                self.right = binary_tree(val)
            self.right.add_item(val)

    def in_order_travesal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_travesal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_travesal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left == None:
                return None
            else:
                return self.left.search(val)
        else:
            if self.right == None:
                return None
            else:
                return self.left.search(val)

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def delete(self, val):
        if self.data == val:
            if self.left is None and self.right == None:
                return None
            elif self.left is None:
                self = self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min()
            self.right = self.right.delete(min_val)
        elif val < self.data:
            self.left = self.left.delete(val)
        else:
            self.right = self.right.delete(val)

        return self


root = binary_tree(15)
root.add_item(12)
root.add_item(14)
root.add_item(7)
root.add_item(20)
root.add_item(23)

print(root.in_order_travesal())
print(root.search(12))
print(root.delete(7))
print(root.in_order_travesal())
