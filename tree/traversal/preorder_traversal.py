from tree.utils.predefined_trees import full_tree_example

def preorder_traversal_recursive(root):
    ret = []

    def pre_order(root):
        nonlocal ret

        if root:
            ret.append(root)
            print(str(root.val) + ' ', end=' ')
            pre_order(root.left)
            pre_order(root.right)

    pre_order(root)
    return ret

def preorder_traversal_iterative(root):
    ret = []
    stack = []

    # easy conversion from recursion to iteration since there is no specific operation
    # after the self-calling recursive functions
    if root:
        stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        ret.append(root)
        print(str(root.val) + ' ', end=' ')

        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return ret

if __name__ == "__main__":
    tree = full_tree_example()
    preorder_traversal_recursive(tree)
    print('\n')
    preorder_traversal_iterative(tree)