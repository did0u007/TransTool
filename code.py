import json
import os


class TransTool:
    encod_to = "utf-8"
    __plang = 22
    __tlang = 22

    def __init__(self):
      
        self.BASE_DIR = os.path.dirname(__file__)
        if (f := "Dict.json") not in os.listdir(self.BASE_DIR):
            with open(f, "w", encoding=self.encod_to) as fb:
                obj = {self.__plang: {}}
                json.dump(obj, fb)

    def take(self, text, form = 'title'):
        """take the text that will be translated
        \n params text : str -> input text
        \n params form : str -> the form of text returned " UPPER, lower, Title"
        \n return : str -> translated texte if successful
        \n return : str -> same input text if faild
        """
        text = text.lower()
        text_ = self.__retrieve(self.__tlang, self.__store(self.__plang, text))
        if form.lower() == "upper":
            text_ = text_.upper()
        elif form.lower() == "lower" :
            text_ = text_.lower()
        else:
            text_ = text_.title()
        return text_

    def __translate(self):
        src = self.ShowSupportedLang()[self.__plang][1]
        dict_: dict = self.ShowDict(langs_only=False)
        dest_list = [(i,self.ShowSupportedLang()[int(i)][1]) for i in dict_.keys() ]
        plang_items = dict_[str(self.__plang)].items()
        for id, text in plang_items:
            for lang_id, dest in dest_list:
                if id not in dict_[lang_id].keys():
                    # Todo Translation part will be here
                    dict_[lang_id][id] = f'translated({text})'
        with open(os.path.join(self.BASE_DIR, 'Dict.json'), 'w', encoding=self.encod_to) as f:
            json.dump(dict_, f)


    def __store(self, lang_idx, text):
        dict_: dict = self.ShowDict(langs_only=False)
        lang_idx = str(lang_idx)
        try: 
            text_list = dict_[lang_idx].values()
            idx_list = [int(x) for x in dict_[lang_idx].keys()]
            text_id = max(idx_list) + 1
            if text not in text_list :
                dict_[lang_idx][str(text_id)] = text
            else:
                return  idx_list[text_list.index(text)]

        except :
            text_id = '0'
            dict_[lang_idx][text_id] = text
        with open(os.path.join(self.BASE_DIR, 'Dict.json'), 'w', encoding=self.encod_to) as f:
            json.dump(dict_, f)
        self.__translate()
        return text_id
    
    def __retrieve(self, lang_idx, text_id):
        dict_: dict = self.ShowDict(langs_only=False)
        try:
            return dict_[str(lang_idx)][str(text_id)]
        except:
            return dict_[str(self.__plang)][str(text_id)]

    def Update(self):
        self.__translate()

    def SetPrimaryLang(self, lang):
        """Set the language to translate from
        \n  default is English
        \n  params : int -> index of the language
        \n  params : str -> name or code of the language
        \n  return language index if successful else None
        """
        plang = None
        try:
            lang = int(lang)
        except:
            pass
        if isinstance(lang, int):
            if lang in self.ShowSupportedLang().keys():
                self.__plang = plang = lang
        elif isinstance(lang, str):
            lang = lang.lower()
            for idx, lng in zip(
                self.ShowSupportedLang().keys(), self.ShowSupportedLang().values()
            ):
                if lang in lng:
                    plang = self.SetPrimaryLang(idx)
                    break

        return plang

    def SetTransToLang(self, lang):
        """Set the language to translate to
        \n default is English
        \n params : int -> index of the language
        \n params : str -> name or code of the language
        \n return language index if successful else None
        """
        tlang = None
        try:
            lang = int(lang)
        except:
            pass
        if isinstance(lang, int):
            if str(lang) not in self.ShowDict(langs_only=False).keys():
                InvalidLanguegeError = ValueError(f"You Have To Call AddLanguages({lang}) First")
                raise InvalidLanguegeError
            if lang in self.ShowSupportedLang().keys():
                self.__tlang = tlang = lang
        elif isinstance(lang, str):
            lang = lang.lower()
            for idx, lng in zip(
                self.ShowSupportedLang().keys(), self.ShowSupportedLang().values()
            ):
                if lang in lng:
                    tlang = self.SetTransToLang(idx)
                    break

        return tlang

    def ShowSupportedLang(self):
        """To Show The Supported Languages And it's Indexes"""
        LANGUAGES = {
            1: ["afrikaans", "af"],
            2: ["albanian", "sq"],
            3: ["amharic", "am"],
            4: ["arabic", "ar"],
            5: ["armenian", "hy"],
            6: ["azerbaijani", "az"],
            7: ["basque", "eu"],
            8: ["belarusian", "be"],
            9: ["bengali", "bn"],
            10: ["bosnian", "bs"],
            11: ["bulgarian", "bg"],
            12: ["catalan", "ca"],
            13: ["cebuano", "ceb"],
            14: ["chichewa", "ny"],
            15: ["chinese (simplified)", "zh-cn"],
            16: ["chinese (traditional)", "zh-tw"],
            17: ["corsican", "co"],
            18: ["croatian", "hr"],
            19: ["czech", "cs"],
            20: ["danish", "da"],
            21: ["dutch", "nl"],
            22: ["english", "en"],
            23: ["esperanto", "eo"],
            24: ["estonian", "et"],
            25: ["filipino", "tl"],
            26: ["finnish", "fi"],
            27: ["french", "fr"],
            28: ["frisian", "fy"],
            29: ["galician", "gl"],
            30: ["georgian", "ka"],
            31: ["german", "de"],
            32: ["greek", "el"],
            33: ["gujarati", "gu"],
            34: ["haitian creole", "ht"],
            35: ["hausa", "ha"],
            36: ["hawaiian", "haw"],
            37: ["hebrew", "iw"],
            38: ["hebrew", "he"],
            39: ["hindi", "hi"],
            40: ["hmong", "hmn"],
            41: ["hungarian", "hu"],
            42: ["icelandic", "is"],
            43: ["igbo", "ig"],
            44: ["indonesian", "id"],
            45: ["irish", "ga"],
            46: ["italian", "it"],
            47: ["japanese", "ja"],
            48: ["javanese", "jw"],
            49: ["kannada", "kn"],
            50: ["kazakh", "kk"],
            51: ["khmer", "km"],
            52: ["korean", "ko"],
            53: ["kurdish (kurmanji)", "ku"],
            54: ["kyrgyz", "ky"],
            55: ["lao", "lo"],
            56: ["latin", "la"],
            57: ["latvian", "lv"],
            58: ["lithuanian", "lt"],
            59: ["luxembourgish", "lb"],
            60: ["macedonian", "mk"],
            61: ["malagasy", "mg"],
            62: ["malay", "ms"],
            63: ["malayalam", "ml"],
            64: ["maltese", "mt"],
            65: ["maori", "mi"],
            66: ["marathi", "mr"],
            67: ["mongolian", "mn"],
            68: ["myanmar (burmese)", "my"],
            69: ["nepali", "ne"],
            70: ["norwegian", "no"],
            71: ["odia", "or"],
            72: ["pashto", "ps"],
            73: ["persian", "fa"],
            74: ["polish", "pl"],
            75: ["portuguese", "pt"],
            76: ["punjabi", "pa"],
            77: ["romanian", "ro"],
            78: ["russian", "ru"],
            79: ["samoan", "sm"],
            80: ["scots gaelic", "gd"],
            81: ["serbian", "sr"],
            82: ["sesotho", "st"],
            83: ["shona", "sn"],
            84: ["sindhi", "sd"],
            85: ["sinhala", "si"],
            86: ["slovak", "sk"],
            87: ["slovenian", "sl"],
            88: ["somali", "so"],
            89: ["spanish", "es"],
            90: ["sundanese", "su"],
            91: ["swahili", "sw"],
            92: ["swedish", "sv"],
            93: ["tajik", "tg"],
            94: ["tamil", "ta"],
            95: ["telugu", "te"],
            96: ["thai", "th"],
            97: ["turkish", "tr"],
            98: ["ukrainian", "uk"],
            99: ["urdu", "ur"],
            100: ["uyghur", "ug"],
            101: ["uzbek", "uz"],
            102: ["vietnamese", "vi"],
            103: ["welsh", "cy"],
            104: ["xhosa", "xh"],
            105: ["yiddish", "yi"],
            106: ["yoruba", "yo"],
            107: ["zulu", "zu"],
        }

        return LANGUAGES

    def ShowDict(self, langs_only=True):
        """To Show The Languages Added To Dict Or Full Dict Data"""
        with open("Dict.json", "r", encoding=self.encod_to) as f:
            lngs = json.load(f)
            if not langs_only:
                return lngs
            else:
                id = map(int, lngs.keys())
                return [self.ShowSupportedLang()[ln] for ln in id]

    def AddLanguages(self, *args, force=False):
        """You Have To Show Supported Languages To See Languges indexes First
        By Calling ShowSupportedLang() Method
        \n force : bool -> True to ignore index errors (False by default)
        \n args :int -> indexs of languages to add
        \n return True if successful else False
        """
        f = open("Dict.json", "r", encoding=self.encod_to)
        langs_dict = json.load(f)
        f.close()
        lngs_id = [i for i in map(int, langs_dict.keys())]
        err = False
        to_add = []
        for i in args:
            try:
                i = int(i)
            except:
                pass
            if i not in self.ShowSupportedLang().keys():
                err = True
            elif i not in lngs_id:
                to_add.append(i)
            else:
                continue
        if not force and err:
            return False
        if force or not err:
            for idx in to_add:
                langs_dict[idx] = {}
            json.dump(langs_dict, open("Dict.json", "w", encoding=self.encod_to))
            return True

    def DropLang(self, lang):
        """To Drop Language From Dictionery
        \n params : int -> index of language to drop
        \n params : str -> name or code of language to drop
        \n return True if successful else False
        """
        with open("Dict.json", "r", encoding=self.encod_to) as f:
            langs_dict: dict = json.load(f)
        droped = False
        try:
            lang = int(lang)
        except:
            pass

        if isinstance(lang, int):
            if lang in list(map(int, langs_dict.keys())):
                del langs_dict[str(lang)]
                json.dump(langs_dict, open("Dict.json", "w", encoding=self.encod_to))
                droped = True

        elif isinstance(lang, str):
            lang = lang.lower()
            for idx, lng in zip(
                self.ShowSupportedLang().keys(), self.ShowSupportedLang().values()
            ):
                if lang in lng:
                    droped = self.DropLang(idx)
                    break

        return droped

    def GetPrimaryLang(self):
        """Return The Primary Language"""

        return {self.__plang: self.ShowSupportedLang()[self.__plang]}

    def GetTransToLang(self):
        """Return The Primary Language"""

        return {self.__tlang: self.ShowSupportedLang()[self.__tlang]}

