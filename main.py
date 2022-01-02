__author__ = 'ZackDev'

from controller import *
from model import *
from view import *


class Client:
    def __init__(self):
        model = RandomOrderModel()
        # model = SequentialOrderModel()
        controller = ControllerA()
        view = GridView(controller)

        controller.run(model, view)


if __name__ == '__main__':
    Client()
