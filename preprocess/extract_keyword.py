from konlpy.tag import Kkma, Okt

kkma = Kkma()
okt = Okt()

def get_main_keyword(sentence: str):
    nouns = get_nouns(sentence)
    return " ".join(nouns)


def get_nouns(sentence: str):
    pos_nouns = []
    for word, pos in kkma.pos(sentence):
        if pos in ['NNG', 'NNP', 'NR', 'NNB', 'NNM', 'NR'] and len(word) >= 2:
            pos_nouns.append(word)
    return pos_nouns


def get_nouns_okt(sentence: str):
    pos_nouns = []
    for word, pos in okt.pos(sentence):
        if pos in ['Noun', 'Number'] and len(word) >= 2:
            pos_nouns.append(word)
    return pos_nouns
