import unittest
from notebooks import insights_and_recommendations as ir

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        self.df, self.df_themes = ir.load_data()
        self.df_merged = ir.merge_data(self.df, self.df_themes)
        self.df_exploded = ir.explode_themes(self.df_merged)
        self.theme_sentiment_counts = ir.calculate_theme_sentiment_counts(self.df_exploded)

    def test_merge_dataframes(self):
        self.assertIn('identified_themes', self.df_merged.columns)
        self.assertGreaterEqual(len(self.df_merged), len(self.df))  # Adjusted assertion

    def test_theme_counts(self):
        theme_counts = self.df_exploded['identified_themes'].value_counts()
        self.assertGreater(len(theme_counts), 0)

    def test_sentiment_ratios(self):
        self.assertIn('positive_ratio', self.theme_sentiment_counts.columns)
        self.assertIn('negative_ratio', self.theme_sentiment_counts.columns)

if __name__ == '__main__':
    unittest.main()
