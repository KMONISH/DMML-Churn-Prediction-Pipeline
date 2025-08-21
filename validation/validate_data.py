import os, pandas as pd, logging, csv
os.makedirs('reports', exist_ok=True)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/data_validation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_csv(path):
    issues = []
    try:
        df = pd.read_csv(path)
        if df.isnull().sum().sum() > 0:
            issues.append('missing_values')
        if df.duplicated().sum() > 0:
            issues.append('duplicates')
        logging.info(f"Validated {path}: rows={len(df)}, issues={issues}")
        return {'path': path, 'rows': len(df), 'issues': ';'.join(issues)}
    except Exception as e:
        logging.exception('Validation failed for %s: %s', path, e)
        return {'path': path, 'rows': 0, 'issues': 'error:'+str(e)}

if __name__ == '__main__':
    results = []
    files = [os.path.join('data/raw', f) for f in os.listdir('data/raw') if f.endswith('.csv')] if os.path.exists('data/raw') else []
    for f in files:
        results.append(validate_csv(f))
    with open('reports/data_quality_report.csv','w',newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['path','rows','issues'])
        w.writeheader()
        for r in results:
            w.writerow(r)
    print('Validation complete. Report: reports/data_quality_report.csv')
