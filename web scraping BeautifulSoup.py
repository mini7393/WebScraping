#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Example1


# In[1]:


import urllib.request


# In[27]:


from bs4 import BeautifulSoup


# In[3]:


pip install bs4


# In[4]:


url = 'https://finance.yahoo.com/quote/FB?p=FB'


# In[5]:


headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}


# In[7]:


req=urllib.request.Request(url,headers=headers)


# In[9]:


res=urllib.request.urlopen(req)


# In[10]:


html=res.read()


# In[11]:


soup=BeautifulSoup(html,'html.parser')


# In[15]:


tagged_values=soup.find_all("td",{'class':'Ta(end) Fw(600) Lh(14px)'})
print(tagged_values)


# In[16]:


values=[x.get_text() for x in tagged_values]
print(values)


# In[17]:


for value in values:
    print(value)


# For different URL's of same page "Facebook, Apple and Google"

# In[19]:


symbols=['FB','GOOG','AAPL']


# In[21]:


for symbol in symbols:
    url='https://finance.yahoo.com/quote/'+symbol+'?p='+symbol
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req)
    html=res.read()
    soup=BeautifulSoup(html,'html.parser')
    tagged_values=soup.find_all("td",{'class':'Ta(end) Fw(600) Lh(14px)'})
    #print(tagged_values)
    values=[x.get_text() for x in tagged_values]
    print(values)


# In[ ]:





# In[ ]:


#Example 2


# In[22]:


import bs4


# In[23]:


from urllib.request import urlopen as uReq


# In[24]:


my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic+cards'


# In[29]:


#opening connection and grabbing the page
uClient=uReq(my_url)
page_html=uClient.read()
#html parsing
page_soup=BeautifulSoup(page_html,'html.parser')


# In[30]:


page_soup.h1


# In[31]:


page_soup.p


# In[33]:


page_soup.body.span


# In[35]:


#grabs each product
containers=page_soup.findAll("div",{"class":"item-cell"})


# In[36]:


len(containers)


# In[64]:


contain=containers[0]


# In[67]:


brand= contain.div.div.div.a.img["alt"]
print(brand)
title=contain.findAll("a",{"class":"item-title"})
print(title)


# In[68]:


product_name=title[0].text


# In[69]:


product_name


# In[71]:


shipping=contain.findAll("li",{'class':'price-ship'})


# In[72]:


shipping[0].text


# In[77]:


filename="products.csv"
f= open(filename,"w")
headers="brand,product,shipping \n"
f.write(headers)
for contain in containers:
    #brand name
    brand= contain.div.div.div.a.img["alt"]#can be img["title"] too
    title=contain.findAll("a",{"class":"item-title"})
    product_name=title[0].text
    shipping=contain.findAll("li",{'class':'price-ship'})
    ship=shipping[0].text
    print("brand: "+brand)
    print("product: "+product_name)
    print("shipping: "+ship)
    f.write(brand + ","+ product_name.replace(",","|")+","+ ship + "\n")
f.close()


# In[ ]:




