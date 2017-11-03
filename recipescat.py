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
                #check's if user already has a category added
            if category not in Recipecats.keys():
                Recipecats[category] = {
                'category':category,
                'owner':owner,
                'recipe':[]
                }
                return True
            return "This category exists"
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
        if recipe != '' and description !='':
            for dic in Recipecats:
                if recipe not in Recipecats[dic]['recipe']:
                    Recipecats[category]['recipe'].append({
                        'recipe': recipe,
                        'description': description,
                        'category':category})
                    return True
                return 'exists'    
        return "blank fields"    
 
    def getrecipes(self, category):
        """ defining method  from category"""
        return Recipecats[category]['recipe']

    def deleterecipe(self, recipe, category):
        """ defining method to delete an recipe from category"""
        if recipe != '' and description !='':
            for dic in Recipecats:                
                for recipes in Recipecats[dic]['recipe']:
                    if recipes['recipe'] == recipe:
                        Recipecats[dic]['recipe'].remove(recipes)
                    return 'does not exist'
                return 'item already exists'        

        return 'blank fields'

    def editrecipe(self, recipe,newrecipe,
                description,newdescription,owner):
        """ defining method to edit a recipe"""
        if recipe != '' and description !='':
            for dic in Recipecats:
                for recipes in Recipecats[dic]['recipe']:
                    if recipes['recipe'] == recipe:
                        del recipes['recipe']
                        recipes['recipe'] = newrecipe
                        return True
        return redirect('/login')
