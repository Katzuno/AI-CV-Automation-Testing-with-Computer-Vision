class Node:
   def __init__(self, head = None):
     self.head, self.left, self.right = head, None, None
   def __contains__(self, head):
     if head == self.head:
        return True
     return (False if self.left is None else head in self.left) or (False if self.right is None else head in self.right)
   def insert(self, head, vals):
     if self.head is None:
        self.head, self.left, self.right = head, Node(vals[0]), Node(vals[1])
     elif self.head == head:
        self.left, self.right = Node(vals[0]), Node(vals[1])
     else:
        getattr(self, 'left' if self.left and head in self.left else 'right').insert(head, vals)


def sExpression(nodes):
    # Write your code here
    # S-exp(node) = ( node->val (S-exp(node->first_child))(S-exp(node->second_child))),

    # where, first_child->val < second_child->val (first_child->val is lexicographically smaller than                   #second_child-> val)
    nodes = nodes.split(" ")

    # tata = poz 1, fiul = poz 3
    sExpression = ""

    tati = {}

    for node in nodes:
        parent = node[1]
        child = node[3]
        tati[parent] = child

    rad = ''
    for parent in tati.keys():
        radacina = 1
        for child in tati.items():
            if parent == child:
                radacina = 0
        if radacina == 1:
            rad = parent

    print(rad)
