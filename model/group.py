class Group(object):
    def __init__(self, header=None, footer=None, name=None):
        self.name = name
        self.header = header
        self.footer = footer
    def __repr__(self):
        return "Name: %s, Head: %s, Foot: %s" % (self.name or 'None', self.header or 'None', self.footer or 'None')
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name