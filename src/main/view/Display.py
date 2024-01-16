import requests

class Display:
    def __init__(self, controller):
        self.controller = controller

    def startApp(self):
        print("Hello! Welcome to WCA Rankings!")
        print("This is a joint-project by Brooklyn Schmidt and YuFeng Lin")
        print("Would you like to begin by seeing the list of available regions to choose from?")

    def showRegions(self, regions):
        print(regions)
    
    def chooseRegion(self):
        print("Please choose a region: ")

    def showEvents(self, events):
        print(events)

    def chooseEvent(self):
        print("Please choose an event: ")



    



