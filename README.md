# Customer Experience Analytics for Fintech Apps

## Task 1: Data Collection and Preprocessing

### Overview

This project aims to scrape and preprocess user reviews from various bank apps on the Google Play Store. The goal is to prepare a clean dataset for further analysis.

### Requirements

<<<<<<< HEAD

- Python 3.11
- Libraries:
  - `pandas`
  - `google-play-scraper`

### Installation

1. **Clone the Repository:**

   git clone https://github.com/metydebebe/bank-reviews-analysis
   cd bank-reviews-analysis
   =======
   Python 3.11

Libraries:

pandas

google-play-scraper

### Installation

Clone the Repository:

git clone https://github.com/metydebebe/bank-reviews-analysis
cd bank-reviews-analysis

Install Required Libraries:

pip install pandas google-play-scraper

## Task 2: Sentiment and Thematic Analysis

### Overview

This task focuses on analyzing the sentiment of bank reviews and extracting recurring themes to uncover satisfaction drivers and pain points.

### Sentiment Analysis

Goal: Quantify sentiment (positive, negative, neutral) of user reviews using the distilbert-base-uncased-finetuned-sst-2-english model.

Method:

Use Hugging Face Transformers pipeline for sentiment classification.

Handle neutral sentiment by thresholding confidence scores.

Aggregate sentiment scores by bank and rating.

Output: CSV file with review text, sentiment labels, and scores.

### Thematic Analysis

Goal: Identify 3–5 actionable themes per bank from user reviews.

Method:

Preprocess reviews with spaCy (tokenization, stop-word removal, lemmatization).

Extract keywords and n-grams using spaCy and TF-IDF.

Manually group keywords into themes such as 'Account Access Issues', 'Customer Support', etc.

Assign themes to reviews based on keyword matching.

Output: CSV file including review text, sentiment data, and identified themes.

### Requirements

Python 3.11

Libraries:

transformers

torch

pandas

spacy

scikit-learn

### Installation

pip install transformers torch pandas spacy scikit-learn
python -m spacy download en_core_web_sm

### Usage

Run the sentiment analysis script to generate sentiment labels and scores.

Run the thematic analysis script to extract keywords, assign themes, and save combined results.

Results are saved as CSV files

> > > > > > > task-2
