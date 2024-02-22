class Node1:

    def __init__(self, val: str):
        self.val = val
        self.children = {}

    def add_child(self, child):
        self.children[child.val] = child


class Node2:
    children = {}

    def __init__(self, val: str):
        self.val = val

    def add_child(self, child):
        self.children[child.val] = child


# class level attributes
n1 = Node2(1)
n2 = Node2(2)

n1.children['foo'] = 'bar'
n2.children['baz'] = 'pow'

# prints both children as children are shared
print('class level:')
for i in n1.children:
    print(i)

# instance level attributes
n1 = Node1(1)
n2 = Node1(2)

n1.children['foo'] = 'bar'
n2.children['baz'] = 'pow'

# prints only n1 children as children are not shared
print('instance level:')
for i in n1.children:
    print(i)
