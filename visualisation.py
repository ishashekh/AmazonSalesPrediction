import matplotlib.pyplot as plt
import seaborn as sns

# Visualization 1: Distribution of Product Ratings
plt.figure(figsize=(8, 6))
sns.histplot(data_cleaned['rating'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')

# Visualization 2: Distribution of Rating Counts (Sales Volume Proxy)
plt.figure(figsize=(8, 6))
sns.histplot(data_cleaned['rating_count'], bins=20, color='salmon')
plt.title('Distribution of Rating Counts (Sales Volume Proxy)')

# Visualization 3: Revenue Distribution Among Top 10 Products
data_cleaned['estimated_revenue'] = data_cleaned['rating_count'] * data_cleaned['discounted_price']
top_products_by_revenue = data_cleaned.nlargest(10, 'estimated_revenue')
plt.figure(figsize=(10, 8))
plt.pie(top_products_by_revenue['estimated_revenue'], labels=top_products_by_revenue['product_name'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', n_colors=10))
plt.title('Revenue Distribution Among Top 10 Products by Estimated Revenue')
