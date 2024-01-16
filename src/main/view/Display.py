import requests

class Display:
    def __init__(self):
        self.regions = []
        self.storeData = []

    def startApp(self):
        print("Hello! Welcome to WCA Rankings!")
        print("This is a joint-project by Brooklyn Schmidt and YuFeng Lin")
        print("Would you like to see the list of available countries to choose from?")

    def getRegion(self, url):

        rank_url = url.format()


        # Make the GET request
        result = requests.get(rank_url)  

        if result.status_code == 200:
            result = result.json()
            results_by_competition_and_event = result['items']

            for entry in results_by_competition_and_event:
                self.storeData.append(entry)

            for region in self.storeData:
                current_name = region['name']
                if (current_name[0:8] != "Multiple"):
                    self.regions.append(region['name'])

            self.storeData = []

    def showRegions(self):
        print(self.regions)



    



