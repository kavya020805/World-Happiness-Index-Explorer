import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def load_data(file_path):
    """Load the World Happiness dataset from an Excel file."""
    return pd.read_excel(file_path)


def clean_data(df):
    """Clean the data: drop duplicates, handle missing values."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def normalize_features(df, features):
    """Min-max normalize specified features in the DataFrame."""
    df_norm = df.copy()
    for feat in features:
        min_val = df_norm[feat].min()
        max_val = df_norm[feat].max()
        df_norm[feat] = (df_norm[feat] - min_val) / (max_val - min_val)
    return df_norm


def plot_correlation(df, features, year):
    """Compute and plot the correlation matrix for given features in a specific year."""
    data = df[df['Year'] == year][features]
    corr = data.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(f"Feature Correlation Heatmap ({year})")
    plt.tight_layout()
    plt.show()


def plot_top_countries(df, year, top_n=10):
    """Plot top N countries by Ladder score for a given year."""
    data = df[df['Year'] == year].nlargest(top_n, 'Ladder score')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Ladder score', y='Country name', data=data, orient='h', palette='viridis')
    plt.xlabel('Ladder Score')
    plt.title(f'Top {top_n} Happiest Countries in {year}')
    plt.tight_layout()
    plt.show()


def compare_countries(df, country1, country2):
    """Interactive comparison of happiness score over years for two countries."""
    data = df[df['Country name'].isin([country1, country2])]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Year', y='Ladder score', hue='Country name', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Ladder Score')
    plt.title(f'Comparison of {country1} vs {country2}')
    plt.tight_layout()
    plt.show()


def main():
    # Path to your dataset Excel file
    file_path = r'D:\Developer\PROJECTS\PYTHON\World Happiness Index Explorer\WHR25_Data_Figure_2.1.xlsx'

    # Load and clean data
    df = load_data(file_path)
    df = clean_data(df)

    # Features for analysis
    features = [
        'Ladder score',
        'Explained by: Log GDP per capita',
        'Explained by: Freedom to make life choices',
        'Explained by: Perceptions of corruption'
    ]

    # Normalize features for correlation analysis
    df_norm = normalize_features(df, features)

    # User parameters
    analysis_year = 2020
    top_n = 10

    # Plot correlation heatmap
    plot_correlation(df_norm, features, analysis_year)

    # Plot top N happiest countries
    plot_top_countries(df, analysis_year, top_n)

    # Interactive comparison
    print("Enter two countries to compare their Happiness Score over years:")
    country1 = input('First country: ')
    country2 = input('Second country: ')
    compare_countries(df, country1, country2)


if __name__ == '__main__':
    main()