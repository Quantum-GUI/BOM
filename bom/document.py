class Document(object):
    def getElementById(self, id):
        raise NotImplementedError

    def getElementsByTagName(self, name):
        raise NotImplementedError

    def getElementsByClassName(self, name):
        raise NotImplementedError

    def createElement(self, element):
        raise NotImplementedError

    def removeChild(self, element):
        raise NotImplementedError

    def appendChild(self, element):
        raise NotImplementedError

    def replaceChild(self, new, old):
        raise NotImplementedError

    def write(self, text):
        raise NotImplementedError

    def querySelectorAll(self, query):
        raise NotImplementedError
