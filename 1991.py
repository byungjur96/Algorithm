import sys

tree = dict()

# 전위 순회
def preorder(tree, root, result=""):
    if root == '.':
        return ""
    return root + preorder(tree, tree[root][0]) + preorder(tree, tree[root][1])


# 중위 순회
def inorder(tree, root, result=""):
    if root == '.':
        return ""
    return inorder(tree, tree[root][0]) + root + inorder(tree, tree[root][1])

# 후위 순회
def postorder(tree, root, result=""):
    if root == '.':
        return ""
    return postorder(tree, tree[root][0]) + postorder(tree, tree[root][1]) + root

for _ in range(int(sys.stdin.readline())):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

print(preorder(tree, "A"))
print(inorder(tree, "A"))
print(postorder(tree, "A"))


