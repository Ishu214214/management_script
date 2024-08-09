
""" 1st methode is this"""

from googleapiclient.discovery import build
import pprint

  # my key  i have 2 key 
my_api_key_1 ="AIzaSyDDPYf9NBXfOv4t_xkeTh1NHmEUt59kguw"
my_api_key = "AIzaSyAqMYCrMdzU3pjrkslNAKKzH6KO17xcM5M"                

my_cse_id = "84b7ff8dccbe2488c"                                          # my search engien id

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

query = "ishu214214.github.io"
results = google_search( query , my_api_key_1, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)





#   if they want to add in the website
"""
<script async src="https://cse.google.com/cse.js?cx=84b7ff8dccbe2488c">
</script>
<div class="gcse-search"></div>
"""



""" 2nd methode is this"""
"""  this is used for the  for used the webscrapping """
from googlesearch import search

queary = "ishu214214.github.io"
for i in search(queary , tld = "com" , num= 10 ,stop =10 ,pause = 2):
	print(i)
     

