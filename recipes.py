



class RecipeCat(object):
    Recipecats = {}
    """an empty list to store my recipe categories"""
    def __init__(self,  category = None, owner = None):
        """initializing class instance variables"""
        self.category = category
        self.owner = owner

    def create(self, category, owner):
        """defining method to create recipe category list"""
        if category != '':
            #call the get_myrecipe_lists function that contains individual recipe categories 
            my_recipecats = self.get_myrecipe_lists(owner)
            if my_recipecats != {}:
                #check's if user already has a category added
                if category not in my_recipecats.keys():
                    self.Recipecats[category] = {
                    'category':category,
                    'owner':owner,
                    }
                    return 1
                else:
                    return 2
            else:
                self.Recipecats[category] = {
                'category':category,
                    'owner':owner,
                }
                return 1
        else:
            return 3

    