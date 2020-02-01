my_family = {
    'A': ['B', 'C' , 'Z'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['L'],
    'G': ['J', 'K'],
    'Z': ['X', 'Y']
    }

def children(family, person):
    list_of_children=[]
    if person in family:
        list_of_children=family[person]
        for e in family[person]:
            for i in children(family,e):
                if i not in list_of_children:
            	    list_of_children+=children(family,e)
    else:
        list_of_children+=[]
    return list_of_children


def findparent(family,child):
    for key, value in family.items():
        if child in value:
            parent=key
            return parent


def grandparent(family, child):
    parent_found = False
    gparent_found = False
    for parent, children in family.items():
        if child in children:
            for p_parent, p_children in family.items():
                if parent in p_children:
                    print ("Grand parent is:", p_parent)
                    gparent_found = True
                    break
            if not gparent_found:
                print ("Sorry only parent is present:", parent)
                parent_found = True
                break
    if not parent_found and not gparent_found:
        print ("Sorry no grandparent or parent")


print ( "*** All children ***")
print(children(my_family, 'C'))
#print(children(my_family, 'D'))
print ( "*** Parent ***")
print(findparent(my_family, 'Y'))
#print(findparent(my_family, 'E'))
print ( "*** Grandparent ***")
print(grandparent(my_family, 'D'))
#print(grandparent(my_family, 'Z'))
