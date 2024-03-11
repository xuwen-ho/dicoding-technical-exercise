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