import requests

class Display:
    def __init__(self):
        self.regions = []
        self.storeData = []
        self.events = []

    def startApp(self):
        print("Hello! Welcome to WCA Rankings!")
        print("This is a joint-project by Brooklyn Schmidt and YuFeng Lin")
        print("Would you like to begin by seeing the list of available regions to choose from?")

    def getRegion(self, url):

        rank_url = url.format()


        # Make the GET request
        result = requests.get(rank_url)  

        if result.status_code == 200:
            result = result.json()
            set_of_continents = result['items']

            for entry in set_of_continents:
                self.storeData.append(entry)

            for region in self.storeData:
                current_name = region['name']
                if (current_name[0:8] != "Multiple"):
                    self.regions.append(region['name'])

            self.storeData = []

    def showRegions(self):
        print(self.regions)
    
    def chooseRegion(self):
        print("Please choose a region to analyze: ")

    def showEvents(self):
        print(self.events)



    



