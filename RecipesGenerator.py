import requests
import json

# http://www.recipepuppy.com/api/




class RecipeGenerator():
    def __init__(self):
        self.__ingredient=None
        self.__response=None

    @property
    def ingredient(self):
        return self.__ingredient
    @ingredient.setter
    def ingredient(self,ingredient):

        if type(self.__ingredient)==int:
            raise ValueError("ingredient should only in str format")
        # self.__ingredient=ingredient
        self.__ingredient = ingredient.replace(' ', ",")


    def working(self, ingredient):
        self.__ingredient=ingredient

        self.__response = requests.get('http://www.recipepuppy.com/api/',
        params={'i': self.__ingredient, 'q': '', 'p': '1'})
        # print(response.status_code)

        recipes = self.__response.json()['results']


        for recipe in recipes:

            print("\n")
            print(recipe['title'])
            print(30 * '-')
            print(recipe['ingredients'])
generator=RecipeGenerator()
generator.working('onion,eggs,bacon')
