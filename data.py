import requests
import rauth


class DataFilter:
    @classmethod
    def getLocation(cls, zipcode, price, cuisine):
        params = dict()
        params["term"] = "restaurant"
        params["location"] = zipcode
        params["open_now"] = True
        params["price"] = price
        params["categories"] = cuisine
        return params

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
        return resp.json()




