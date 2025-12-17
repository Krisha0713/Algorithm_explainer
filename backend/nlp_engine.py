from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Known concepts with example descriptions
CONCEPTS = {
    "master theorem": [
        "divide and conquer recurrence",
        "recurrence relation time complexity",
        "T(n)=aT(n/b)+f(n)",
        "algorithm complexity analysis"
    ],
    "dynamic programming": [
        "overlapping subproblems",
        "optimal substructure",
        "memoization",
        "bottom up approach"
    ]
}

# Prepare corpus
concept_names = list(CONCEPTS.keys())
documents = [" ".join(v) for v in CONCEPTS.values()]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

def identify_concept(user_input):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    best_match_index = similarities.argmax()

    if similarities[0][best_match_index] < 0.2:
        return None

    return concept_names[best_match_index]
