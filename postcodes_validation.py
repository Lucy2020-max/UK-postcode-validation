# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:11:54 2021

@author: Luciano
"""

class postcodes:
    
    def __init__(self, data):
        import json
        # Initialization of the Strings
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.outward = [] 
        self.inward = []
        self.postcodes = json.loads(data)
        self.post_codes_list = list(self.postcodes.keys())
        self.validated_list = dict()
        for pc in self.post_codes_list:
            self.validated_list[pc] = self.validation(pc)
        self.validated_list = json.dumps(self.validated_list)
        
    def validate_outward(self, outward):
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
        if len(inward) == 3:
            if (inward[0] in self.numbers) and (inward[1] in self.letters) and (inward[2] in self.letters):
                validated = True
            else:
                validated = False
        else:
            validated = False
        return validated
           
    def validation(self, P):
        spos = P.find(" ")
        if spos != -1:
            self.outward = P[0:spos]
            self.inward = P[(spos+1):]
            valout = self.validate_outward(self.outward)
            valin = self.validate_inward(self.inward)
            if valout == True and valin == True:
                validated = True
            else:
                validated = False 
        else:
            validated = False
        return validated
