
 Movie Recommendation System

A **content-based movie recommendation system** built using the **MovieLens dataset**. This project recommends movies based on **genre similarity** using **TF-IDF vectorization** and **cosine similarity**.

This project is **GitHub-ready**, clean, and suitable for **academic submissions, internships, and viva explanations**.

---

##  Features

* Uses **MovieLens dataset**
* Performs **data cleaning & preprocessing**
* Content-based filtering (no user history needed)
* Uses **TF-IDF + Cosine Similarity**
* Simple, fast, and explainable
* Easy to extend with Flask or collaborative filtering

---

##  Project Structure

```
movie-recommendation-system/
│
├── data/
│   └── movies.csv
│
├── recommender.py
├── demo.py
├── requirements.txt
└── README.md
```

---

##  Dataset

We use the **MovieLens (latest-small)** dataset.

Required file:

* `movies.csv`

Important columns:

* `movieId`
* `title`
* `genres`

Download from MovieLens official website and place it inside the `data/` folder.

---

##  Recommendation Approach

1. Clean movie titles and genres
2. Convert genres into text format
3. Apply **TF-IDF Vectorization**
4. Compute **Cosine Similarity** between movies
5. Recommend top-N similar movies

---

##  How to Run

### 1️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️ Run Demo

```bash
python demo.py
```

---

##  Sample Output

```
Recommendations for 'Toy Story (1995)':
['Bug's Life, A (1998)', 'Monsters, Inc. (2001)', 'Antz (1998)', 'Toy Story 2 (1999)', 'Shrek (2001)']
```

---

##  Evaluation (Qualitative)

* Movies with similar genres are recommended
* Works well for small and medium datasets
* No cold-start problem for new users

---

##  Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

##  Future Improvements

* Add **movie overviews (TMDB API)**
* Implement **Collaborative Filtering**
* Build **Flask REST API**
* Add **UI / Streamlit app**
