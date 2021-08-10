class RoleManager(object):
    def __init__(self):
        self.admin = dict()

    def isAdmin(self, id):
        return id in self.admin

    def setAdmin(self, id):
        self.admin[id] = True
