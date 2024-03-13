import unittest
import sys
import os


# Get the parent directory of the current file
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the parent directory to the system path
sys.path.append(parent_dir)

from src.search import process_data, calculate_similarity_scores


class TestQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Preprocess the data
        filepath = "tests/dicoding_courses.json"
        cls.courses, cls.corpus = process_data(filepath)

    def test_calculate_similarity_scores(self):
        # Test similarity scores for the machine learning query
        query = "machine learning"
        expected_sorted_courses = [
            (0.74, {"name": "Belajar Pengembangan Machine Learning", "summary": "Pelajari implementasi machine learning pada industri mulai dari computer vision, natural language, serta deployment proyek machine learning.",
             "course_link": "https://www.dicoding.com/academies/185"}),
            (0.70, {"name": "Belajar Machine Learning untuk Pemula", "summary": "Pelajari materi dasar pengembangan machine learning dan langkah menciptakan model machine learning pertamamu untuk memproses data.",
             "course_link": "https://www.dicoding.com/academies/184"}),
            (0.70, {"name": "Machine Learning Terapan", "summary": "Pelajari penerapan machine learning dengan real-world projects mulai dari predictive analytics, sentiment analysis, dan sistem rekomendasi.",
             "course_link": "https://www.dicoding.com/academies/319"}),
            (0.62, {"name": "Belajar Penerapan Machine Learning dengan Google Cloud", "summary": "Pelajari penerapan machine learning di Google Cloud mulai dari mengembangkan model hingga membangun aplikasi machine learning.",
             "course_link": "https://www.dicoding.com/academies/658"}),
            (0.54, {"name": "Machine Learning Operations (MLOps)", "summary": "Pelajari proses pengembangan dan pengoperasian sistem machine learning dalam lingkup produksi dengan menerapkan berbagai prinsip MLOps.",
             "course_link": "https://www.dicoding.com/academies/443"}),
            (0.51, {"name": "Belajar Penerapan Machine Learning untuk Android", "summary": "Kembangkan keterampilan integrasi Machine Learning di Android dengan memanfaatkan ML Kit, TensorFlow Lite, MediaPipe, dan Firebase ML.",
             "course_link": "https://www.dicoding.com/academies/663"}),
            (0.39, {"name": "Belajar Dasar AI", "summary": "Kelas ini memberikan pemahaman terkait dasar-dasar Artificial Intelligence dan subbidang AI mencakup Machine Learning serta Deep Learning.",
             "course_link": "https://www.dicoding.com/academies/653"}),
            (0.26, {"name": "Memulai Pemrograman dengan Python", "summary": "Pelajari dasar pemrograman Python hingga library populer yang menjadi landasan tren industri seperti data science dan machine learning.",
             "course_link": "https://www.dicoding.com/academies/86"}),
            (0.22, {"name": "Simulasi Ujian TensorFlow Developer Certificate", "summary": "Latihan ujian sebagai persiapan pengambilan ujian sertifikasi TensorFlow Developer Certificate pada program Google Developers Certification.",
             "course_link": "https://www.dicoding.com/academies/312"}),
            (0.09, {"name": "Cloud Practitioner Essentials (Belajar Dasar AWS Cloud)", "summary": "Pelajari materi dasar Cloud dengan menggunakan AWS, dari konsep cloud computing, hingga cara membangun arsitektur yang baik.",
             "course_link": "https://www.dicoding.com/academies/251"})
        ]

        # Calculate similarity scores
        sorted_courses = calculate_similarity_scores(
            query, self.courses, self.corpus)
        # Round the similarity scores to 2 decimal places for the top 10 results
        sorted_courses_rounded = [(round(score, 2), course)
                                  for score, course in sorted_courses[:10]]
        # Extract name, summary, and course_link from the dictionaries in sorted_courses_rounded
        selected_data = [(score, {'name': courseDict['name'], 'summary': courseDict['summary'], 'course_link': courseDict['course_link']})
                         for score, courseDict in sorted_courses_rounded]

        # Assert if the expected sorted list matches the actual sorted list
        self.assertEqual(expected_sorted_courses, selected_data)


if __name__ == "__main__":
    unittest.main()
