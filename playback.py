# A programm that prints ... or pause between words
def code():
    userinput = input("say something\n")
    userinput = userinput.replace(" ", "...")
    return userinput    

def main():
    pause  = code()
    print(pause)

main()
