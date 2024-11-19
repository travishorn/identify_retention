import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Flag users as retained for each month
user_data['retained_3_months'] = user_data['num_active_months'] >= 3

# RETENTION CURVES

# Retention rate calculations by feature
retention_by_feature = {}
for feature in features:
    retention_by_feature[feature] = user_data[user_data[feature] == 1]['retained_3_months'].mean()

# Prepare data for retention curves
retention_curves = {}
for feature in features:
    retention_curves[feature] = user_data.groupby(feature)['num_active_months'].apply(
        lambda x: np.array([(x >= i).mean() for i in range(1, 7)])
    )

# Plot retention curves
plt.figure(figsize=(10, 6))
for feature, rates in retention_curves.items():
    plt.plot(range(1, 7), rates[1], label=feature.replace('_used', '').capitalize())
plt.title('Retention Curves by Feature')
plt.xlabel('Months')
plt.ylabel('Retention Rate')
plt.legend()
plt.grid()
plt.savefig('output/retention_curves.png')
plt.clf();

# RETENTION RATE PERCENTAGES

retention_rates = {}
for feature in features:
    retention_rates[feature] = user_data.groupby(feature)['retained_3_months'].mean()

print("Retention rates for users engaging with features in the first week:")
for feature, rate in retention_by_feature.items():
    print(f"{feature}: {rate:.2%}")

# Extract features and retention rates for plotting
features = list(retention_by_feature.keys())
retention_rates = [rate * 100 for rate in retention_by_feature.values()]  # Convert to percentages

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(features, retention_rates, color='skyblue', edgecolor='black')

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f"{height:.1f}%", ha='center', va='bottom')

# Add title and labels
plt.title("Retention Rates by Feature", fontsize=16)
plt.xlabel("Features", fontsize=14)
plt.ylabel("Retention Rate (%)", fontsize=14)

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig('output/retention_rates.png')
