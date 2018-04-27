class Node():
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.val = value

    def __init__(self, value, l_node=None, r_node=None):
        self.left = l_node
        self.right = r_node
        self.val = value

    def __str__(self):
        left_str = "not exists"
        if self.left:
            left_str = "value " + str(self.left.val)

        right_str = "not exists"
        if self.right:
            right_str = "value " + str(self.right.val)

        return "node: value " + str(self.val) + ", left node: " + left_str + ", right node: " + right_str


