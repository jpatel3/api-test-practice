from pprint import pprint
from fatsecret import FatSecretClient, FatSecretApplication
from fatsecret import FatSecretError
import sys

class FatSecretTestApplication(FatSecretApplication):
	key = 'your_key'
	secret = 'your_shared_secret_key'
                
client = FatSecretClient().connect().setApplication(FatSecretTestApplication)

print 'foods.search :'
pprint(client.foods.search(search_expression='BK Veggie Burger', max_results=1))

#print 'foods.food_id :'
#pprint(client.foods.search(food_id='104648'))

#print 'recipie.search :'
#pprint(client.recipes.search(search_expression='taco', max_results=1))

print 'recipie.id :'
pprint(client.recipe.get(recipe_id=245110))
