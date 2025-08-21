import os, json, requests, logging
from datetime import datetime
LOG = 'logs/data_ingestion.log'
os.makedirs('data/raw/api', exist_ok=True)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename=LOG, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_api(url, name):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        out = f"data/raw/api/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(out, 'w') as f:
            json.dump(data, f, indent=2)
        logging.info(f"Ingested API {url} -> {out}")
        print('Ingested API to', out)
    except Exception as e:
        logging.exception('API ingest failed: %s', e)

if __name__ == '__main__':
    ingest_api('https://dummyjson.com/users', 'demographics')
