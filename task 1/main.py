import re
from statistics import median


def main():
    dictionary_maker()
    sentence_maker()
    n_gram()


def dictionary_maker():
    file = open('Text.txt', 'r')
    text = file.read()
    file.close()

    words = re.split('\W', text)
    counter = 0
    for index in words:
        check = re.fullmatch('\w',index)
        if not check:
            words.remove(index)
        counter += 1

    dicter = {}
    for word in words:
        count = dicter.get(word, 0)
        dicter[word] = count + 1

    dict_keys = dicter.keys()

    for word in dict_keys:
        print(word, dicter[word])

    print(words)


def sentence_maker():
    file = open('Text.txt', 'r')
    text = file.read()
    file.close()

    sentences = (re.split(r'[\.\?!]', text))
    sentences.remove("")

    words = re.split('\W', text)
    counter = 0

    for index in words:
        check = re.fullmatch('\w', index)
        if not check:
            words.remove(index)
        counter += 1

    print(words)
    print(sentences)
    print("Число предложений  : ", len(sentences))
    print("Количество слов  :", len(words))
    print("Слово в предложении ", len(words)/len(sentences))
    print("Медианное количество слов ", median([len(re.findall(r'\b\w{1,12}\b', sentence)) for sentence in sentences]))


def n_gram():
    file = open('Text.txt', 'r')
    text = file.read()
    file.close()
    print("Введите 1, если хотите сами ввести N и K. Введите 2, если К=10 и N=4. ")
    number = int(input())
    if number == 1:
        print("Введите значение K: ")
        K = int(input())
        print("Введите значение N: ")
        N = input()
    else:
        K = 10
        N = '4'

    words = re.findall(r'\b\w{'+N+'}\\b', text)

    dict= {}

    for word in words:
        count = dict.get(word, 0)
        dict[word] = count + 1

    dict_item = list(dict.items())
    dict_item.sort(key=lambda i: i[1])
    dict_item.reverse()

    counter = 0
    while counter < K and counter != len(dict.items()):
        print(dict_item[counter])
        counter += 1

main()