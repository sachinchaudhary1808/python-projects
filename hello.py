def main():
    name = input("what's your name?: ")
    if name:  # Check if name is not an empty string
        hello(name)
    else:
        hello()

def hello(to="world"):
    print("hello,", to)

main()

