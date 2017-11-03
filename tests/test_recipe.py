"""tests for recipe category class"""
import unittest
from recipescat import RecipeCat

class TestRecipeCat(unittest.TestCase):
    """
    Perform unit testing for the recipe category class
    """
    def setUp(self):
        """The setUp method before doing the tests"""
        self.category = RecipeCat()       
        self.category.Recipecats  = {}
        self.owner = "Erick"

    def test_for_creating_a_recipe_category(self):
        """ defining method to test for recipe categories """
        output = self.category.create('Breakfast', self.owner)
        self.assertEqual(True, output, "List successfully created")

    def test_if_category_name_is_empty(self):
        """defining method to test for adding a category with the name blank """
        output = self.category.create('', self.owner)
        self.assertEqual('blank category', output, "name cannot be blank")

    def test_if_description_empty(self):
        """defining method to test for adding a recipe with an empty name"""
        output = self.category.createrecipe('Breakfast', '' ,'tea')
        self.assertEqual('blank fields', output, "please fill the description")

    def test_if_recipe_in_category(self):
        """defining method to test for recipe in a category"""
        output = self.category.createrecipe('', 'method' ,'Breakfast')
        self.assertEqual('blank fields', output)

    def test_if_recipe_is_created(self):
        """defining method to test for adding a recipe """
        output = self.category.createrecipe('tea', 'method' ,'Breakfast')
        self.assertEqual(True, output)

if __name__ =='main':
    unittest.main()    
    