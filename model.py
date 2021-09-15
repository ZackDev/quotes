__author__ = 'ZackDev'

import xml.dom.minidom as minidom
import random as random
from abc import ABC, abstractmethod


class Data:
    def __init__(self, author, quote, image_path):
        self.author = author
        self.quote = quote
        self.image_path = image_path


class AbstractModel(ABC):
    xml_file = 'cites.xml'
    path_to_img = 'img/'
    image_type = '.png'
    default_image = path_to_img + 'default' + image_type

    @abstractmethod
    def get_quote(self):
        pass

    def __init__(self):
        self.data_source = minidom.parse(self.xml_file)
        self.quotes = []
        self._populate_quotes()

    def _populate_quotes(self):
        # there are the following cases:
        # -author tag without name -> name: unknown, file: default_image
        # -author tag with name but missing image -> name: author, file: default_image
        # -author tag with name and image -> name: author, file: specific_image

        authors = self.data_source.getElementsByTagName('author')
        for author in authors:
            image_path = self.default_image
            name = author.getAttribute('name')
            image = author.getAttribute('image')
            if name is None:
                name = 'Unknown'
            if image is not None:
                temp_path = self.path_to_img + image
                if self._file_exists(temp_path) is True:
                    image_path = temp_path
                else:
                    image_path = self.default_image
            quotes = author.getElementsByTagName('cite')
            for quote in quotes:
                quote = quote.firstChild.nodeValue
                self.quotes.append(Data(name, quote, image_path))

    def _file_exists(self, path_to_file):
        try:
            f = open(path_to_file)
            f.close()
            return True
        except Exception:
            return False


class RandomOrderModel(AbstractModel):
    def get_quote(self):
        return self._get_random_quote()

    def _get_random_quote(self):
        return random.choice(self.quotes)


class SequentialOrderModel(AbstractModel):
    def get_quote(self):
        return self._pop_quote()

    def _pop_quote(self):
        try:
            return self.quotes.pop(0)
        except Exception:
            return None
