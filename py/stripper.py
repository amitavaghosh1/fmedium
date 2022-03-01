import re

class Medium:
    def __init__(self):
        self.regex = r"<script src=\"https://cdn-client\.medium\.com/lite/static/js([^\"]+)\"></script>"
        self.subst = ""

    def strip_scripts_with_src(self, h: str) -> str:
        result = re.sub(self.regex, self.subst, h, 0, re.MULTILINE)
        if result:
            return result
        return h

class Others:
    def __init__(self):
        self.regex = r"<script src=\"([^\"]+)\"></script>"
        self.subst = ""

    def strip_scripts_with_src(self, h: str) -> str:
        result = re.sub(self.regex, self.subst, h, 0, re.MULTILINE)
        if result:
            return result
        return h

