from main.view.Display import Display
from main.controller.UserInputController import UserInputController
from main.controller.DataController import DataController


def launch():
    input_controller = UserInputController()
    data_controller = DataController()
    display = Display(data_controller)

    display.startApp()

    input_controller.handleRegions(data_controller, display)
    display.chooseRegion()
    data_controller.region = input_controller.choose(data_controller.regions)

    input_controller.handleEvents(data_controller, display)

    data_controller.event = input_controller.choose(data_controller.events)

if __name__ == '__main__':
    launch()

