__author__ = 'ZackDev'

from abc import ABC, abstractmethod


class AbstractController(ABC):
    def run(self, model, view):
        self.model = model
        self.view = view
        self.view.main()

    @abstractmethod
    def get_quote(self):
        raise NotImplementedError


class ControllerA(AbstractController):
    def get_quote(self):
        data = self.model.get_quote()
        if data:
            self.view.update_quote(data.quote)
            self.view.update_author(data.author)
            self.view.update_image(data.image_path)
        else:
            exit()
