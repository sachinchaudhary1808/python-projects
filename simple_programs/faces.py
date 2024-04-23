# a programm that converts text emoji into graphical emojis


# converts text emoji into graphical emojis if availble in input
def face():
    user_input = input()
    converted_input = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return converted_input
 
# prints the return value of previous function
def main():
    faces = face()
    print(faces)


# main function
main()
