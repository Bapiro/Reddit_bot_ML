from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math


def similarity(reddit_questions):
    Z = []
    for i in range(len(reddit_questions)):
        Z.append(reddit_questions[i])

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(Z)

    #Q = []
    # Q.append(question)
    #tfidf_vectorizer = TfidfVectorizer()
    #tfidf_question = tfidf_vectorizer.transform(Q)
    # print("----------------")
    # print(tfidf_question.shape[0])
    # print(tfidf_question)

    best_answer = ""
    best_angle = 200

    #simi = cosine_similarity(tfidf_question, tfidf_matrix)
    # simi.sort()
    # print(simi[0])

    for i in range(len(reddit_questions)):
        # print(i)
        # print(len(reddit_questions)-1)
        if(i+1 == len(reddit_questions)):
            continue

        cos_simi = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i])

        if(cos_simi[0][0] > 1):
            return reddit_questions[i]

        angle_in_radians = math.acos(cos_simi[0][0])
        degree = math.degrees(angle_in_radians)

        if (degree < best_angle):
            best_answer = i
            best_angle = degree

    return best_answer
