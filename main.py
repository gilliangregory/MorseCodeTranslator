from binarytree import *
ERROR = "~~~ INVALID INPUT! PLEASE TRY AGAIN! ~~~"
def get_input()-> str:
    return input(">>>").strip()

def display_options()->None:
    print("""~~~~~~~~~~~~~~~~~~~~~~~~
Select how you want to proceed:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|1| Draw binary tree
|2| Encode from English to Morse Code
|3| Decode from Morse Code to English""")

def display_morsecode(option, rooty, whatever):
    #whatever is either the morseCode encoding or English decoding that is done in process_selection

#INPUT OPTION 1 PRINTING   
    if option == "1":
        print("~" * 60)
        drawtree(rooty)
        print("~" * 60)
        
#INPUT OPTION 2 PRINTING
    if option == "2":
        print("~" * 60)
        print(whatever)
        print("~" * 60)
        
#INPUT OPTION 3 PRINTING
    if option == "3":
        print("~" * 60)
        print(whatever)
        print("~" * 60)
        
def process_selection(user_input, option):

#INPUT OPTION 1 PROCESSING
    if option == "1":
        return

#INPUT OPTION 2 PROCESSING
    elif option == "2":
        text = user_input.upper()
        morseCode = ""

        for char in text:
            dotty = []
            tomorse(rooty, char, dotty)
            code = "".join(dotty)
            morseCode = morseCode + code + " "
        return morseCode

#INPUT OPTION 3 PROCESSING
    elif option == "3":
        morse = user_input

        message = toeng(morse, rooty)
        return message

def main():
    while True:
        display_options()
        selection = get_input()

        if selection in ["1", "2", "3", "tree", "encode", "decode"]:
            print("~" * 60)
            print("Type \" back\" to revisit the options menu.")
            print("Type \" exit\" to exit the program.")
            print("~" * 60)

            while True:

#USER SELECTS INPUT OPTION 1
                if selection in ["1", "tree"]:
                    print("\nDo you want to print the tree? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    display_morsecode("1", rooty)

#USER SELECTS INPUT OPTION 2
                if selection in ["2", "encode"]:
                    print("\nWhat message do you want to encode from English to Morse Code? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    morsey = process_selection(user_input, "2")
                    display_morsecode("2", rooty, morsey)

#USER SELECTS INPUT OPTION 3
                if selection in ["3", "decode"]:
                    print("\nWhat message do you want to decode from Morse Code to English? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    englo = process_selection(user_input, "3")
                    display_morsecode("3", rooty, englo)

        elif selection == "exit":
                exit()

if __name__ == "__main__":
    main()

                    
        
