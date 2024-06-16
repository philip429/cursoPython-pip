import requests
import pprint

def GetCategories():
    req = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(req)
    print(req.status_code)
    categories = req.json()
    pprint.pprint(categories)
    print('\n')
    
    for category in categories: print(category['name'])    
    