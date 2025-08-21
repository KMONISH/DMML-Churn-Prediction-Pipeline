import pandas as pd, sqlite3, os
os.makedirs('data/transformed', exist_ok=True)
prepared = [f for f in os.listdir('data/clean') if f.startswith('clean_customers_')] if os.path.exists('data/clean') else []
if prepared:
    df = pd.read_csv(os.path.join('data/clean', prepared[-1]))
else:
    df = pd.read_csv('seed/customers.csv')
con = sqlite3.connect('data/transformed/features.db')
df.to_sql('features_customer', con, if_exists='replace', index=False)
print('Stored transformed data to data/transformed/features.db (table: features_customer)')
