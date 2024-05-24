import datetime

def main():
    with open("hello.txt", "w") as f:
        f.write(str(datetime.datetime.now().time) + ": Hello")
        f.close()
    
if __name__ == "__main__":
    main()