#!/usr/bin/env python
# coding: utf-8

# In[2]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler #sirve para la autenticacion
from tweepy.streaming import StreamListener
import json

###CREDENCIALES########################
ckey = "-------------"
csecret = "-------------"
atoken = "-------------"
asecret = "-------------"
#####################################


# In[ ]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)   #toman los valores de las keys
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Admin:DjMvYixzWDgk8m8@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('track')
except:
    db = server['track'] 
    
'''===============LOCATIONS=============='''    
twitterStream.filter(track=['tokio','juegos olimpicos'])


# In[ ]:




