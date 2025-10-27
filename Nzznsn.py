import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Load the CSV file
df = pd.read_csv("customers.csv")

print("📊 Raw Data Preview:")
print(df.head(), "\n")

# 2️⃣ Data Cleaning
print("🧹 Checking for missing values:")
print(df.isnull().sum(), "\n")

# Convert 'Subscription Date' to datetime
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')

# Drop rows where essential fields are missing
df = df.dropna(subset=['Customer Id', 'Email', 'Subscription Date'])

# 3️⃣ Basic Info
print("ℹ️ Dataset Info:")
print(df.info(), "\n")

# 4️⃣ Key Insights

# a. Total Customers
total_customers = len(df)
print(f"👥 Total Customers: {total_customers}\n")

# b. Customers by Country
customers_by_country = df['Country'].value_counts()
print("🌍 Customers by Country:")
print(customers_by_country, "\n")

# c. Customers by Company
top_companies = df['Company'].value_counts().head(5)
print("🏢 Top 5 Companies with Most Customers:")
print(top_companies, "\n")

# d. Subscription Trend Over Time
df['Year'] = df['Subscription Date'].dt.year
subscriptions_per_year = df['Year'].value_counts().sort_index()
print("📅 Subscriptions per Year:")
print(subscriptions_per_year, "\n")

# 5️⃣ Visualization
plt.figure(figsize=(12, 8))

# Country Distribution
plt.subplot(2, 2, 1)
customers_by_country.plot(kind='bar', color='skyblue')
plt.title("Customers by Country")
plt.xlabel("Country")
plt.ylabel("Number of Customers")

# Top Companies
plt.subplot(2, 2, 2)
top_companies.plot(kind='barh', color='orange')
plt.title("Top 5 Companies with Most Customers")
plt.xlabel("Number of Customers")
plt.ylabel("Company")

# Subscriptions Over Time
plt.subplot(2, 1, 2)
plt.plot(subscriptions_per_year.index, subscriptions_per_year.values, marker='o', color='green')
plt.title("Subscription Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Subscriptions")

plt.tight_layout()
plt.show()

# 6️⃣ Advanced Insight: Domain Analysis (Emails)
df['Email Domain'] = df['Email'].apply(lambda x: x.split('@')[-1])
top_domains = df['Email Domain'].value_counts().head(5)
print("📧 Top Email Domains:")
print(top_domains)
