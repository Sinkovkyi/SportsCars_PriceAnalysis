import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv(r"Sport_car_price.csv", sep=',')

#Cleaning and converting relevant columns to numeric types for accurate analysis
df.dropna(inplace=True)
df['Price (in USD)'] = df['Price (in USD)'].replace('[\$,]', '', regex=True).astype(float)
df['Horsepower'] = pd.to_numeric(df['Horsepower'], errors='coerce')
df['0-60 MPH Time (seconds)'] = pd.to_numeric(df['0-60 MPH Time (seconds)'], errors='coerce')
df['Engine Size (L)'] = pd.to_numeric(df['Engine Size (L)'], errors='coerce')



# Filtering recent data for selected sports car brands and plotting their price trends on a logarithmic scale
def plot_price_trends(df):
    brands = ['Ferrari', 'Lamborghini', 'McLaren']
    colors = ['#c43d16', '#4B4B4B', '#fcb500']

    df_filtered = df[(df['Year'] >= 2019) & (df['Car Make'].isin(brands))]
    custom_yticks = [125000, 250000, 500000, 1000000]
    ytick_labels = [f"${int(p):,}" for p in custom_yticks]

    plt.figure(figsize=(13, 6))
    sns.set_style("whitegrid")

    for brand, color in zip(brands, colors):
        sns.regplot(
            data=df_filtered[df_filtered['Car Make'] == brand],
            x='Year',
            y='Price (in USD)',
            color=color,
            scatter=False,
            label=brand
        )

    plt.yscale('log')
    plt.title('Price trends of the Top 3 Supercar Brands', fontsize=16)
    plt.xlabel('YEAR', labelpad=14, fontweight='bold')
    plt.ylabel('')
    plt.legend()
    plt.gca().set_yticks(custom_yticks)
    plt.gca().set_yticklabels(ytick_labels)
    plt.tight_layout()
    plt.show()


# Creating a logarithmic boxplot to visualize price distribution across all car brands without showing outliers
def plot_price_distribution(df):
    plt.figure(figsize=(14, 7))

    sns.boxplot(
        data=df,
        x='Car Make',
        y='Price (in USD)',
        fliersize=0
    )

    plt.yscale('log')
    custom_yticks = [25000, 75000, 125000, 250000, 500000, 1000000, 2000000]
    ytick_labels = [f"${int(p):,}" for p in custom_yticks]

    plt.yticks(custom_yticks, ytick_labels, fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.title('Price distribution by Brand', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Filtering cars with 0-60 mph times under 3 seconds and plotting a sorted bar chart of their acceleration times
def plot_fastest_cars_with_price_limited(df, price_cap=None):
    df_fast = df[df['0-60 MPH Time (seconds)'] <= 3].copy()
    df_fast_sorted = df_fast.sort_values(by='0-60 MPH Time (seconds)', ascending=False).copy()

    df_fast_sorted['Car Model'] = pd.Categorical(
        df_fast_sorted['Car Model'],
        categories=df_fast_sorted['Car Model'].unique(),
        ordered=True
    )
    
    if price_cap is None:
        price_cap = df_fast_sorted['Price (in USD)'].quantile(0.70)
    

    capped_prices = np.minimum(df_fast_sorted['Price (in USD)'], price_cap)
    
    norm = plt.Normalize(capped_prices.min(), price_cap)
    colors = plt.cm.viridis(norm(capped_prices))

    plt.figure(figsize=(15, 7))
    ax = sns.barplot(
        data=df_fast_sorted,
        x='Car Model',
        y='0-60 MPH Time (seconds)',
        palette=colors
    )

    sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
    sm.set_array([])

    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label(f'Price (in USD)', rotation=270, labelpad=15, fontweight='bold')

    plt.title('Blistering 0–60 mph in Under 3 Seconds with Price Range', fontsize=15)
    plt.xlabel('')
    plt.ylabel('0–60 mph time', labelpad=8, fontweight='bold')
    plt.xticks(rotation=45, fontsize=9, ha='right')
    plt.tight_layout()
    plt.show()



# Plotting a quadratic regression of price versus engine size on a logarithmic scale with custom price category labels
def plot_engine_vs_price(df):
    df_filtered = df[df['Engine Size (L)'] > 0].copy()

    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df_filtered,
        x='Engine Size (L)',
        y='Price (in USD)',
        scatter_kws={'alpha': 0.4, 'color': 'teal'},
        line_kws={'color': 'darkred', 'linewidth': 2},
        order=2  
    )

    plt.yscale('log')
    yticks = [50000, 200000, 1000000]
    yticklabels = ['Low Price', 'Medium Price', 'High Price']
    plt.yticks(yticks, yticklabels)
    plt.title('Engine size Influences Car price', fontsize=16)
    plt.xlabel('Engine Size (L)', fontsize=12, labelpad=10, fontweight='bold')
    plt.ylabel('', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()


# MAIN EXECUTION
plot_price_trends(df)
plot_price_distribution(df)
plot_fastest_cars_with_price_limited(df)
plot_engine_vs_price(df)
