import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("2019.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())


data = data.drop_duplicates()


data = data.fillna(data.mean(numeric_only=True))

print("\nDataset after cleaning:")
print(data.head())


happiest = data.sort_values(by="Score", ascending=False)

print("\nTop 10 Happiest Countries:")
print(happiest[["Country or region", "Score"]].head(10))

print("\nTop 10 Least Happy Countries:")
print(happiest[["Country or region", "Score"]].tail(10))

average = data["Score"].mean()

print("\nAverage Happiness Score:", round(average, 2))


top10 = happiest.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top10["Country or region"], top10["Score"])

plt.title("Top 10 Happiest Countries")
plt.xlabel("Countries")
plt.ylabel("Happiness Score")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="GDP per capita",
    y="Score"
)

plt.title("GDP vs Happiness Score")
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="Social support",
    y="Score"
)

plt.title("Social Support vs Happiness Score")
plt.xlabel("Social Support")
plt.ylabel("Happiness Score")

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="Healthy life expectancy",
    y="Score"
)

plt.title("Life Expectancy vs Happiness Score")
plt.xlabel("Healthy Life Expectancy")
plt.ylabel("Happiness Score")

plt.tight_layout()
plt.show()


correlation = data.select_dtypes(include="number").corr()

print("\nCorrelation with Happiness Score:")
print(correlation["Score"].sort_values(ascending=False))


plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Global Happiness Report Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nHappiness Report Analysis Completed!")