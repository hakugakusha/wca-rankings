from datetime import datetime

continent_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/continents.json'
country_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/countries.json'
events_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/events.json'
 

class UserInputController:

    def handleRegions(self, data_controller, display):
        user_input = input("(y/n): ")

        if (user_input.lower() == 'y'):
            data_controller.getRegion(continent_url)
            data_controller.getRegion(country_url)
            display.showRegions()
        else:
            print("See you next time!")
            exit()

    def handleEvents(self, data_controller, display):
        data_controller.getEvents(events_url)
        display.showEvents()
        display.chooseEvent()



    def choose(self, list_of_param):
        keepAsking = True
        while(keepAsking):

            user_input = input()
            if (user_input.lower() in list_of_param):
                keepAsking = False
                return user_input
            else:
                print("Try Again!")
                continue

    def input_time(self):
        return int(input(f"Please enter an integer, representing the number of years from {datetime.now().year}.\n"))


