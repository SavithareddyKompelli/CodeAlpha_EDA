import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load dataset
df = pd.read_csv("scraped_books.csv")

# 2️⃣ Clean Price column
df["Price"] = df["Price"].str.replace("Â", "", regex=False)
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].astype(float)

# 3️⃣ Save cleaned dataset
df.to_csv("scraped_books_cleaned.csv", index=False)

# ⛔ Important: this line prevents plot window from blocking the script
plt.close('all')

# 4️⃣ Graph 1 — Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=20)
plt.title("Book Price Distribution")
plt.savefig("price_distribution.png")
plt.close()

# 5️⃣ Graph 2 — Rating Frequency
plt.figure(figsize=(8,5))
sns.countplot(x=df["Rating"], order=df["Rating"].value_counts().index)
plt.title("Rating Frequency")
plt.savefig("rating_frequency.png")
plt.close()

# 6️⃣ Graph 3 — Availability Status
plt.figure(figsize=(8,5))
sns.countplot(y=df["Availability"])
plt.title("Availability Status")
plt.savefig("availability.png")
plt.close()

print("🎉 All graphs generated and saved successfully!")
