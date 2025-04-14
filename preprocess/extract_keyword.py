from konlpy.tag import Kkma

kkma = Kkma()

def get_main_keyword(sentence: str):
    nouns = get_nouns(sentence)
    return " ".join(nouns)


def get_nouns(sentence: str):
    pos_nouns = []
    for word, pos in kkma.pos(sentence):
        if pos in ['NNG', 'NNP', 'NR', 'NNB', 'NNM']:
            pos_nouns.append(word)
    return pos_nouns
