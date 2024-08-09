
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient , ASCENDING, DESCENDING 
import time
from datetime import datetime
import multiprocessing


                 # database connection
#CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
client = MongoClient(CONNECTION_STRING)
mydatabase = client['web_scrapping_using_multiprocessing'] 
mycollection=mydatabase['Scraping_Product']

keyword_name = [ 'mobile']



def insert_into_db(result_price_list ,produck_link_final , result_img , result_name ,status_dict ):


    results_list =[]
    for i in range(0,len(result_price_list)):


        status_dict= { 
                        'product_title':result_name[i], 'product_image' :result_img[i] , 'price':result_price_list[i] ,'keyword':"mobile",'amazone_sku':produck_link_final[i]
                            ,'is_scrap': 0 ,  'current_time':round(time.time()) , 'current_date': datetime.now()
                            }
        results_list.append(status_dict)
    
    # print("insert start")
    # print(results_list[6])
    #mycollection.insert_many(results_list)


def keyword_page_scrape(result_price_list, produck_link_final ,result_img , result_name):
    

    final_link= "https://www.amazon.in/s?k=" + keyword_name[0]

    driver = webdriver.Firefox()
    driver.get(final_link)
    time.sleep(2)  

    soup= BeautifulSoup(driver.page_source ,'html.parser')
   
    print("featch image link and title of the product ")
    product_page_1= soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
    product_page_1_1 =product_page_1.find_all('img', class_='s-image')

  
    for i in range(0,len(product_page_1_1) -2):

        img_all_list= product_page_1_1[i]

        if img_all_list :

            if img_all_list.attrs['src'] != "https://m.media-amazon.com/images/I/81L6069AwHL._AC_UL640_QL65_.jpg":

                result_img.append(img_all_list.attrs['src'])
                name_valadition= (img_all_list.attrs['alt']).replace('Sponsored Ad -', '')
                
                result_name.append(name_valadition)

    # print(result_img)
    # print()
    # print(result_name)
    # print()
    # print(len(result_img))
    # print()
    # print(len(result_name))

    # sku
    
    product_sku= soup.find_all('div', class_='sg-col-20-of-24')
    # print(len(product_sku))

    for k in range(1,len(product_sku)-3):
        produck_link= product_sku[k]
        valide_sku =produck_link.attrs['data-asin']
        if valide_sku:
            produck_link_final.append( valide_sku )


    # print(produck_link_final)
    # print(len(produck_link_final))

    # price
       

    try:
        print("scrape the price")
        product_page_price= soup.find_all('div', class_='puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right')  
        #print(len(product_page_price))

        for i in range(0 ,len(product_page_price)):
            product_page_price_1 =product_page_price[i]
            product_price  =product_page_price_1.find('span', class_='a-price-whole')
            product_price_1 = product_price.get_text()
            product_price_1 = product_price_1.strip()
            product_price_1= (product_price_1.replace(',', ''))
            product_price_1= (product_price_1.replace(' ', ''))
            product_price_1= (product_price_1.replace('\n', ''))
            product_price_final= float(product_price_1)
            #print(product_price_final)
            result_price_list.append(product_price_final)

    except:
        pass

    #print(result_price_list)

    driver.quit()
    #print("end")



if __name__ == '__main__':

    manager = multiprocessing.Manager()
    status_dict = manager.dict()    
    #status_list = manager.list()  
    result_price_list= manager.list() 
    produck_link_final = manager.list()      
    result_img = manager.list()    
    result_name= manager.list()  

    print("scrap the detail page")

    for i in range(0,len(keyword_name)):
        m1 = multiprocessing.Process( target=keyword_page_scrape, args=(result_price_list ,produck_link_final , result_img , result_name))
        m1.start()
        m1.join()         

    # print(result_price_list)
    # print(produck_link_final)
    # print(result_img)
    # print(result_name)

    print("insert into db")

    for i in range(0,len(keyword_name)):
        m2 = multiprocessing.Process( target=insert_into_db, args=(result_price_list ,produck_link_final , result_img , result_name ,status_dict ))
        m2.start()
        m2.join()         

    print("task complet")
