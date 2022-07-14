line = 1
id = 2000
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
            f = open(
                "C://Users//dell//Documents//programing//python//login_signup//data.txt", "r")
            text = f.read()
            list = text.split("\n")
            list1 = []
            try:
                key = int(input("Enter Key: "))
                temp = key
                temp = temp % 2000
                text1 = list[temp]
                list1 = text1.split("|")
            except IndexError:
                key = 0
            except ValueError:
                key = 0
            if str(key) not in list1:
                print("You don't have an account")
                line = 1
            else:
                count = 1
                while True:
                    if count == 1:
                        password = input("Enter Pass: ")
                        if password not in list1:
                            print("")
                            print("Wrong password")
                            print("for forget password: 1")
                            print("for re-enter password: 2")
                            print("for back: 3")
                            event = input("Enter Your Command: ")
                            if event == "3":
                                line = 1
                                break
                            count = 1
                        else:
                            print("")
                            print("Your ID:     ", list1[0])
                            print("Your Name:   ", list1[1])
                            print("Your Branch: ", list1[2])
                            print("Your Email:  ", list1[3])
                            input("Press Enter")
                            break
            f.close()
        elif command == '2':
            print("")
            first = input("Enter Your Name: ")
            stream = input("Enter Your Branch: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your password: ")
            f = open(
                "C://Users//dell//Documents//programing//python//login_signup//data.txt", "r")
            text = f.read()
            list = text.split("\n")
            id = 2000+len(list)
            print("----Thanks For Creating an account-----")
            information = ["\n", str(id), "|", first,
                           "|", stream, "|", email, "|", password]
            f = open(
                "C://Users//dell//Documents//programing//python//login_signup//data.txt", "a")
            f.writelines(information)
            f.close()
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
        break
