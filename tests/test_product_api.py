import requests

def test_api_list_of_products():
    r = requests.get('http://127.0.0.1:8000/products')
    response = r.json() 
    print(response)

test_api_list_of_products()