import requests
from TimePeriod import TimePeriod

# These variables will be sourced from user input
continent_id = "north-america"
ranking_type = "average"
country_code = "AE"
event_type = "333"
time_frame = TimePeriod.SIX_MONTHS


rank_template_url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/rank/{region}/{type}/{event}.json"
rank_url = rank_template_url.format(region=continent_id,type=ranking_type,event=event_type)


# Make the GET request
result = requests.get(rank_url)

# If we've established connection
if result.status_code == 200:
    result = result.json()
    results_by_competition_and_event = result['items']

    # Gets all the people in one competition
    people = []
    for entry in results_by_competition_and_event:
        people.append(entry.get('personId'))

    # This line can be deleted after program is done
    print(len(people))

    # Gets the competition for every person from people[]
    person_template_url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/persons/{id}.json"
    person_and_competitions = {}

    
    # I think we can only generate 50 people at a time bruh - 
    for i in range(100):
        person = people[i]
        person_url = person_template_url.format(id=person)
        person_info = requests.get(person_url).json()
        print(f"Fetched {i}th guy")
        name = person_info['name']
        competitions = person_info['competitionIds']
        person_and_competitions[name] = competitions

    # Iterate over dictionary items to print both names and competitions
    for name, competitions in person_and_competitions.items():
        print(f"Name: {name}")
        print(f"Competitions: {competitions}")
        print()  # Add a blank line for better readability

        
    
