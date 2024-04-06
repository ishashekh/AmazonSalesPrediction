# Assuming data_cleaned is available from Team Member 1's work

# Step 2: Convert price-related fields and percentages to numeric formats
data_cleaned['discounted_price'] = data_cleaned['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
data_cleaned['actual_price'] = data_cleaned['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
data_cleaned['discount_percentage'] = data_cleaned['discount_percentage'].str.replace('%', '').astype(float)
data_cleaned['rating'] = pd.to_numeric(data_cleaned['rating'], errors='coerce')

# Step 3: Handle missing values
data_cleaned['rating'] = data_cleaned['rating'].fillna(data_cleaned['rating'].mean())
data_cleaned['rating_count'] = data_cleaned['rating_count'].fillna(0)

# Commit message: "Implemented feature transformation and missing value handling."
