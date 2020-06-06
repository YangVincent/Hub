from fbchat import Client
from fbchat.models import *

class Hub:
    def __init__(self):
        self.Client = Client("vincenty.376@gmail.com", "password")

    def logout(self):
        self.Client.logout()


if __name__ == "__main__":
    client = None

    while True:
        command = input("hub >> ")
        print("You entered " + command)
    
        if command == "e":
            print("Logging out")
            client.logout()
            break
        elif command == "login":
            print("Logging in")
            client = Hub()
