def Code(inputText=""):
    replacements = {
        "f": "ju", "a": "fa", "r": "su", "m": "ra", "n": "re", "j": "na", 
        "e": "je", "k": "ne", "b": "fe", "h": "ke", "t": "te", "d": "ja", 
        "g": "ka", "s": "ta", "q": "se", "p": "sa", "u": "tu", "z": "ge", 
        "v": "za", "w": "ze", "x": "zu", "y": "ga", "c": "fu", "i": "ku", 
        "o": "ru", "l": "nu", "natu": "ju", "tatu": "su", "rje": "re"
    }

    inputText = inputText.lower()
    for key, value in replacements.items():
        inputText = inputText.replace(key, value)
    return inputText

def Decode(inputText=""):
    replacements = {
        "fa": "a", "fe": "b", "fu": "c", "ja": "d", "je": "e", "ju": "f", 
        "ka": "g", "ke": "h", "ku": "i", "na": "j", "ne": "k", "nu": "l", 
        "ra": "m", "re": "n", "ru": "o", "sa": "p", "se": "q", "su": "r", 
        "ta": "s", "te": "t", "tu": "u", "za": "v", "ze": "w", "zu": "x", 
        "ga": "y", "ge": "z"
    }

    inputText = inputText.lower()
    for key, value in replacements.items():
        inputText = inputText.replace(key, value)
    return inputText

class Lingo:
    class LetterA:
        Disp = "A"
        Sound = "Fa"
    class LetterB:
        Disp = "B"
        Sound = "Fe"
    class LetterC:
        Disp = "C"
        Sound = "Fu"
    class LetterD:
        Disp = "D"
        Sound = "Ja"
    class LetterE:
        Disp = "E"
        Sound = "Je"
    class LetterF:
        Disp = "F"
        Sound = "Ju"
    class LetterG:
        Disp = "G"
        Sound = "Ka"
    class LetterH:
        Disp = "H"
        Sound = "Ke"
    class LetterI:
        Disp = "I"
        Sound = "Ku"
    class LetterJ:
        Disp = "J"
        Sound = "Na"
    class LetterK:
        Disp = "K"
        Sound = "Ne"
    class LetterL:
        Disp = "L"
        Sound = "Nu"
    class LetterM:
        Disp = "M"
        Sound = "Ra"
    class LetterN:
        Disp = "N"
        Sound = "Re"
    class LetterO:
        Disp = "O"
        Sound = "Ru"
    class LetterP:
        Disp = "P"
        Sound = "Sa"
    class LetterQ:
        Disp = "Q"
        Sound = "Se"
    class LetterR:
        Disp = "R"
        Sound = "Su"
    class LetterS:
        Disp = "S"
        Sound = "Ta"
    class LetterT:
        Disp = "T"
        Sound = "Te"
    class LetterU:
        Disp = "U"
        Sound = "Tu"
    class LetterV:
        Disp = "V"
        Sound = "Za"
    class LetterW:
        Disp = "W"
        Sound = "Ze"
    class LetterX:
        Disp = "X"
        Sound = "Zu"
    class LetterY:
        Disp = "Y"
        Sound = "Ga"
    class LetterZ:
        Disp = "Z"
        Sound = "Ge"
    Map = {
    1: LetterA,
    2: LetterB,
    3: LetterC,
    4: LetterD,
    5: LetterE,
    6: LetterF,
    7: LetterG,
    8: LetterH,
    9: LetterI,
    10: LetterJ,
    11: LetterK,
    12: LetterL,
    13: LetterM,
    14: LetterN,
    15: LetterO,
    16: LetterP,
    17: LetterQ,
    18: LetterR,
    19: LetterS,
    20: LetterT,
    21: LetterU,
    22: LetterV,
    23: LetterW,
    24: LetterX,
    25: LetterY,
    26: LetterZ}