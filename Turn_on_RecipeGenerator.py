from RecipesGenerator import RecipeGenerator
ing=str(ing)
ing=input('Please put your ingredients')
ing.lower()
while ing=='n':

    generator=RecipeGenerator()
    generator.working(ing)