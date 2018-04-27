from tree import Node
from linear_data_structure.Queue import Queue
from io import StringIO
import math


def bst_example():
    # code a predefined BST

    return


def heap_example():
    # code a predefined heap
    return


def full_tree_example():
    # tree structure[1, 2, 3, 4, 5, 6, 7, 8, 9]

    node1 = Node(4, Node(8), Node(9))
    node2 = Node(2, node1, Node(5))
    node3 = Node(3,Node(6), Node(7))
    root = Node(1, node2, node3)

    return root


def breath_traversal_with_none(root):
    # enqueue the nodes in the tree level by level
    tree_height = get_tree_height(root)

    tree_breath_traversal = dict()
    q = Queue()
    q.enQueue(root)
    tree_level = 0
    nodes_at_current_level = []
    nodes_at_next_level = []

    while not q.isEmpty() and tree_level < tree_height:
        q_node = q.deQueue()
        nodes_at_current_level.append(q_node)
        if q_node:
            nodes_at_next_level += [q_node.left, q_node.right]
        else:
            nodes_at_next_level += [None, None]
        if q.isEmpty():
            tree_breath_traversal[tree_level] = nodes_at_current_level
            tree_level += 1
            q = Queue(nodes_at_next_level)
            nodes_at_current_level = []
            nodes_at_next_level = []

    return tree_breath_traversal


def print_tree_quick(root):
    d = breath_traversal_with_none(root)
    for k, v in d.items():
        level = [node.val if node else None for node in v]
        print("level " + str(k) + ": " + str(level))


def print_tree_pretty(root, file_path=None):
    # currently can't adjust to tree value with multiple digits. Single digit mode only
    tree_height = get_tree_height(root)
    pretty_output = StringIO()
    node_value_width = 3
    spaces = node_value_width * 2 * int(math.pow(2, tree_height-1))
    tree_nodes = breath_traversal_with_none(root)

    pretty_output.seek(0)

    for tree_level in range(tree_height):
        tree_nodes_by_level = [str(node.val) if node else "N" for node in tree_nodes[tree_level]]
        node_start_pos = spaces // 2
        temp = [' '] * (len(tree_nodes_by_level) * 2 -1)
        temp[0::2] = tree_nodes_by_level
        temp.insert(0, "")

        node_level_contents = (' '*(node_start_pos-1)).join(temp)
        pretty_output.write(node_level_contents + '\n')

        spaces //= 2
        next_spaces = spaces // 2
        horizontal_edge_by_level = (' '*next_spaces + '-'*(next_spaces-1)
                                    + ' ' + '-'*(next_spaces-1) + ' '*(next_spaces+1)) * (2 ** tree_level)
        pretty_output.write(horizontal_edge_by_level + '\n')
        if tree_level < tree_height - 1:
            skew_edge_by_level = (' '*(next_spaces-1) + '/' + ' '*(2*next_spaces-1) + '\\' + ' '*next_spaces) *(2 ** tree_level)
            pretty_output.write(skew_edge_by_level + '\n')
    contents = pretty_output.getvalue()

    if not file_path:
        print(contents)
    else:
        f = open(file_path, 'w', encoding='utf-8')
        f.write(contents)


def get_tree_height(root):
    if not root:
        return 0

    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

if __name__ == '__main__':
    root = full_tree_example()
    print(get_tree_height(root))
    print_tree_quick(root)
    print_tree_pretty(root)
    # print_tree_pretty(root, './tree.txt')
    from tree.traversal.postorder_traversal import postorder_traversal_recursive
    postorder_traversal_recursive(root)
