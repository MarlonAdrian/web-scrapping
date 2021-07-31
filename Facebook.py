#!/usr/bin/env python
# coding: utf-8

# In[6]:


from facebook_scraper import get_posts
import couchdb
import json
import time


# In[8]:


couch=couchdb.Server('http://Admin:DjMvYixzWDgk8m8@127.0.0.1:5984')
#db=couch.create('olympics')
nombredb='olympics'
db=couch[nombredb]


# In[ ]:


i=1
for post in get_posts('olympics', pages=10, extra_info=True):
    print(i)
    i=i+1
    time.sleep(1)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado" )

    except Exception as e:    
        print("no se grabó:" + str(e))


# In[ ]:




