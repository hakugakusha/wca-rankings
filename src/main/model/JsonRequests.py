import requests
import concurrent.futures
from TimePeriod import TimePeriod

# These variables will be sourced from user input
continent_id = "north-america"
ranking_type = "average"
country_code = "AE"
event_type = "333"
time_period = TimePeriod.FIVE_YEAR
current_year = 2024


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

    # Gets the competition for every person from people[]
    person_template_url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/persons/{id}.json"
    person_and_competitions = {}

    # running multi-thread requests so not with a for-loop
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # I need to cap it at 500 or else my computer crashes
        futures = [executor.submit(requests.get, person_template_url.format(id=person)) for person in people[:500]]

    # iternate every name from future and stores them
    for future in concurrent.futures.as_completed(futures):
        person_info = future.result().json()
        name = person_info['name']
        competitions = person_info['results']
        person_and_competitions[name] = competitions
        print(f"Fetched {name}")

    # Sort the competitions by time
    time_period_mapping = {
        TimePeriod.ONE_YEAR: 1,
        TimePeriod.TWO_YEAR: 2,
        TimePeriod.THREE_YEAR: 3,
        TimePeriod.FOUR_YEAR: 4,
        TimePeriod.FIVE_YEAR: 5,
    }

    year_to_stop = current_year

    if time_period in time_period_mapping:
        year_to_stop = current_year - time_period_mapping[time_period]

    # List of people to not include
    people_with_no_records = []
    for name, result in person_and_competitions.items():
        averages = []
        
        """
        For every competition, if the competition includes the year, we find the event == 333, stores average,
        and replace the competitions with only the list of averages
        """
        # Now this dictionary gets down to the times and stuff 
        for competition_name, event_details in result.items():
            # Uses the last four characters of the name to determine the year
            if int(competition_name[-4:]) >= year_to_stop:
                # Adds the person's average from the event into the list
                event_detail = event_details.get('333', None)

                if event_detail is not None:
                    # This line assumes the list only has one object in it
                    average = event_detail[0].get('average',None)
                    averages.append(average)
        
        # The following is to see how many averages they have 
        # print(f"{name}'s averages in {event_type} in the recent {int(time_period / 12)} years:")
        # print(averages)
        # print()
                    
        ### I need a test case here for what happens if someone have not participated in any in the past 5 years
        ### and a test for why do someone has an average of 0 for whatever reason?
        if averages:
            # Bruh I was writing a for-loop to sum everything up
            average = round(sum(averages) / len(averages), 2)
            # Yes, I am replacing the competitions with the average
            person_and_competitions[name] = average
        else:
            people_with_no_records.append(name)

        # print(f"{name}'s average in {event_type} in the recent {int(time_period / 12)} years:")
        # print(person_and_competitions[name])

    # Deletes everyone with no recent records
    for people in people_with_no_records:
        del person_and_competitions[people]

    # So apparently we need to grab everything out to sort them, and put the result into a new data structure
    final_ranking = dict(sorted(person_and_competitions.items(), key=lambda item:item[1]))

    # Prints out the results
    number_of_people_we_like_to_show = 50
    print(f"Ranking for {event_type} in the past {int(time_period/12)} years:")
    for index, (name,time) in enumerate(final_ranking.items()):
        if index == number_of_people_we_like_to_show:
            break
        print(f"{index + 1}. {name}, Average: {time}")
        



    

        
    
