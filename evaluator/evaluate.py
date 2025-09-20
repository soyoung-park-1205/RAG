from preprocess.extract_keyword import get_nouns, get_nouns_okt


def judge_answer_by_nouns(answer, context, question):
    question_nouns = get_nouns_okt(question)
    answer_nouns = get_nouns_okt(answer)
    context_nouns = get_nouns_okt(context)
    answer_nouns = [x for x in answer_nouns if x not in question_nouns]
    context_nouns = [x for x in context_nouns if x not in question_nouns]
    count = len([noun for noun in answer_nouns if noun in context_nouns])
    if len(answer_nouns) == 0:
        return False
    if count / len(answer_nouns) < 0.6:
        return False
    else:
        return True
