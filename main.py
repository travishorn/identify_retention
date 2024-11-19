import pandas as pd

# Load CSV data
data = pd.read_csv('dataset.csv')

# Ensure datetime format for date columns
data['signup_date'] = pd.to_datetime(data['signup_date'])
data['activity_date'] = pd.to_datetime(data['activity_date'])

# Add a column for the first week of engagement
data['first_week'] = data['activity_date'] <= (data['signup_date'] + pd.Timedelta(weeks=1))

# Filter to first-week engagement
first_week_engagement = data[data['first_week']]

# Identify feature engagement within the first week
features = ['feature_a_used', 'feature_b_used', 'feature_c_used']
first_week_features = first_week_engagement.groupby('user_id')[features].max()

# Retention analysis
# Merge first-week feature usage with overall user data
user_data = data.groupby('user_id').agg(
    signup_date=('signup_date', 'min'),
    num_active_months=('num_active_months', 'max')
).reset_index()
user_data = user_data.merge(first_week_features, on='user_id', how='left')

# Flag users as retained after 3 months (if num_active_months >= 3)
user_data['retained_3_months'] = user_data['num_active_months'] >= 3

# Calculate retention rates for each feature
retention_by_feature = {}
for feature in features:
    retained = user_data[user_data[feature] == 1]['retained_3_months'].mean()
    retention_by_feature[feature] = retained

# Display results
print("Retention rates for users engaging with features in the first week:")
for feature, rate in retention_by_feature.items():
    print(f"{feature}: {rate:.2%}")
