from main.view.Display import Display
from main.controller.UserInputController import UserInputController
from main.controller.DataController import DataController
from main.model.User import User
from main.model.JsonRequests import GetRank
import pycountry



def launch():
    user = User()
    input_controller = UserInputController()
    data_controller = DataController(user)
    display = Display(data_controller, user)

    display.startApp()

    input_controller.handleRegions(data_controller, display)
    display.chooseRegion()

    # this line stores the user region
    region_name = input_controller.choose(data_controller.regions)
    user.region = pycountry.countries.get(name=region_name).alpha_2

    input_controller.handleEvents(data_controller, display)

    # and this one stores the user event
    user.event = input_controller.choose(data_controller.events)

    # and this is for time
    user.time = input_controller.input_time()

    result = GetRank(user.region,user.event,user.time)

    result.print_result()

if __name__ == '__main__':
    launch()

