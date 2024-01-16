continent_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/continents.json'
country_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/countries.json' 
events_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/events.json'

class UserInputController:

    def continueApp(self, display):
        user_input = input("(y/n): ")

        if (user_input.lower() == 'y'):
            display.getRegion(continent_url)
            display.getRegion(country_url)
            display.showRegions()
        else:
            print("See you next time!")
            exit()

    def chooseRegion(self, list_of_regions):
        keepAsking = True
        while(keepAsking):

            user_input = input()
            user_input = user_input[0].upper() + user_input[1:]
            if (user_input in list_of_regions):
                keepAsking = False
                return user_input
            else:
                print("Try Again!")
                continue


