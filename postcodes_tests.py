# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:11:54 2021

@author: Luciano
"""

import unittest

class postcodes:
    
    def __init__(self, P):
        # Initialization of the Strings
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.outward = [] 
        self.inward = []
        self.validated = self.validation(P) 
        
    def validate_outward(self, outward):
        # validation of outward part of post code
        if len(outward) == 2:
            if (outward[0] in self.letters) and (outward[1] in self.numbers):
                validated = True
            else:
                validated = False
        elif len(outward) == 3:
            if (outward[0] in self.letters) and (((outward[1] in self.numbers) and (outward[2] in self.letters)) or ((outward[1] in self.letters) and (outward[2] in self.numbers)) or ((outward[1] in self.letters) and (outward[2] in self.letters))):
                validated = True
            else:
                validated = False        
        elif len(outward) == 4:
            if (outward[0] in self.letters) and (outward[1] in self.letters) and (outward[2] in self.numbers) and ((outward[3] in self.letters) or (outward[3] in self.numbers)):
                validated = True
            else:
                validated = False
        else:
            validated = False
        return validated
        
    def validate_inward(self, inward):
        # validation of inward part of postcode
        if len(inward) == 3:
            if (inward[0] in self.numbers) and (inward[1] in self.letters) and (inward[2] in self.letters):
                validated = True
            else:
                validated = False
        else:
            validated = False
        return validated
           
    def validation(self, P):
        # determine whether postcode includes space between inward and outward parts
        spos = P.find(" ")
        if spos != -1:
            self.outward = P[0:spos]
            self.inward = P[(spos+1):]
            # validate outward
            valout = self.validate_outward(self.outward)
            # validate inward
            valin = self.validate_inward(self.inward)
            if valout == True and valin == True:
                validated = True
            else:
                validated = False 
        else:
            validated = False
        return validated

class  TestPostCodes(unittest.TestCase):

    def test_postcodes(self):
        self.assertEqual(postcodes("SW1W 0NY").validated, True)
        self.assertEqual(postcodes("PO16 7GZ").validated, True)
        self.assertEqual(postcodes("GU16 7HF").validated, True)
        self.assertEqual(postcodes("L1 8JQ").validated, True)
        self.assertEqual(postcodes("L18JQ").validated, False)
        self.assertEqual(postcodes("L1 80Q").validated, False)
        self.assertEqual(postcodes("LL 8JQ").validated, False)
        self.assertEqual(postcodes("GUP9 7HF").validated, False)

if __name__ == '__main__':
    unittest.main()
