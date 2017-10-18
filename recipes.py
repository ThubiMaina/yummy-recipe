



class RecipeCat(object):
    Recipecats = {}
    """an empty list to store my recipe categories"""
    def __init__(self,  category = None, owner = None):
        """initializing class instance variables"""
        self.category = category
        self.owner = owner

    