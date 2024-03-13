import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def process_data(filepath):
    """
    Load JSON data from a file and preprocess it for future similarity calculation.

    Args:
        filepath (str): The path to the JSON file containing dicoding course data.

    Returns:
        tuple: A tuple containing:
            - courses (list): List of dictionaries each representing a course.
            - corpus (list): List of strings each containing combined name, summary and description of a course.
    """

    # Load the JSON data
    with open(filepath, encoding='utf-8') as f:
        courses = json.load(f)

    # Corpus will be a list of strings, with each string being the combined name, summary and description
    corpus = []
    # Each course is a dictionary
    for course in courses:
        corpus.append(
            ' '.join([course['name'], course['summary'], course['description']]).lower())

    return courses, corpus


def calculate_similarity_scores(query, courses, corpus):
    """
    Calculate similarity scores between a search query and course descriptions.

    Args:
        query (str): The search query.
        courses (list): List of dictionaries, each representing a course.
        corpus (list): List of strings, each containing combined name, summary and description of a course.

    Returns:
        list: A list of tuples containing similarity scores and corresponding course dictionaries, sorted in descending order of similarity scores.
    """

    # Vectorise data to enable us to compute cosine similarity
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Vectorise search query to allow for use of cosine similarity
    query_vector = vectorizer.transform([query])

    # Compute the cosine similarity
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

    # Store tuples of (score, course) in a list
    score_course_pairs = [(score, courseDict)
                          for score, courseDict in zip(similarity_scores[0], courses)]
    # Sort the list of tuples based on the score in descending order
    sorted_courses = sorted(
        score_course_pairs, key=lambda x: x[0], reverse=True)

    return sorted_courses


def display_results(sorted_courses):
    """
    Display the top relevant courses based on similarity scores.

    Args:
        sorted_courses (list): A list of tuples containing similarity scores and corresponding course dictionaries, sorted in descending order of similarity scores.
    """

    # Display the top 10 relevant courses
    print(f"Top relevant courses for '{query}':")
    for i, (score, courseDict) in enumerate(sorted_courses[:10], start=1):
        print(f"{i}. {courseDict['name']} (Similarity Score: {score:.2f})")
        print(f"   Summary: {courseDict['summary']}")
        print(f"   Link: {courseDict['course_link']}")
        print("\n")


if __name__ == "__main__":
    filepath = input("Enter the filpath for the Json file: ")
    courses, corpus = process_data(filepath)

    query = input("Enter your search query: ").lower()
    sorted_courses = calculate_similarity_scores(query, courses, corpus)

    display_results(sorted_courses)
