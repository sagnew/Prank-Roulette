import oauth2
import urllib
import urllib2
import json

# Fill in these values
consumer_key = 'QBHd3TQsXpIJDQjN-powkQ'
consumer_secret = '7jEk4frCUDvGClW_Rr2LB-xfFO4'
token = 'Zhe8ohFB5Z4COhCXi3ZoJ5uYJkPlz8X5'
token_secret = 'V7Vc6IBSIoXsC02cGQo72ash_uM'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
url = 'http://api.yelp.com/v2/search?term=bars&location=sf&limit=4'

print 'URL: %s' % (url,)

oauth_request = oauth2.Request('GET', url, {})
oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
	'oauth_timestamp': oauth2.generate_timestamp(),
	'oauth_token': token,
	'oauth_consumer_key': consumer_key})

token = oauth2.Token(token, token_secret)

oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

signed_url = oauth_request.to_url()


try:
	conn = urllib2.urlopen(signed_url, None)
	try:
		response = json.loads(conn.read())
	finally:
		conn.close()
except urllib2.HTTPError, error:
	response = json.loads(error.read())


for business in response['businesses']:
	print business['phone']
