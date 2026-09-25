user_count = 1
user_dict = dict()
while True:
    
    command = int(input("1-add , 2-show , 3-edit , 4-del , 5-report , 6-exit : \n"))

    if command == 1:
        fullname = input("Full name : ")
        email = f"{fullname}@email.com"
        city = input("City : ")
        education = input("Education/Degree : ")
        skills = input("Skills : ")
        user_dict[user_count] = [fullname ,email , city , skills , education] 
        path = r"users.txt"
        with open(path , "a")   as users:
            users.write(str(user_count))
            for v in user_dict[user_count]:
                users.write(v)

            users.write("\n")    
        user_count += 1





    if command == 6 :
        break


