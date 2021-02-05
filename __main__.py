from bot import WebBot, Walmart

def main():
    #Runs the WebBot depending on website
    print("Select Store:\nBestBuy = 1\nWalmart = 2")
    selection = input()
    if selection == 1:
        w = WebBot()
    else:
        w = Walmart()


if __name__ == "__main__":
    main()