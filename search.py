import json

# Load the JSON data
with open('dicoding_courses.json', encoding='utf-8') as f:
    courses = json.load(f)

# Corpus will be a list of strings, with each string being the combined name, summary and description
corpus = []

# Each course is a dictionary
for course in courses:
    corpus.append(' '.join([course['name'], course['summary'], course['description']]).lower())
    
print(corpus[1])