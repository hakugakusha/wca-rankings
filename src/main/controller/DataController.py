import requests

class DataController:
    def __init__(self, user, region=None, event=None):
        self.events = []
        self.regions = []
        self.storeData = []
        self.user = user

    def getEvents(self, url):
        event_url = url.format()

        result = requests.get(event_url)

        if result.status_code == 200:
            result = result.json()
            set_of_events = result['items']

        for entry in set_of_events:
            self.storeData.append(entry)
            
        for event in self.storeData:
            if (event['id'][-5:] != "magic"):
                self.events.append(event['id']) 

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
                    self.regions.append(region['name'].lower())

            self.storeData = []