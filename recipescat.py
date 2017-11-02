Recipecats = {}
class RecipeCat(object):
    
   
    """an empty dictionary to store my recipe categories"""
    def __init__(self, category=None, owner=None):
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
                    Recipecats[category] = {
                    'category':category,
                    'owner':owner,
                    'recipe':[]
                    }
                    return True
                else:
                    return "This category exists"
            else:
                Recipecats[category] = {
                    'category':category,
                    'owner':owner,
                    'recipe':[]
                    
                }
                return True
        else:
            return "blank category"

    def get_recipecat_lists(self):
        """defining method to get one recipe categories"""
        return Recipecats

    def get_myrecipe_lists(self, owner):
        """defining method to get one user's recipe category lists"""
        data = Recipecats
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
        return Recipecats[category]    

    def delete(self, category):
        """defining method to delete a recipe category"""
        if category in Recipecats.keys():
            #checks if the category being deleted exists
            del Recipecats[category]
            return True
        else:
            return 'does not exist'

    def edit(self, old, category, owner):
        """defining method to edit a  recipe category"""
        
        if category != '':
            del Recipecats[old]
            Recipecats[category] = {
            'category' : category,
            'owner' : owner,
            }
            return True
        else:
            return "blank"

    def createrecipe(self, recipe, description, category):
        """defining method to create an recipe in a category"""
        if recipe != '' or description !='':
            Recipecats[category]['recipe'].append({
                'recipe': recipe,
                'description': description,
                'category':category})
            return True
        return "blank fields"    
 
    def getrecipes(self, category):
        """ defining method  from category"""
        return Recipecats[category]['recipe']

    def deleterecipe(self, recipe, category):
        """ defining method to delete an recipe from category"""
        print("I am in deleterecipe",Recipecats )
        for dic in Recipecats:
            print( " after ",Recipecats[dic])
            print( "recipes", Recipecats[dic]['recipe'])

            for recipes in Recipecats[dic]['recipe']:
                if recipes['recipe'] == recipe:
                    print('dsfhjbfs')
                    Recipecats[dic]['recipe'].remove(recipes)
                    print('dsfhjbfs2', Recipecats[dic]['recipe'])

                return 'does not exist'
                # recipes.pop(recipes['recipe'])
            print('success')
                
                # 

            # # 
            # #     del Recipecats[category]['recipe']
            # #     result = True
            # #     # print('cool cool')
            # else:
            #     result = "does not exist"

        # return result 
