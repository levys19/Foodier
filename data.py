import requests
from food_rekognition import FoodRekognition
import pprint

class DataFilter:
    @classmethod
    def getLocation(cls, zipcode, price):
        params = dict()
        params["term"] = "restaurant"
        params["location"] = zipcode
        params["open_now"] = True
        params["price"] = price
        params["limit"] = 10
        return params

# method returns a dictionary of keys: restaurant ids and values: photo urls
    @classmethod
    def get_results(cls,params):
        consumer_key = "a5QvhItx614Et3Zy6H5qHQ"
        consumer_secret = "sTAAmFINqdlrKhlNfJbBa3FzfTjbI5WvBh1s643EY5zj7dgnx0m7BKXSNZdjV4RF"
        data = {'grant_type': 'client_credentials', 'client_id': consumer_key, 'client_secret': consumer_secret}
        token = requests.post('https://api.yelp.com/oauth2/token', data=data)
        access_token = token.json()['access_token']
        url = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization': 'bearer %s' % access_token}
        resp = requests.get(url=url, params=params, headers=headers)
        restaurants = resp.json()
        business = restaurants["businesses"]
        rest_photo = dict()
        for ids in business:
            url2 = 'https://api.yelp.com/v3/businesses/' + ids["id"]
            resp2 = requests.get(url=url2, headers=headers)
            rest_info = resp2.json()
            name = rest_info["id"]
            rest_photo[name] = rest_info["photos"] #mapping photo urls to their restaurant ids
        # print("------")
        # print("BEFORE:")
        # pprint.pprint(rest_photo)
        # print("------")

        rekognizer = FoodRekognition
        for photos in rest_photo.values():
            for indiv in photos:
                if not rekognizer.is_food(indiv):
                    photos.remove(indiv)
        # print("------")
        # print("AFTER:")
        # pprint.pprint(rest_photo)
        # print("------")
        return rest_photo

    @classmethod
    def getLink(cls, ID):
        print(ID)
        consumer_key = "a5QvhItx614Et3Zy6H5qHQ"
        consumer_secret = "sTAAmFINqdlrKhlNfJbBa3FzfTjbI5WvBh1s643EY5zj7dgnx0m7BKXSNZdjV4RF"
        data = {'grant_type': 'client_credentials', 'client_id': consumer_key, 'client_secret': consumer_secret}
        token = requests.post('https://api.yelp.com/oauth2/token', data=data)
        access_token = token.json()['access_token']
        url = 'https://api.yelp.com/v3/businesses/' + ID
        headers = {'Authorization': 'bearer %s' % access_token}
        resp = requests.get(url=url, params=ID, headers=headers)
        restaurants = resp.json()
        business = restaurants["url"]
        return business
    @classmethod
    def getName(cls, ID):
        consumer_key = "a5QvhItx614Et3Zy6H5qHQ"
        consumer_secret = "sTAAmFINqdlrKhlNfJbBa3FzfTjbI5WvBh1s643EY5zj7dgnx0m7BKXSNZdjV4RF"
        data = {'grant_type': 'client_credentials', 'client_id': consumer_key, 'client_secret': consumer_secret}
        token = requests.post('https://api.yelp.com/oauth2/token', data=data)
        access_token = token.json()['access_token']
        url = 'https://api.yelp.com/v3/businesses/' + ID
        headers = {'Authorization': 'bearer %s' % access_token}
        resp = requests.get(url=url, params=ID, headers=headers)
        restaurants = resp.json()
        business = restaurants["name"]
        return business

# R = DataFilter.get_results(DataFilter.getLocation("14223", "1"))
