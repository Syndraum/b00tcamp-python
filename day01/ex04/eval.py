class Evaluator:
    def zip_evaluate(coef, words):
        if not isinstance(coef, list) or not isinstance(words, list):
            return -1
        if len(coef) != len(words):
            return -1
        count = 0
        list_zip = zip(coef, words)
        for tuple in list_zip:
            count += tuple[0] * len(tuple[1])
        return count
