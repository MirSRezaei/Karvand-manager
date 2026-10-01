 ## from json to dict

# print(type(d))
# x = json.dumps(d, indent = 2) ## to str
# print(type(x),x)
# print(d['bootcamp'],x[0])
# print(karvands['karvands'][0]['id'])
# {
# "bootcamp" : {
#   "title" : "" , "year" : ""
#   } ,
#  "karvands" : [
#      {
#           "id" : "", "name" : "" , "email" : "" , "city" : "" ,
#           "education" : { "degree" : "" , "fields" : []  
#            }  ,
#               "skills": [
#                       {
#                   "name" : "" , "level" : "" 
#                        }
#                  ]
#           }
#       ]
#   }
# karvand_inp = {
#           "id" : "", "fullname" : "" , "email" : "" , "city" : "" ,
#           "education" : { "degree" : "" , "field" : ""  
#            }  ,
#               "skills": 
#                       []
#                 }
# karvand_inp["fullname"] = input("Name : ")
# karvand_inp["email"] = input("email : ")
# karvand_inp["city"] = input("City : ")
# karvand_inp["education"]["degree"] = input("degree : ")
# karvand_inp["education"]["field"] = input("field : ")
# print("skills and level ,enter 0 if none left : ")
# while True : 
    
    
#     skill_name = input("skill name : ")
#     if skill_name != "0":
#         skill_lvl  = input("level : ")
#         karvand_inp["skills"].append({"name" : skill_name , "level" : skill_lvl })
#     else:
#         break
# print(karvand_inp)

import json
with open('karvands.json', 'r' ) as f:
    karvands = json.load(f)
    print(karvands,type(karvands))
    x = json.dumps(karvands)
    print(x,type(x))