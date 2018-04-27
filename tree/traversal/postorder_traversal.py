from tree.utils.predefined_trees import full_tree_example


def postorder_traversal_recursive(root):
    ret = []

    def post_order(root):
        nonlocal ret
        if root:
            post_order(root.left)
            post_order(root.right)
            ret.append(root)
            print(str(root.val) + ' ', end=' ')

    post_order(root)
    return ret

def postorder_traversal_iterative(root):
    ret = []


if __name__ == "__main__":
    tree = full_tree_example()
    postorder_traversal_recursive(tree)

