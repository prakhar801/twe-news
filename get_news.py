import json
import urllib.parse
import urllib.request
import ssl

def lookup(topic):
    """Looks up articles by topic."""
    #ctx=ssl.create_default_context()
    #ctx.check_hostname = False
    #ctx.verify_mode = ssl.CERT_NONE

    feed = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=in&category={}&apiKey=be54272d4e6a44999625361ad1a5e8d1".format(urllib.parse.quote(topic, safe="")))
    feed=feed.read()
    feed=feed.decode()
    feed=json.loads(feed)
    dat = feed['articles']#dat is a list of dictionaries
    data=list()#data will be a list of dictionaries
    for item in dat:#item is a dict containing a newsapi
        app_data=dict()
        app_data['title']=item['title']
        app_data['description']=item['description']
        app_data['url']=item['url']
        data.append(app_data)
    return data#returns list of news each is a dictionary with keys
    #'title','description','url' and values string
