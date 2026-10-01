user_count = 1
<<<<<<< HEAD
user_dict = dict() #add #commit #push #branch  ###hello(txt-manager)
=======
user_dict = dict() #add #commit #push #branch  ###hello(txt-managerrrrr)
>>>>>>> txt-manager
#asdasdasdads
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
while True:
    
    command = int(input("1-add , 2-show , 3-edit , 4-del , 5-report , 6-exit : \n"))

    if command == 1:
        karvand_inp = {
          "id" : "", "fullname" : "" , "email" : "" , "city" : "" ,
          "education" : { "degree" : "" , "field" : ""  
           }  ,
              "skills": 
                      []
                }
        karvand_inp["fullname"] = input("Name : ")
        karvand_inp["email"] = input("email : ")
        karvand_inp["city"] = input("City : ")
        karvand_inp["education"]["degree"] = input("degree : ")
        karvand_inp["education"]["field"] = input("field : ")
        print("skills and level ,enter 0 if none left : ")
        while True : 
    
    
            skill_name = input("skill name : ")
            if skill_name != "0":
                skill_lvl  = input("level : ")
                karvand_inp["skills"].append({"name" : skill_name , "level" : skill_lvl })
            else:
                break
        karvand_inp["id"] = user_count

        
        path = r"karvand.json"
        with open(path , "a")   as users:
            users.write(str(user_count))
            for v in user_dict[user_count]:
                users.writelines(v)

            users.write("\n")    
        user_count += 1
    elif command == 2:
        print("Fullname--email--city--skills-education")
        for karvand in user_dict.values():
            print('--'.join([val for val in karvand]))

    elif command ==3:
        changes = ["Fullname" , "Email" ,"City" , "Skills"  , "Education" ]
        name = print("Enter karvands name : ")
        for id,karvand_info in user_dict.items():
            if karvand_info[0] == name:
                print("if no change is needed press 'Enter'.")
                for item in changes.keys():
            
                    change = input(f"{item} :  ")
                    changes[item] = change
                for i,change_inf in zip(range(0,5),changes.values()) : 
                    if  change_inf != "" :
                        user_dict[id][i] == changes
                    

        # for karvand,change in zip(user_dict.values(),changes.keys()):
        #     if (karvand in )







    if command == 6 :
        break


