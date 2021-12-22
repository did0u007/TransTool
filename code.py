import json

"""
lngs = {
    0: ["Arabic", "ar", "ara", "arab"],
    1: ["English", "en", "eng", "anglais"],
    2: ["French", "fr", "fre", "français"],
    3: ["Spanish", "es", "spa", "espagnol"],
    4: ["German", "de", "ger", "allemand"],
}

json.dump(lngs, open("languages.json", "w", encoding="utf-8"))

"""


class TransTool:
    def take(self, text):
        pass

    def SetPrimaryLang(self, lang):
        pass

    def TransToLang(self, lang):
        pass

    def ShowSupportedLang():
        lngs = json.load(open('languages.json', 'r', encoding='utf-8' ))
        return [lng[0] for lng in lngs.values()]

    def AddLanguages(self, *args):
        pass

    def DropLang(self, lang):
        pass

print(TransTool.ShowSupportedLang())