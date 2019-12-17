from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math


def similarity(reddit_questions):

    # Create Z-matrix from the questions
    Z = []
    for i in range(len(reddit_questions)):
        Z.append(reddit_questions[i])

    # Create td-idf matrix for the questions
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(Z)

    best_answer = ""
    best_angle = 200

    for i in range(len(reddit_questions)):

        # Stops the code from comparing the question to itself
        if(i+1 == len(reddit_questions)):
            continue

        # Calculate cosine similarity between the asked question and the reddit questions
        cos_simi = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[i])

        # Acos does not work for values above 1
        if(cos_simi[0][0] > 1):
            return reddit_questions[i]

        # Get the angle between the questions
        angle_in_radians = math.acos(cos_simi[0][0])
        degree = math.degrees(angle_in_radians)

        # Store the best angle and corresponding question
        if (degree < best_angle):
            best_answer = i
            best_question = reddit_questions[i]
            best_angle = degree

    print(best_angle)
    return best_answer
