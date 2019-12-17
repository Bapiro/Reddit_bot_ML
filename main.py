import json
import random
import sys
import markovify
from summa import keywords
from summa.summarizer import summarize
from cos_similarity import *

# Markov Chains


def read_file():
    with open('dataSum.json', encoding='utf-8') as f:
        data = json.load(f)
    titles = []
    # for i in range(10):
    #    test = data[i]["postTitle"]
    #    titles += " " + test

    for i in range(len(data)):
        titles.append(data[i]["postTitle"] + " " + data[i]["post"])
        # for comment in comments:
        #    titles += " " + comment

    # titles = titles.replace('\n\n', '')

    return titles


def get_comments():
    with open('dataSum.json', encoding='utf-8') as f:
        data = json.load(f)

    # titles = titles.replace('\n\n', '')

    return data


# print("title: " + data[0]["postTitle"])
# print("comment: " + data[0]["bestcomment"][2])
# print("title: " + titles)


def build_chain(text, chain={}):
    textString = ""
    for comment in text:
        if(comment != "[removed]" and comment != "[deleted]"):
            textString += " " + comment

    words = textString.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    return chain


def generate_message(chain, count=20):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    return message


def textrank(text):
    textString = ""
    for comment in text:
        if(comment != "[removed]" and comment != "[deleted]"):
            textString += " " + comment
    message = summarize(textString, ratio=0.1)
    return message


def write_file(message):
    print("--------")
    print(message)


def markov(text):
    textString = ""
    for comment in text:
        if(comment != "[removed]" and comment != "[deleted]"):
            textString += " " + comment

    text = markovify.Text(textString)
    for i in range(1):
        print(text.make_sentence())


if __name__ == '__main__':
    user_input = ""
    while user_input != "stop":
        message = read_file()
        comments = get_comments()
        print("ask a question, ('stop')")
        user_input = input()
        if(user_input == "stop"):
            break
        # user_input = "If a movie was made about your life, what would the title be?"
        # user_input = "What should I do if I get robbed?"
        message.append(user_input)
        answer = similarity(message)
        print(user_input)
        # print("--" + comments[answer]["postTitle"] + "--")
        print(comments[answer]["bestcomment"][0])
        print(answer)
        # textrank(message)
        print("----- sum -----")
        summ = textrank(comments[answer]["bestcomment"])
        print(summ)
        print("----- chain -----")
        # chain = build_chain(comments[answer]["bestcomment"])
        # message = generate_message(chain)
        # write_file(message)
        markov(comments[answer]["bestcomment"])
        print("----- cosine similarity -----")
        commentList = comments[answer]["bestcomment"]
        commentList.append(user_input)
        simComment = similarity(commentList)
        print(commentList[simComment])
