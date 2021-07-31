#!/usr/bin/env python
# coding: utf-8

# In[7]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler #sirve para la autenticacion
from tweepy.streaming import StreamListener
import json

###CREDENCIALES########################
ckey = "6JlbmR28K45NF143FujQsRYpx"
csecret = "C9nfUefWkj6itK2evwwsjUJ82ZruLRyEYottE4ENufnzcGIWVU"
atoken = "1416063692450541569-B0PlwCVFYvN5RRwfznjM1KFah3U2pj"
asecret = "fHaH2xOn1UWHaos75MhmkdBHdzZj6F6xHxA8yQLwekxpP"
#####################################


# In[6]:


"----------------------------------------PRIMER UBICACION----------------------------------------------"
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
    db = server.create('ciudad1')
except:
    db = server['ciudad1'] 
    
'''===============UBICACION QUITO=============='''    

twitterStream.filter(locations=[-78.545462,-0.243648,-78.4742,-0.169451])  


# In[ ]:




