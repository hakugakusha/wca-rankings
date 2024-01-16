from main.view.Display import Display

continent_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/continents.json'
country_url = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/countries.json' 

def launch():
    display = Display()

    display.startApp()

    display.getRegion(continent_url)
    display.getRegion(country_url)
    display.showRegions()
    
    

if __name__ == '__main__':
    launch()

