import datetime

def main():
    with open("hello.txt", "w") as f:
        f.write(datetime.datetime.now().strftime() + ": Hello")
        f.close()
    
if __name__ == "__main__":
    main()