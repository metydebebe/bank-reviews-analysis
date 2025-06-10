import os
import pandas as pd

def load_data():
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, 'data')
    
    df = pd.read_csv(os.path.join(data_path, 'bank_reviews_with_sentiment.csv'))
    df_themes = pd.read_csv(os.path.join(data_path, 'bank_reviews_with_themes.csv'))
    return df, df_themes

def merge_data(df, df_themes):
    return pd.merge(df, df_themes[['review', 'identified_themes']], on='review', how='left')

def explode_themes(df_merged):
    return df_merged.explode('identified_themes')

def calculate_theme_sentiment_counts(df_exploded):
    theme_sentiment_counts = df_exploded.groupby(['bank', 'identified_themes', 'sentiment_label']).size().unstack(fill_value=0)
    theme_sentiment_counts['total'] = theme_sentiment_counts.sum(axis=1)
    theme_sentiment_counts['positive_ratio'] = theme_sentiment_counts.get('POSITIVE', 0) / theme_sentiment_counts['total']
    theme_sentiment_counts['negative_ratio'] = theme_sentiment_counts.get('NEGATIVE', 0) / theme_sentiment_counts['total']
    return theme_sentiment_counts
