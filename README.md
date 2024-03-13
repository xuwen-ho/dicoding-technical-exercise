# Dicoding Course Search

This Python script allows you to search for relevant Dicoding courses based on a given query. It calculates the similarity scores between the query and the course descriptions using the TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity methods from the scikit learn libaray.

## Prerequisites

- Python 3.x
- scikit-learn library (`pip install scikit-learn`)

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `search.py` script:

   ```
   python search.py
   ```

4. When prompted, enter the filepath for the JSON file containing the Dicoding course data. For example, if the file is located in the same directory as the script, you can enter:

   ```
   Enter the filepath for the JSON file: dicoding_courses.json
   ```

5. Next, enter your search query:

   ```
   Enter your search query: machine learning
   ```

6. The script will calculate the similarity scores between your query and the course descriptions, and display the top 10 most relevant courses with their names, summaries, similarity scores, and links.

Example output:

```
Top relevant courses for 'machine learning':
1. Belajar Pengembangan Machine Learning (Similarity Score: 0.74)
   Summary: Pelajari implementasi machine learning pada industri mulai dari computer vision, natural language, serta deployment proyek machine learning.
   Link: https://www.dicoding.com/academies/185

2. Belajar Machine Learning untuk Pemula (Similarity Score: 0.70)
   Summary: Pelajari materi dasar pengembangan machine learning dan langkah menciptakan model machine learning pertamamu untuk memproses data.
   Link: https://www.dicoding.com/academies/184

... (remaining top 10 courses)
```