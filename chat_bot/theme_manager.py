class ThemeManager(object):
    def __init__(self):
        self.themes = dict()

    def setTheme(self, theme, group):
        self.themes[group] = theme
        return self.themes[group]

    def getTheme(self, group):
        if group in self.themes:
            return self.themes[group]
        else:
            return "No theme set."
