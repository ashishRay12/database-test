"""
-pID             ->  char
-pTAGS           ->  []
-pPRICE          -> int
-pDESC           -> char
-pMEDIAURL       -> url
-pCAT            -> char
-pSTOCK-PRESENT  -> bool
-pSTOCK-QUANTITY -> int      
-pOFFER          -> int
-pFEATURES       -> []
"""


import json
from random import *
#print(randint(0,9))


mockDB = []


for i in range(0,100):
    data = {}
    data["id"]    = randint(782932,9887462363243724)
    data["price"] = randint(100,4000)
    data["quantity"] = randint(0,30)
    data["stock-present"] = choice([True, False])
    data["offer"] = randint(20,50)
    data["features"] = ["feature-1","feature-2","feature-3","feature-4"]
    data["tags"] = ["tag-1","tag-2","tag-3","tag-4","tag-5"]
    data["cat"] = ["CAT-1","CAT-2","CAT-3","CAT-4"]
    data["desc"] = "loren is ipsum io poinh termiso oilo punolipsu"
    data["media-url"] = "https://placehold.it/350x150"
    
    #json_data = json.dumps(data)
    with open('data.txt', 'a') as outfile:
         json.dump(data, outfile, sort_keys = True, indent = 4,ensure_ascii=False)
	 outfile.write(",");
         outfile.write("\n");
    mockDB.append(data)
print mockDB
    
