import json
import weibo

with open("my_weibo_app.json","r") as load_f:
	my_weibo_app = json.load(load_f)

APP_KEY = my_weibo_app["APP_KEY"]
MY_APP_SECRET = my_weibo_app["MY_APP_SECRET"]

REDIRECT = "#ip"

client = weibo.Client(APP_KEY,MY_APP_SECRET,REDIRECT)
authorize_url = client.authorize_url
print(authorize_url)
code = input("code>")
client.set_code(code)