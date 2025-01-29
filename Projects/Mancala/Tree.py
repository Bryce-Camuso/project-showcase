
class NAryTree:

    def __init__(self, numberOfChildren, element = None, parent = None, children = None):
        self._children = [None] * numberOfChildren
        self._element = element
        self._parent = parent
        if children is not None:
            self._children = children
        
    def get_element(self):
        return self._element
    
    def get_parent(self):
        return self._parent
    
    def get_child(self, index):
        return self._children[index]
    
    def get_children(self):
        returnValue = self._children.copy()
        return returnValue
    
    def set_element(self, newElement):
        self._element = newElement

    def set_parent(self, newParent):
        self._parent = newParent

    def set_children(self, newChild, index = None):
        '''if an index is not specified and the array is full the new Child will not be written in'''
        if index is not None:
            self._children[index] = newChild

        else:
            for i in self._children:
                if i is None:
                    self._children = newChild


