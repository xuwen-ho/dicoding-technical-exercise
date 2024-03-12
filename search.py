import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
    
# Load the JSON data
with open('dicoding_courses.json', encoding='utf-8') as f:
    courses = json.load(f)

# Corpus will be a list of strings, with each string being the combined name, summary and description
corpus = []
# Each course is a dictionary
for course in courses:
    corpus.append(' '.join([course['name'], course['summary'], course['description']]).lower())
    
# Vectorise data to enable us to compute cosine similarity    
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Prompt the user for the search query
query = input("Enter your search query: ").lower()
query_vector = vectorizer.transform([query])

# Compute the cosine similarity
similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

# Store tuples of (score, course) in a list
score_course_pairs = [(score, courseDict) for score, courseDict in zip(similarity_scores[0], courses)]
# Sort the list of tuples based on the score in descending order
sorted_courses = sorted(score_course_pairs, key=lambda x: x[0], reverse=True)

# Display the top 10 relevant courses
print(f"Top relevant courses for '{query}':")
for i, (score, courseDict) in enumerate(sorted_courses[:10], start=1):
    print(f"{i}. {courseDict['name']} (Similarity Score: {score:.2f})")
    print(f"   Summary: {courseDict['summary']}")
    print(f"   Link: {courseDict['course_link']}")
    print("\n")
