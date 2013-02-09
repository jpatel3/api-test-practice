from pprint import pprint
from fatsecret import FatSecretClient, FatSecretApplication
from fatsecret import FatSecretError
import sys

class FatSecretTestApplication(FatSecretApplication):
	key = 'ed1da5872e244f0b91cdc7b9e0aa732e'
	secret = 'ee9bebe76783478a86072307689f8c78'
                
client = FatSecretClient().connect().setApplication(FatSecretTestApplication)

print 'foods.search :'
pprint(client.foods.search(search_expression='BK Veggie Burger', max_results=1))

#print 'foods.food_id :'
#pprint(client.foods.search(food_id='104648'))

#print 'recipie.search :'
#pprint(client.recipes.search(search_expression='taco', max_results=1))

print 'recipie.id :'
pprint(client.recipe.get(recipe_id=245110))