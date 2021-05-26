# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:53:10 2021

@author: Luciano
"""

import json
from postcodes_validation import postcodes

# define a list of post codes to be validated
post_codes = {"SW1W 0NY" : None, "PO16 7GZ" : None, "GU16 7HF" : None, "L1 8JQ" : None, "L18JQ" : None, "L1 80Q" : None, "LL 8JQ" : None, "GUP9 7HF" : None}

# create a formatted string of the JSON object
text_in = json.dumps(post_codes)

# process the list of postcodes to be validated
validated_post_codes = postcodes(text_in)

# print validated list of postcodes
print(validated_post_codes.validated_list)

