import json
import random
import sys


from summa import keywords
from summa.summarizer import summarize
from cos_similarity import *

# Markov Chains


def read_file():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
    titles = []
    # for i in range(10):
    #    test = data[i]["postTitle"]
    #    titles += " " + test

    for i in range(10):
        titles.append(data[i]["postTitle"])
        #for comment in comments:
        #    titles += " " + comment

    #titles = titles.replace('\n\n', '')
    print(titles)
    return titles


# print("title: " + data[0]["postTitle"])
# print("comment: " + data[0]["bestcomment"][2])
# print("title: " + titles)


def build_chain(text, chain={}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    return chain


def generate_message(chain, count=100):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    return message


def textrank(text):
    print(summarize(text, ratio=0.2))
    return message


def write_file(message):
    print("--------")
    print(message)


if __name__ == '__main__':
    message = read_file()
    #user_input = input()
    #user_input = "If a movie was made about your life, what would the title be?"
    user_input = "What should I do if I get robbed?"
    message.append(user_input)
    answer = similarity(user_input, message)
    print(answer)
    #textrank(message)
    #chain = build_chain(message)
    #message = generate_message(chain)
    # write_file(message)
