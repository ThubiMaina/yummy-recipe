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
        self.assertEqual(1, output, "List successfully created")

    def test_if_category_name_is_empty(self):
        """defining method to test for adding a category with the name blank """
        output = self.category.create('', self.owner)
        self.assertEqual('blank', output, "name cannot be blank")

if __name__ =='main':
    unittest.main()    
    