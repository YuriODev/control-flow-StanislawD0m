# Your solution to Exercise 18
rem_name = input()
if rem_name == "yes" :
    ex = input()
    if ex == "yes" :
        drunk = input()
        if drunk == "yes" :
            rekindle = input()
            if rekindle == "yes" :
                output = "Say hi."
            else:
                output = "Don't say hi."
        else:
            convertible = input()
            if convertible == "yes" :
                output = "Say hi."
            else:
                output = "Don't say hi."
    else:
        f_ex = input()
        if f_ex == "yes" :
            output = "Don't say hi."
        else:
            enemy = input()
            if enemy == "yes" :
                convertible = input()
                if convertible == "yes" :
                    output = "Say hi."
                else:
                    output = "Don't say hi."
            else:
                rob = input()
                if rob == "yes" :
                    output = "Don't say hi."
                else:
                    bath = input()
                    if bath == "yes" :
                        output = "Don't say hi."
                    else:
                        output = "Say hi."
else:
    flee = input()
    if flee == "yes" :
        output = "Run for it."
    else:
        cell = input()
        if cell == "yes" :
            output = "Hello, doctor. What are my test results?"
        else:
            sunglasses = input()
            if sunglasses == "yes" :
                output = "Keep walking."
            else:
                output = "Address the person using an amusing nickname such as Sarge , Slugger or Master Blaster."
print(output)