import os, pandas as pd, logging
from datetime import datetime
LOG = 'logs/data_ingestion.log'
os.makedirs('data/raw', exist_ok=True)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename=LOG, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_csv(src, name):
    try:
        df = pd.read_csv(src)
        out = f"data/raw/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(out, index=False)
        logging.info(f"Ingested {src} -> {out} (rows={len(df)})")
        print('Ingested', out)
    except Exception as e:
        logging.exception('Failed to ingest %s: %s', src, e)

if __name__ == '__main__':
    ingest_csv('seed/customers.csv', 'customers')
    ingest_csv('seed/orders.csv', 'orders')
    ingest_csv('seed/sessions.csv', 'sessions')
