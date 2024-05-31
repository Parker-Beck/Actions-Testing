import datetime

def main():
    with open("hello.txt", "w") as f:
        f.write(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ": Hello World")
        f.close()
    
if __name__ == "__main__":
    main()