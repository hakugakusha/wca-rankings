from main.view.Display import Display
from main.controller.UserInputController import UserInputController
from main.controller.DataController import DataController


def launch():
    display = Display()
    input_controller = UserInputController()
    data_controller = DataController()

    display.startApp()

    input_controller.continueApp(display)
    display.chooseRegion()
    data_controller.region = input_controller.chooseRegion(display.regions)

if __name__ == '__main__':
    launch()

