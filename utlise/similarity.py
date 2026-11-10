from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):
    """
    Resume aur Job Description ke beech
    TF-IDF based cosine similarity calculate karta hai.
    """

    # Documents
    documents = [
        resume_text,
        job_description
    ]

    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    # Convert text into numerical vectors
    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    # Calculate cosine similarity
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    # Convert into percentage
    similarity_score = similarity[0][0] * 100

    return round(similarity_score, 2)