from tree.utils.predefined_trees import full_tree_example


def inorder_traversal_recursive(root):
    ret = []

    def inorder(root):
        nonlocal ret
        if root:
            inorder(root.left)
            print(str(root.val) + ' ', end='')
            ret.append(root)
            inorder(root.right)

    inorder(root)
    return ret


def inorder_traversal_iterative(root):
    stack = []
    ret = []

    while len(stack) > 0 or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        ret.append(root)
        print(str(root.val) + ' ', end='')
        root = root.right

    return ret

if __name__ == "__main__":
    tree = full_tree_example()
    inorder_traversal_recursive(tree)
    print('\n')
    inorder_traversal_iterative(tree)
