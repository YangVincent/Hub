# Docs: https://fbchat.readthedocs.io/en/stable/examples.html

from iterfzf import iterfzf
from fbchat import Client
from fbchat.models import *
import os

USER = os.environ.get('USER')
PASS = os.environ.get('PASS')




# Helper for fzf
def iter_conversations(convos):
    for c in convos:
        yield c


class Hub:
    def __init__(self):
        self.Client = Client(USER, PASS)

    def logout(self):
        self.Client.logout()
 
    def list(self, size=20):
        users = self.Client.fetchThreadList(limit=size)
        convos = {}
        for u in users[:100]:
            if u.name != None:
                convos[u.name] = u.uid
        print("fetched conversations")
        return convos

    def fetchUsers(self):
        self.users = self.Client.fetchAllUsers()
        return self.users
    def fetchUserInfo(self, ui):
        return self.Client.fetchUserInfo(ui)

    def get_conversations(self):
        return self.conversations

    def fetch_messages(self, conv_id):
        messages = self.Client.fetchThreadMessages(thread_id=conv_id, limit=10)
        return messages

    def search_conversations(self):
        convos = self.list()
        print("Convos is " + str(convos))
        selection = iterfzf(iter_conversations(convos.keys()), multi=False)

        # Fetch thread messages
        print(self.fetch_messages(convos[selection]))





if __name__ == "__main__":
    print("Logging in")
    client = Hub()

    while True:
        command = input("hub >> ")
        cmds = command.split(" ")
        print("You entered " + command)
    
        if cmds[0] == "e":
            print("Logging out")
            client.logout()
            break
        elif cmds[0] == "ls":
            users = client.list()
            print("users' IDs: {}".format([user.uid for user in users[:10]]))
            print("users' names: {}".format([user.name for user in users[:10]]))
        elif cmds[0] == "lsal":
            if len(cmds) == 1:
                print("lsal requires another argument (user id)")
            else:
                ui = client.fetchUserInfo(cmds[1])
                print("user info is " + str(ui))
        elif cmds[0] == "f":
            # Use fzf to fuzzy search through conversations
            # TODO(yangvincent): Add prefilled search.
            client.search_conversations()



