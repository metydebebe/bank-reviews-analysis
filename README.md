# Customer Experience Analytics for Fintech Apps

## Task 1: Data Collection and Preprocessing

### Overview

This project aims to scrape and preprocess user reviews from various bank apps on the Google Play Store. The goal is to prepare a clean dataset for further analysis.

### Requirements

- Python 3.11
- Libraries:
  - `pandas`
  - `google-play-scraper`

### Installation

Clone the Repository:

git clone https://github.com/metydebebe/bank-reviews-analysis
cd bank-reviews-analysis

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

# Task 3: Database Export and Management

## Overview

This task involves exporting the processed bank reviews data from Oracle XE into a dump file (.dmp) using Oracle Data Pump (expdp). This enables backup, sharing, and migration of the database schema and data.

## Steps Taken

Created an Oracle directory object pointing to a physical folder on the Oracle server machine.

Granted read and write privileges on the directory to the database user.

Used the expdp command-line utility to export the schema and data into a .dmp file.

Stored the dump file and export log in a dedicated dumps/ folder within the project for organization and version control.

## Requirements

Oracle Database XE 21c installed and running.

Oracle user with sufficient privileges (DATAPUMP_EXP_FULL_DATABASE role).

Access to Oracle command-line utilities (expdp).

Physical directory on the server machine accessible by Oracle for dump files.

# Usage

Create the directory object and grant privileges:

sql
CREATE OR REPLACE DIRECTORY dump_dir AS 'C:\app\metya\product\21c\dbhomeXE\dump';
GRANT READ, WRITE ON DIRECTORY dump_dir TO demo_user;
Run the export command from your OS terminal:

expdp demo_user/demouser@localhost:1521/XEPDB1 DIRECTORY=dump_dir DUMPFILE=bank_reviews.dmp LOGFILE=export.log SCHEMAS=DEMO_USER
Locate the dump file and log in the dumps/ folder of the project.

# Task 4: Insights and Recommendations

## Overview

In this task, we derive actionable insights from the sentiment and thematic analysis of bank app user reviews. We visualize key findings to better understand user satisfaction drivers and pain points, and provide practical recommendations to improve the apps.

## Objectives

Identify at least 2 drivers (e.g., fast navigation) and 2 pain points (e.g., app crashes) supported by data.

Compare customer experience across banks (e.g., Commercial Bank of Ethiopia vs. Bank of Abyssinia).

Create 3 clear and labeled visualizations (e.g., sentiment trends, rating distributions, keyword clouds).

Use a dedicated Git branch (task-4) for development, with commits and pull requests for version control.

## Data and Methods

Combined sentiment labels and thematic categories extracted from user reviews.

Exploded theme lists to analyze frequency and sentiment distribution by bank.

Visualized theme frequencies, sentiment distributions, and word clouds using Matplotlib and Seaborn.

Interpreted findings to identify key drivers and pain points.

## Usage

Open the notebook notebooks/insights_and_recommendations.ipynb.

Run all cells sequentially to reproduce the analysis and visualizations.

Visualizations are saved in the notebooks/figures/ folder.
