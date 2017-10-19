



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

    def edit(self, old, category, owner):
        """defining method to delete bucket list"""
        if category != '':
            del self.Recipecats[old]
            self.Recipecats[category] = {
            'category' : category,
            'owner' : owner,
            }
            return 1
        else:
            return 2

    def get_recipecat_lists(self):
        """defining method to get one recipe categories"""
        return self.Recipecats

    def get_myrecipe_lists(self, owner):
        """defining method to get one user's recipe category lists"""
        data = self.Recipecats
        my_recipecats = {}
        for category in data.keys():
            #loop through the categories in recipe and assign the dictionary to variables
            recipecat = data[category]
            recipeowner = recipecat['owner']
            if recipeowner == owner:
                my_recipecats[category] = {
                'category': category,
                'owner': owner,
                }
            else:
                result = my_recipecats
        return my_recipecats

    def get_recipecat_list(self, category):
        """defining method to get one recipe lists"""
        return self.Recipecats[category]    

    def delete(self, category):
        """defining method to delete a recipe category"""
        if category in self.Recipecats.keys():
            #checks if the category being deleted exists
            del self.Recipecats[category]
            return 1
        else:
            return 2

