
import oauth2 as oauth
import time
import requests
from hashlib import sha1
import hmac

FATSECRET_CONSUMER_KEY = 'ed1da5872e244f0b91cdc7b9e0aa732e'
FATSECRET_SHARED_SECRET = 'ee9bebe76783478a86072307689f8c78'
FATSECRET_USER = 'hsparikh@tuvalabs.com'
FATSECRET_URL = 'http://platform.fatsecret.com/rest/server.api'

token = oauth.Token(key="tok-test-key", secret="tok-test-secret")

params = {
	'oauth_consumer_key':FATSECRET_CONSUMER_KEY,
	'oauth_signature_method':"HMAC-SHA1",
    'oauth_timestamp': str(int(time.time())),
    'oauth_nonce': oauth.generate_nonce(),
	'oauth_version': "1.0",
	'method':"foods.get_most_eaten",
	}

consumer = oauth.Consumer(key=FATSECRET_CONSUMER_KEY, secret=FATSECRET_SHARED_SECRET)

try:
	# Create our request. Change method, etc. accordingly.
	req = oauth.Request(method="GET", url=FATSECRET_URL, parameters=params)
	
	# Sign the request.
	signature_method = oauth.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, token)
	
	import pdb;pdb.set_trace()
	
	r = requests.get(req.to_url())
	
	print r.status_code
	print r.text

except:
	raise

'''
import oauth2 as oauth

FATSECRET_CONSUMER_KEY = 'ed1da5872e244f0b91cdc7b9e0aa732e'
FATSECRET_SHARED_SECRET = 'ee9bebe76783478a86072307689f8c78'
FATSECRET_USER = 'hsparikh@tuvalabs.com'
FATSECRET_URL = 'http://platform.fatsecret.com/rest/server.api'

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=FATSECRET_CONSUMER_KEY, 
    secret=FATSECRET_SHARED_SECRET)

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(FATSECRET_URL, "GET")
print resp
print content

'''