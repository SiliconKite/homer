#!/usr/bin/env python
#import requests
import urllib
import base64
import requests
import json

oauth2URL = "https://api.idealista.com/oauth/token"
apiURL = "https://api.idealista.com/3.5/es/search"

apikey = r'wq0ynwj5wz01516vg760dwmn2abayjjy'
secret = r'LTfIKlBTlErl'

apikey_enc = urllib.quote_plus(apikey)
secret_enc = urllib.quote_plus(secret)
apisecret = apikey_enc + ':' + secret_enc 
auth = base64.b64encode(apisecret)

r = requests.post(oauth2URL, 
headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization' : 'Basic ' + auth},
data = {'grant_type':'client_credentials'})

print r.status_code
print r.text

# requests.post(oauth2URL, data={'grant_type' : 'authorization_code','code' : authorizationCode, 'client_id' : clientId, 'client_secret' : clientSecret})
#             # If the above gives a 4XX or 5XX error
#             getTokens.raise_for_status()
#             # Get the JSON from the above
#             newTokens = getTokens.json()
#             # Get the new access token, valid for 60 minutes
#             accessToken = newTokens['access_token']
#             # Log the access token we're using
#             logging.info('Generated Access Token: %s' % accessToken)
#             # Get the refresh token, valid for 60 days
#             refreshToken = newTokens['refresh_token']
#             # Log the new refresh token we've generated
#             logging.info('Generated Refresh Token: %s' % refreshToken)
#             # Update plist with new refresh token & time generated, refresh token used for subsequent runs
#             plistlib.writePlist({'Refresh Token':refreshToken,'Time Generated': datetime.now().isoformat(),}, plistFileFullPath)
#             # Update tokenPlist variable
#             tokenPlist = plistlib.readPlist(plistFileFullPath)
#         # If we cannot generate the tokens






# url = 'https://api.idealista.com/3.5/es/search'
# payload = {'format': 'json', 'key': 'site:dummy+type:example+group:wheel'}
# r = requests.get(url, params=payload)
# print(r.url)


# url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere'
# payload = json.load(open("request.json"))
# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# r = requests.post(url, data=json.dumps(payload), headers=headers)



def get_oauth_token():
  http_obj = Http()
  url = "https://api.idealista.com/oauth/token"
  apikey= urllib.parse.quote_plus('Provided_API_key')
  secret= urllib.parse.quote_plus('Provided_API_secret')
  auth = base64.encode(apikey + ':' + secret)
  body = {'grant_type':'client_credentials'}
  #headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + auth}
  headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization' : 'Basic ' + auth}
  resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
  return content

def search_api(token):
  http_obj = Http()
  url = "http://api.idealista.com/3.5/es/search?center=40.42938099999995,-3.7097526269835726&country=es&maxItems=50&numPage=1&distance=452&propertyType=bedrooms&operation=rent"
  headers = {'Authorization' : 'Bearer ' + token}
  resp, content = http_obj.request(url,method='POST',headers=headers)
  return content
