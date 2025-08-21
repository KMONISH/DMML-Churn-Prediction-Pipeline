import os, pandas as pd, logging
from datetime import datetime
os.makedirs('data/clean', exist_ok=True)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/data_prep.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def prepare():
    # For demo, read seed files if data/raw not present
    customers = pd.read_csv('data/raw/customers_*.csv'.replace('*','')) if False else pd.read_csv('seed/customers.csv')
    orders = pd.read_csv('data/raw/orders_*.csv'.replace('*','')) if False else pd.read_csv('seed/orders.csv')
    sessions = pd.read_csv('data/raw/sessions_*.csv'.replace('*','')) if False else pd.read_csv('seed/sessions.csv')

    customers['created_at'] = pd.to_datetime(customers['created_at'])
    orders['order_ts'] = pd.to_datetime(orders['order_ts'])
    sessions['session_ts'] = pd.to_datetime(sessions['session_ts'])

    spend = orders.groupby('customer_id').agg(total_spend=('amount','sum'), orders_count=('order_id','nunique')).reset_index()
    sess = sessions.groupby('customer_id').agg(sessions_count=('session_id','nunique')).reset_index()

    df = customers.merge(spend, on='customer_id', how='left').merge(sess, on='customer_id', how='left')
    df['total_spend'] = df['total_spend'].fillna(0)
    df['orders_count'] = df['orders_count'].fillna(0).astype(int)
    df['sessions_count'] = df['sessions_count'].fillna(0).astype(int)

    out = f"data/clean/clean_customers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(out, index=False)
    logging.info(f'Prepared data -> {out}')
    print('Prepared data ->', out)

if __name__ == '__main__':
    prepare()
