class tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        space = ' ' * self.get_level() * 2
        print(space+self.data)

        for child in self.children:
            child.print_tree()


root = tree("Electronics")

laptop = tree("laptop")
root.add_child(laptop)
lenovo = tree("lenovo")
laptop.add_child(lenovo)
ideapad_130 = tree("ideapad_130")
lenovo.add_child(ideapad_130)
mac = tree("mac")
laptop.add_child(mac)

tv = tree("tv")
root.add_child(tv)

mobile = tree("mobile")
root.add_child(mobile)

root.print_tree()
