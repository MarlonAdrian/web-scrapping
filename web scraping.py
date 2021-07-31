#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument


# In[38]:


db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[39]:


response = requests.get('https://resultados.elpais.com/deportivos/juegos-olimpicos/medallero/')
soup = BeautifulSoup(response.content, "lxml")

Oro=[]
Plata=[]
Bronce=[]


post_oro=soup.find_all("td", class_="m_oro")
post_plata= soup.find_all("td", class_="m_plata") 
post_bronce=soup.find_all("td", class_="m_bronce")


extracted = []

#para hacer busqueda
for element in post_oro: 
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Oro.append(limpio.strip())


for element in post_plata: 
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Plata.append(limpio.strip())

for element in post_bronce:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Bronce.append(limpio.strip())


# In[40]:


dbJuegos=pd.DataFrame({"Oro":Oro,"Plata":Plata,"Bronce":Bronce})


# In[41]:


dbJuegos.to_csv('NumeroMedallas.csv')
dbJuegos.to_csv('NumeroMedallas.json')


# In[44]:


from pymongo import MongoClient 
import pandas as pd
import json
import pandas as pd  #bien


# In[45]:


Client = MongoClient('mongodb://localhost:27017') #guardando el cliente en una variable llamada CLient


# In[46]:


df=pd.read_csv(r'C:\Users\USUARIO\NumeroMedallas.csv')


# In[47]:


data=df.to_dict(orient="records")
data 


# In[48]:


db=Client['numero_medallas']
db.Medallas.insert_many(data)


# In[ ]:





# In[58]:


import pymongo  
client = pymongo.MongoClient("mongodb+srv://Marlon:marlon@cluster0.xfmsa.mongodb.net/examenretryWrites=true&w=majority")  
  
