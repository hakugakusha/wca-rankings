from main.view.Display import Display
from main.controller.UserInputController import UserInputController
from main.controller.DataController import DataController
from main.model.User import User


def launch():
    user = User()
    input_controller = UserInputController()
    data_controller = DataController(user)
    display = Display(data_controller, user)

    display.startApp()

    input_controller.handleRegions(data_controller, display)
    display.chooseRegion()
    user.region = input_controller.choose(data_controller.regions)

    input_controller.handleEvents(data_controller, display)

    user.event = input_controller.choose(data_controller.events)

if __name__ == '__main__':
    launch()

