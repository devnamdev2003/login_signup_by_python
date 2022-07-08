line = 1
id = 2000
data = {id: {
    "name": "", "branch": "", "password": "", "email": ""
}}
print("")
print("-*-*-*---LOGIN/SIGNUP SYSTEM---*-*-*-")
while True:
    if line == 1:
        print("")
        print("For login: 1")
        print("For Signup: 2")
        print("For exit: 3")
        command = input("Enter your command: ")
        if command == '1':
            try:
                key = int(input("Enter Your Key: "))
            except ValueError:
                key = 0
            except NameError:
                key = 0
            if key in data.keys() and data[2000]["name"] != "":
                count = 1
                while True:
                    if count == 1:
                        password = input("Enter Your password: ")
                        if password == data[key]["password"]:
                            print("")
                            print("Your ID:     ", key)
                            print("Your Name:   ", data[key]["name"])
                            print("Your Branch: ", data[key]["branch"])
                            print("Your Email:  ", data[key]["email"])
                            input("Press Enter")
                            break
                        else:
                            print("Wrong Password ")
                            count = 1
            elif key==0:
                print("please enter a right key")
            else:
                print("You don't have an account")
                line = 1
        elif command == '2':
            print("")
            first = input("Enter Your Name: ")
            stream = input("Enter Your Branch: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your password: ")
            data[id] = {}
            data[id]["name"] = first
            data[id]["branch"] = stream
            data[id]["email"] = email
            data[id]["password"] = password
            print("----Thanks For Creating an account-----")
            print("Your Key is: ", id)
            id = id+1
            line = 1
        elif command == '3':
            line = 2
        else:
            print("Wrong command")
            line == 1
    elif line == 2:
        print("Thank you!")
        if data[2000]["name"] == "":
            break
        else:
            for i in data:
                print(i, "|", data[i]["name"], "|", data[i]
                      ["branch"], "|", data[i]["email"])
        break
