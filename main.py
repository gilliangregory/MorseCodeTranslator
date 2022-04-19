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

def display_morsecode(option, rooty, text="", message=""):
    if option == "1":
        print("~" * 60)
        drawtree(rooty)
        print("~" * 60)

    if option == "2":
        print("~" * 60)
        print("~" * 60)

    if option == "3":
        print("~" * 60)
        print("~" * 60)
        

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

                if selection in ["1", "tree"]:
                    print("\nDo you want to print the tree? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    display_morsecode("1", rooty)

                if selection in ["2", "encode"]:
                    print("\nWhat message do you want to encode from English to Morse Code? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    display_morsecode("2",text)

                if selection in ["3", "decode"]:
                    print("\nWhat message do you want to decode from Morse Code to English? ")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    display_morsecode("3",message)

        elif selection == "exit":
                exit()

if __name__ == "__main__":
    main()

                    
        
