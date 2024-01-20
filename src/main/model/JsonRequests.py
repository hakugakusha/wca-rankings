import requests
import concurrent.futures
from datetime import datetime

class GetRank:

    def __init__(self, region:str = 'north-america', event:str = '333',  time:int = 5) -> None:
        """These variables will be sourced from user input"""
        self.region = region
        self.ranking_type = "average"
        self.event_type = event
        self.time_period = time
        self.current_year = int(datetime.now().year)
        self.number_of_people_we_like_to_show = 500

    def get_init_rank(self) -> requests.Response:
        """Make the GET request"""
        rank_template_url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/rank/{region}/{type}/{event}.json"
        rank_url = rank_template_url.format(region=self.region,type=self.ranking_type,event=self.event_type)
        result = requests.get(rank_url)
        if result.status_code == 200:
            return requests.get(rank_url)
        else:
            raise requests.exceptions.HTTPError(f"Request failed with status code: {result.status_code}")
        
    def get_people_from_rank(self) -> list:
        """Gets all the people from the initial rank"""
        result = self.get_init_rank().json()
        results_by_competition_and_event = result['items']
        people = []
        for entry in results_by_competition_and_event:
            people.append(entry.get('personId'))
        return people

    def get_competition_for_everyone(self) -> dict:
        """Gets the competition for every person from people[]"""
        person_template_url = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/persons/{id}.json"
        person_and_competitions = {}
        people = self.get_people_from_rank()

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

        return person_and_competitions
    
    def sort_competition_by_time(self) -> dict:
        """Sort the competitions by time, returns a dictionary of person and their average"""
        year_to_stop = self.current_year - self.time_period

        # List of people to not include (b/c they don't have a time)
        people_with_no_records = []
        person_and_competitions = self.get_competition_for_everyone()
        for name, result in person_and_competitions.items():
            averages = []
            
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
        person_and_time = dict(sorted(person_and_competitions.items(), key=lambda item:item[1]))

        return person_and_time

    def print_result(self) -> None:
        # Prints out the results
        print(f"Ranking for {self.event_type} in the past {self.time_period} years:")
        final_ranking = self.sort_competition_by_time()
        for index, (name,time) in enumerate(final_ranking.items()):
            if index == self.number_of_people_we_like_to_show:
                break
            print(f"{index + 1}. {name}, Average: {time}")
                
if __name__ == '__main__':
    """Executes the file"""
    rank = GetRank()
    rank.print_result()