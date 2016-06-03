import tweepy
import requests
from StringIO import StringIO
from PIL import Image, ImageFont, ImageDraw

#twiteer access data
ckey = "app key"
csecret = "app key"
atoken = "app key"
asecret = "app key"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

response = requests.get("http://maps.googleapis.com/maps/api/streetview?size=640x480&location=40.4063246,-3.8306592&fov=90&heading=360&pitch=0&sensor=false")
img = Image.open(StringIO(response.content))
draw = ImageDraw.Draw(img)
draw.text((10,10), "Light Pollution:low",(255,255,255))
img.save("test_image.jpg")

api.update_with_media("test_image.jpg",status='Nueva farola identificada', lat=40.4063246, long=-3.830659)
