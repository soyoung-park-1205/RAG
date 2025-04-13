from konlpy.tag import Kkma

kkma = Kkma()


def get_main_keyword(sentence: str):
    nouns = get_nouns(sentence)
    return " ".join(nouns)


def get_nouns(sentence: str):
    return kkma.nouns(sentence)