collection = client.libraryDB.books  
booksData = [{
  "_id": {
    "$oid": "61048da612f36af9277071e0"
  },
  "Unnamed: 0": 0,
  "Oro": 19,
  "Plata": 10,
  "Bronce": 11
},{
  "_id": {
    "$oid": "61048da612f36af9277071e1"
  },
  "Unnamed: 0": 1,
  "Oro": 17,
  "Plata": 4,
  "Bronce": 7
},{
  "_id": {
    "$oid": "61048da612f36af9277071e2"
  },
  "Unnamed: 0": 2,
  "Oro": 14,
  "Plata": 16,
  "Bronce": 11
},{
  "_id": {
    "$oid": "61048da612f36af9277071e3"
  },
  "Unnamed: 0": 3,
  "Oro": 10,
  "Plata": 14,
  "Bronce": 10
},{
  "_id": {
    "$oid": "61048da612f36af9277071e4"
  },
  "Unnamed: 0": 4,
  "Oro": 9,
  "Plata": 2,
  "Bronce": 11
},{
  "_id": {
    "$oid": "61048da612f36af9277071e5"
  },
  "Unnamed: 0": 5,
  "Oro": 6,
  "Plata": 9,
  "Bronce": 9
},{
  "_id": {
    "$oid": "61048da612f36af9277071e6"
  },
  "Unnamed: 0": 6,
  "Oro": 5,
  "Plata": 4,
  "Bronce": 6
},{
  "_id": {
    "$oid": "61048da612f36af9277071e7"
  },
  "Unnamed: 0": 7,
  "Oro": 3,
  "Plata": 7,
  "Bronce": 5
},{
  "_id": {
    "$oid": "61048da612f36af9277071e8"
  },
  "Unnamed: 0": 8,
  "Oro": 3,
  "Plata": 5,
  "Bronce": 5
},{
  "_id": {
    "$oid": "61048da612f36af9277071e9"
  },
  "Unnamed: 0": 9,
  "Oro": 3,
  "Plata": 4,
  "Bronce": 9
},{
  "_id": {
    "$oid": "61048da612f36af9277071ea"
  },
  "Unnamed: 0": 10,
  "Oro": 3,
  "Plata": 3,
  "Bronce": 5
},{
  "_id": {
    "$oid": "61048da612f36af9277071eb"
  },
  "Unnamed: 0": 11,
  "Oro": 3,
  "Plata": 3,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af9277071ec"
  },
  "Unnamed: 0": 12,
  "Oro": 3,
  "Plata": 2,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af9277071ed"
  },
  "Unnamed: 0": 13,
  "Oro": 3,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af9277071ee"
  },
  "Unnamed: 0": 14,
  "Oro": 2,
  "Plata": 7,
  "Bronce": 11
},{
  "_id": {
    "$oid": "61048da612f36af9277071ef"
  },
  "Unnamed: 0": 15,
  "Oro": 2,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af9277071f0"
  },
  "Unnamed: 0": 16,
  "Oro": 2,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af9277071f1"
  },
  "Unnamed: 0": 17,
  "Oro": 2,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071f2"
  },
  "Unnamed: 0": 18,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af9277071f3"
  },
  "Unnamed: 0": 19,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af9277071f4"
  },
  "Unnamed: 0": 20,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071f5"
  },
  "Unnamed: 0": 21,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071f6"
  },
  "Unnamed: 0": 22,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af9277071f7"
  },
  "Unnamed: 0": 23,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071f8"
  },
  "Unnamed: 0": 24,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071f9"
  },
  "Unnamed: 0": 25,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af9277071fa"
  },
  "Unnamed: 0": 26,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af9277071fb"
  },
  "Unnamed: 0": 27,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071fc"
  },
  "Unnamed: 0": 28,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071fd"
  },
  "Unnamed: 0": 29,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af9277071fe"
  },
  "Unnamed: 0": 30,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af9277071ff"
  },
  "Unnamed: 0": 31,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707200"
  },
  "Unnamed: 0": 32,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707201"
  },
  "Unnamed: 0": 33,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707202"
  },
  "Unnamed: 0": 34,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707203"
  },
  "Unnamed: 0": 35,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707204"
  },
  "Unnamed: 0": 36,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707205"
  },
  "Unnamed: 0": 37,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707206"
  },
  "Unnamed: 0": 38,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707207"
  },
  "Unnamed: 0": 39,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707208"
  },
  "Unnamed: 0": 40,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707209"
  },
  "Unnamed: 0": 41,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770720a"
  },
  "Unnamed: 0": 42,
  "Oro": 0,
  "Plata": 2,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770720b"
  },
  "Unnamed: 0": 43,
  "Oro": 0,
  "Plata": 2,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770720c"
  },
  "Unnamed: 0": 44,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770720d"
  },
  "Unnamed: 0": 45,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770720e"
  },
  "Unnamed: 0": 46,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770720f"
  },
  "Unnamed: 0": 47,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707210"
  },
  "Unnamed: 0": 48,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707211"
  },
  "Unnamed: 0": 49,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707212"
  },
  "Unnamed: 0": 50,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707213"
  },
  "Unnamed: 0": 51,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707214"
  },
  "Unnamed: 0": 52,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707215"
  },
  "Unnamed: 0": 53,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707216"
  },
  "Unnamed: 0": 54,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707217"
  },
  "Unnamed: 0": 55,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707218"
  },
  "Unnamed: 0": 56,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707219"
  },
  "Unnamed: 0": 57,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af92770721a"
  },
  "Unnamed: 0": 58,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af92770721b"
  },
  "Unnamed: 0": 59,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770721c"
  },
  "Unnamed: 0": 60,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770721d"
  },
  "Unnamed: 0": 61,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770721e"
  },
  "Unnamed: 0": 62,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770721f"
  },
  "Unnamed: 0": 63,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707220"
  },
  "Unnamed: 0": 64,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707221"
  },
  "Unnamed: 0": 65,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707222"
  },
  "Unnamed: 0": 66,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707223"
  },
  "Unnamed: 0": 67,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707224"
  },
  "Unnamed: 0": 68,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707225"
  },
  "Unnamed: 0": 69,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707226"
  },
  "Unnamed: 0": 70,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707227"
  },
  "Unnamed: 0": 71,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707228"
  },
  "Unnamed: 0": 72,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707229"
  },
  "Unnamed: 0": 73,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722a"
  },
  "Unnamed: 0": 74,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722b"
  },
  "Unnamed: 0": 75,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722c"
  },
  "Unnamed: 0": 76,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722d"
  },
  "Unnamed: 0": 77,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722e"
  },
  "Unnamed: 0": 78,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770722f"
  },
  "Unnamed: 0": 79,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707230"
  },
  "Unnamed: 0": 80,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707231"
  },
  "Unnamed: 0": 81,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707232"
  },
  "Unnamed: 0": 82,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707233"
  },
  "Unnamed: 0": 83,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707234"
  },
  "Unnamed: 0": 84,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707235"
  },
  "Unnamed: 0": 85,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707236"
  },
  "Unnamed: 0": 86,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707237"
  },
  "Unnamed: 0": 87,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707238"
  },
  "Unnamed: 0": 88,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707239"
  },
  "Unnamed: 0": 89,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723a"
  },
  "Unnamed: 0": 90,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723b"
  },
  "Unnamed: 0": 91,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723c"
  },
  "Unnamed: 0": 92,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723d"
  },
  "Unnamed: 0": 93,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723e"
  },
  "Unnamed: 0": 94,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770723f"
  },
  "Unnamed: 0": 95,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707240"
  },
  "Unnamed: 0": 96,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707241"
  },
  "Unnamed: 0": 97,
  "Oro": 26,
  "Plata": 18,
  "Bronce": 26
},{
  "_id": {
    "$oid": "61048da612f36af927707242"
  },
  "Unnamed: 0": 98,
  "Oro": 12,
  "Plata": 8,
  "Bronce": 21
},{
  "_id": {
    "$oid": "61048da612f36af927707243"
  },
  "Unnamed: 0": 99,
  "Oro": 46,
  "Plata": 37,
  "Bronce": 38
},{
  "_id": {
    "$oid": "61048da612f36af927707244"
  },
  "Unnamed: 0": 100,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707245"
  },
  "Unnamed: 0": 101,
  "Oro": 8,
  "Plata": 11,
  "Bronce": 10
},{
  "_id": {
    "$oid": "61048da612f36af927707246"
  },
  "Unnamed: 0": 102,
  "Oro": 27,
  "Plata": 23,
  "Bronce": 17
},{
  "_id": {
    "$oid": "61048da612f36af927707247"
  },
  "Unnamed: 0": 103,
  "Oro": 9,
  "Plata": 3,
  "Bronce": 9
},{
  "_id": {
    "$oid": "61048da612f36af927707248"
  },
  "Unnamed: 0": 104,
  "Oro": 8,
  "Plata": 7,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af927707249"
  },
  "Unnamed: 0": 105,
  "Oro": 10,
  "Plata": 18,
  "Bronce": 14
},{
  "_id": {
    "$oid": "61048da612f36af92770724a"
  },
  "Unnamed: 0": 106,
  "Oro": 17,
  "Plata": 10,
  "Bronce": 15
},{
  "_id": {
    "$oid": "61048da612f36af92770724b"
  },
  "Unnamed: 0": 107,
  "Oro": 4,
  "Plata": 3,
  "Bronce": 15
},{
  "_id": {
    "$oid": "61048da612f36af92770724c"
  },
  "Unnamed: 0": 108,
  "Oro": 4,
  "Plata": 9,
  "Bronce": 5
},{
  "_id": {
    "$oid": "61048da612f36af92770724d"
  },
  "Unnamed: 0": 109,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 7
},{
  "_id": {
    "$oid": "61048da612f36af92770724e"
  },
  "Unnamed: 0": 110,
  "Oro": 5,
  "Plata": 3,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770724f"
  },
  "Unnamed: 0": 111,
  "Oro": 8,
  "Plata": 12,
  "Bronce": 8
},{
  "_id": {
    "$oid": "61048da612f36af927707250"
  },
  "Unnamed: 0": 112,
  "Oro": 8,
  "Plata": 3,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af927707251"
  },
  "Unnamed: 0": 113,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707252"
  },
  "Unnamed: 0": 114,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707253"
  },
  "Unnamed: 0": 115,
  "Oro": 3,
  "Plata": 2,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707254"
  },
  "Unnamed: 0": 116,
  "Oro": 7,
  "Plata": 6,
  "Bronce": 6
},{
  "_id": {
    "$oid": "61048da612f36af927707255"
  },
  "Unnamed: 0": 117,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af927707256"
  },
  "Unnamed: 0": 118,
  "Oro": 2,
  "Plata": 1,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af927707257"
  },
  "Unnamed: 0": 119,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707258"
  },
  "Unnamed: 0": 120,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707259"
  },
  "Unnamed: 0": 121,
  "Oro": 2,
  "Plata": 6,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770725a"
  },
  "Unnamed: 0": 122,
  "Oro": 2,
  "Plata": 4,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770725b"
  },
  "Unnamed: 0": 123,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770725c"
  },
  "Unnamed: 0": 124,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af92770725d"
  },
  "Unnamed: 0": 125,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af92770725e"
  },
  "Unnamed: 0": 126,
  "Oro": 2,
  "Plata": 2,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770725f"
  },
  "Unnamed: 0": 127,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707260"
  },
  "Unnamed: 0": 128,
  "Oro": 4,
  "Plata": 2,
  "Bronce": 7
},{
  "_id": {
    "$oid": "61048da612f36af927707261"
  },
  "Unnamed: 0": 129,
  "Oro": 0,
  "Plata": 2,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707262"
  },
  "Unnamed: 0": 130,
  "Oro": 3,
  "Plata": 1,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af927707263"
  },
  "Unnamed: 0": 131,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707264"
  },
  "Unnamed: 0": 132,
  "Oro": 2,
  "Plata": 2,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707265"
  },
  "Unnamed: 0": 133,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707266"
  },
  "Unnamed: 0": 134,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707267"
  },
  "Unnamed: 0": 135,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707268"
  },
  "Unnamed: 0": 136,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707269"
  },
  "Unnamed: 0": 137,
  "Oro": 3,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770726a"
  },
  "Unnamed: 0": 138,
  "Oro": 1,
  "Plata": 2,
  "Bronce": 5
},{
  "_id": {
    "$oid": "61048da612f36af92770726b"
  },
  "Unnamed: 0": 139,
  "Oro": 7,
  "Plata": 4,
  "Bronce": 6
},{
  "_id": {
    "$oid": "61048da612f36af92770726c"
  },
  "Unnamed: 0": 140,
  "Oro": 3,
  "Plata": 2,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af92770726d"
  },
  "Unnamed: 0": 141,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770726e"
  },
  "Unnamed: 0": 142,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770726f"
  },
  "Unnamed: 0": 143,
  "Oro": 2,
  "Plata": 2,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707270"
  },
  "Unnamed: 0": 144,
  "Oro": 2,
  "Plata": 6,
  "Bronce": 7
},{
  "_id": {
    "$oid": "61048da612f36af927707271"
  },
  "Unnamed: 0": 145,
  "Oro": 5,
  "Plata": 2,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af927707272"
  },
  "Unnamed: 0": 146,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707273"
  },
  "Unnamed: 0": 147,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707274"
  },
  "Unnamed: 0": 148,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707275"
  },
  "Unnamed: 0": 149,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707276"
  },
  "Unnamed: 0": 150,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707277"
  },
  "Unnamed: 0": 151,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707278"
  },
  "Unnamed: 0": 152,
  "Oro": 2,
  "Plata": 3,
  "Bronce": 6
},{
  "_id": {
    "$oid": "61048da612f36af927707279"
  },
  "Unnamed: 0": 153,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770727a"
  },
  "Unnamed: 0": 154,
  "Oro": 2,
  "Plata": 5,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af92770727b"
  },
  "Unnamed: 0": 155,
  "Oro": 3,
  "Plata": 5,
  "Bronce": 9
},{
  "_id": {
    "$oid": "61048da612f36af92770727c"
  },
  "Unnamed: 0": 156,
  "Oro": 0,
  "Plata": 3,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770727d"
  },
  "Unnamed: 0": 157,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af92770727e"
  },
  "Unnamed: 0": 158,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af92770727f"
  },
  "Unnamed: 0": 159,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af927707280"
  },
  "Unnamed: 0": 160,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707281"
  },
  "Unnamed: 0": 161,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707282"
  },
  "Unnamed: 0": 162,
  "Oro": 3,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707283"
  },
  "Unnamed: 0": 163,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707284"
  },
  "Unnamed: 0": 164,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707285"
  },
  "Unnamed: 0": 165,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707286"
  },
  "Unnamed: 0": 166,
  "Oro": 1,
  "Plata": 7,
  "Bronce": 10
},{
  "_id": {
    "$oid": "61048da612f36af927707287"
  },
  "Unnamed: 0": 167,
  "Oro": 19,
  "Plata": 18,
  "Bronce": 19
},{
  "_id": {
    "$oid": "61048da612f36af927707288"
  },
  "Unnamed: 0": 168,
  "Oro": 6,
  "Plata": 6,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707289"
  },
  "Unnamed: 0": 169,
  "Oro": 6,
  "Plata": 3,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770728a"
  },
  "Unnamed: 0": 170,
  "Oro": 2,
  "Plata": 6,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af92770728b"
  },
  "Unnamed: 0": 171,
  "Oro": 2,
  "Plata": 3,
  "Bronce": 2
},{
  "_id": {
    "$oid": "61048da612f36af92770728c"
  },
  "Unnamed: 0": 172,
  "Oro": 1,
  "Plata": 4,
  "Bronce": 4
},{
  "_id": {
    "$oid": "61048da612f36af92770728d"
  },
  "Unnamed: 0": 173,
  "Oro": 1,
  "Plata": 3,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770728e"
  },
  "Unnamed: 0": 174,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770728f"
  },
  "Unnamed: 0": 175,
  "Oro": 1,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707290"
  },
  "Unnamed: 0": 176,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707291"
  },
  "Unnamed: 0": 177,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707292"
  },
  "Unnamed: 0": 178,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707293"
  },
  "Unnamed: 0": 179,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707294"
  },
  "Unnamed: 0": 180,
  "Oro": 1,
  "Plata": 0,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707295"
  },
  "Unnamed: 0": 181,
  "Oro": 0,
  "Plata": 4,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af927707296"
  },
  "Unnamed: 0": 182,
  "Oro": 0,
  "Plata": 2,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707297"
  },
  "Unnamed: 0": 183,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 3
},{
  "_id": {
    "$oid": "61048da612f36af927707298"
  },
  "Unnamed: 0": 184,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af927707299"
  },
  "Unnamed: 0": 185,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770729a"
  },
  "Unnamed: 0": 186,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770729b"
  },
  "Unnamed: 0": 187,
  "Oro": 0,
  "Plata": 1,
  "Bronce": 0
},{
  "_id": {
    "$oid": "61048da612f36af92770729c"
  },
  "Unnamed: 0": 188,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770729d"
  },
  "Unnamed: 0": 189,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770729e"
  },
  "Unnamed: 0": 190,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af92770729f"
  },
  "Unnamed: 0": 191,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af9277072a0"
  },
  "Unnamed: 0": 192,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
},{
  "_id": {
    "$oid": "61048da612f36af9277072a1"
  },
  "Unnamed: 0": 193,
  "Oro": 0,
  "Plata": 0,
  "Bronce": 1
}
] 
  
collection.insert_many(booksData) 


# In[ ]:




