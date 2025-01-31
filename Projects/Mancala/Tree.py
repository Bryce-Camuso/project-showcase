
class NAryTree:

    def __init__(self, numberOfChildren, element = None, parent = None, children = None):
        '''
        This class expects the number of children with the option to add an element, parent node, and children array.

        parent expects another NAryTree object
        children expects an array of NAryTree objects or None
        '''
        self._children = [None] * numberOfChildren
        self._element = element
        self._parent = parent
        if children is not None:
            self._children = children
        
    def get_element(self):
        '''
        Gives the objects element
        '''
        return self._element
    
    def get_parent(self):
        '''
        Gives the objects parent object
        '''
        return self._parent
    
    def get_child(self, index):
        '''
        Gives a the child object at the array index
        '''
        return self._children[index]
    
    def get_children(self):
        '''
        makes a copy of the Children array and returns it
        '''
        returnValue = self._children.copy()
        return returnValue
    
    def set_element(self, newElement):
        '''
        sets the element of the object
        '''
        self._element = newElement

    def set_parent(self, newParent):
        '''
        sets the parent node
        method expects an NArytree object
        '''
        self._parent = newParent

    def set_children(self, newChild, index = None):
        '''
        sets an index in the child array

        method takes an index

        if an index is not specified it will find the first availble index
        
        if the array is full the new Child will not be written in
        '''
        if index is not None:
            self._children[index] = newChild

        else:
            for i in self._children:
                if i is None:
                    self._children = newChild


