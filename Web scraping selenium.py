#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[1]:


from selenium import webdriver


# In[3]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
option=webdriver.ChromeOptions()
option.add_argument("--incognito")


# In[44]:


browser = webdriver.Chrome(executable_path='C:/Users/sivay/Desktop/chromedriver',options=option)


# In[45]:


browser.get('https://finance.yahoo.com/quote/FB?p=FB')


# In[27]:


browser = webdriver.Chrome(executable_path='C:/Users/sivay/Desktop/chromedriver',options=option)
browser.get('https://finance.yahoo.com/quote/FB?p=FB')
timeout=30
try:
    WebDriverWait(browser,timeout).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='Va(m) C($primaryColor) Wow(bw) Us(n)']")))
except TimeoutException:
    print("Time out waiting to load the page")
    browser.quit()


# In[49]:


titles_element=browser.find_elements_by_xpath("//td[@class='C($primaryColor) W(51%)']")
titles=[x.text for x in titles_element]
print(titles)


# In[41]:


titles_element_value=browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(600) Lh(14px)']")
title_values=[x.text for x in titles_element_value]
print(title_values)


# In[42]:


for title, value in zip(titles,title_values):
    print(title+ ":"+ value)


# In[ ]:





# In[ ]:


#Example 2


# In[50]:


#new code
https://www.youtube.com/watch?v=wCoTJdhRcQE


# In[17]:


import selenium
from selenium import webdriver
webD=webdriver.Chrome('C:/Users/sivay/Desktop/chromedriver')
webD.get('https://www.webscraper.io/test-sites/e-commerce/static')


# In[18]:


clickobj=webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')


# In[19]:


clickobj.click()


# In[20]:


webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()


# In[21]:


li=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div')


# In[109]:


productInfo=webD.find_elements_by_class_name("thumbnail")


# In[111]:



list1=[]
for product in productInfo:
    ppp1=product.find_elements_by_tag_name('h4')[1]
    ppp2=ppp1.find_element_by_tag_name('a')
    
    list1.append(ppp2.get_property('href'))
    
    


# In[112]:


list1


# In[23]:


list1=[]
condition=True
while condition:
    productInfo=webD.find_elements_by_class_name("thumbnail")
    for product in productInfo:
        ppp1=product.find_elements_by_tag_name('h4')[-1]
        ppp2=ppp1.find_element_by_tag_name('a')
        list1.append(ppp2.get_property('href'))
        if (ppp2.get_property('href')=='https://www.webscraper.io/test-sites/e-commerce/static/product/632'):
                condition=False
    try:
         webD.find_elements_by_class_name('page-link')[-1].click()
            
            
            
    except:
        
        condition=False
  


# In[24]:


list1


# In[25]:


len(list1)


# In[ ]:




