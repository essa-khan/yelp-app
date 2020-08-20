# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, json 
    
def search_businesses(search_term, search_location):
    
    api_key = "z6Ki-01wJkXzlDyFkdLMp-uhkqdC5ZnMJmQH2QdXfpYU3Z15zh5HbVhCM24LNiQ1BVib8rwP5PLMPATJblk3tuAVjfw_rp5w37w1SiXSKR1YXp0mOmCY-ZCVvotWW3Yx"
    
    url = "https://api.yelp.com/v3/businesses/search"
    
    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }
    
    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 5,
    }
    
    businesses_object = requests.get(url, headers=my_headers, params=my_params)
    
    businesses_dict = businesses_object.text
    
    businesses_json = json.loads(businesses_dict)
    
    businesses_list = businesses_json["businesses"]
      
    return businesses_list

#    # Extract the list of businesses from businesses_dict
#    businesses_list = businesses_dict["businesses"]
#    
#    # Create an empty list
#    list_of_businesses = []
#    
#    # Loop through list of businesses and append each business to list_of_businesses variable
#    for each in businesses_list:
#        list_of_businesses.append(each)
    
#    return list_of_businesses
    
    
#    return businesses_dict
  
# Invoke the search_businesses functions
#invoke_yelp = search_businesses("restaurants", "chicago")
#print(invoke_yelp)