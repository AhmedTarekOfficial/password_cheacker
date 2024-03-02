while True:
    password = input("please enter your password : ")

    special_characters = ["*","#","!","%","$","/","@"]

    if len(password) < 8 :
        print("please enter at least 8 characters in your password \n \n")

    is_upper = False
    is_lower = False 
    white_space = False
    tap = False
    special_charac = False
    digit = False
    score = 0

    for passwrod_check in  password:
        if passwrod_check.islower():
            is_lower = True
            score += 3

        if passwrod_check.isdigit():
            digit = True
            score+=3
        if passwrod_check.isupper():
            is_upper = True
            score += 3
            
        if passwrod_check in special_characters and not special_charac:
            special_charac = True
            score += 3
            
        if ' ' in password:
            white_space = True
            print("the password contain white space please try again and enter password without white space")
            break
        if passwrod_check in "\t":
            break


    

    if white_space or tap:
        break
    else:

        if is_upper and is_lower and digit and special_charac:
            print("the password in perfect")
        elif is_lower and digit:
         print("suggetion to help you to strong your password , \n try to put upper chracter and special chracter  \n \n")
        elif is_lower and is_upper:
         print("suggetion to help you to strong your password , \n try to put digit chracter and special chracter  \n \n")
        elif is_lower and special_charac :
         print("suggetion to help you to strong your password , \n try to put upper chracter and digits  \n \n")
        elif is_upper and digit:
         print("suggetion to help you to strong your password , \n try to put lower chracter and special chracter  \n \n")
        elif is_upper and special_charac:
         print("suggetion to help you to strong your password , \n try to put lower chracter and digits  \n \n")
        elif is_upper:
            print("suggetion to help you to strong your password , \n try to put lower chracter and digits and special chracter  \n \n")
        elif is_lower:
            print("suggetion to help you to strong your password , \n try to put upper chracter and digits and special chracter \n \n")
        elif special_charac:
         print("suggetion to help you to strong your password , \n try to put lower chracter and digits and upper chracter \n \n")
        elif digit:
            print("suggetion to help you to strong your password , \n try to put lower chracter and upper chracter and special chracter  \n \n")


        if is_lower and digit and is_upper and special_characters:
            print("the password is perfect")
            print("the score of your password is ",score)
        elif is_upper and special_charac :
            print("your password  between strong and very good")
            print("the score of your password is ",score)
        elif is_lower and special_charac:
            print("your password  between strong and very good ")
            print("the score of your password is ",score)
        elif digit and special_charac:
            print("your password  between strong and very good ")
            print("the score of your password is ",score)
        elif digit:
                print("your password from week to good")
                print("the score of your password is ",score)
        elif is_lower:
            print("your password from week to good")
            print("the score of your password is ",score)
        elif is_upper:
            print("your password from week to good")
            print("the score of your password is ",score)
        elif special_charac :
            print("your password from week to good")
            print("the score of your password is ",score)
        
        