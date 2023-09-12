# def words_sorting(*args):
#     res = {}
#
#     for word in args:
#         value = sum([ord(c) for c in word])
#         res[word] = value
#     if sum(res.values()) % 2 !=0:
#         return sorted(res.items(),key=lambda x:-x[1])
#     return sorted(res.items(),key=lambda x:(-x[1],x[0]),reverse=True)


def words_sorting(*args):
    def calculate_word_value(word):
        return sum(ord(x) for x in word)

    word_dict = {word: calculate_word_value(word) for word in args}
    total_words_value = sum(word_dict.values())
    if total_words_value % 2 == 0:
        result = sorted(word_dict.items())

    else:
        result = sorted(word_dict.items(),key=lambda x:-x[1])

    return '\n'.join(f'{word} - {count}' for (word,count) in result)




print("-" *  50)
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print("-" *  50)
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print("-" *  50)
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
