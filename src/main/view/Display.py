import requests

class Display:
    def __init__(self, controller, user):
        self.controller = controller
        self.user = user

    def startApp(self):
        print("Hello! Welcome to WCA Rankings!")
        print("This is a joint-project by Brooklyn Schmidt and YuFeng Lin")
        print("Would you like to begin by seeing the list of available regions to choose from?")

    def showRegions(self):
        print(self.controller.regions)
    
    def chooseRegion(self):
        print("Please choose a region: ")

    def showEvents(self):
        print(self.controller.events)

    def chooseEvent(self):
        print("Please choose an event: ")



    



