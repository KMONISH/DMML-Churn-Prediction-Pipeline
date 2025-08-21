import pandas as pd, joblib, os
model_path = 'models/churn_model_v1.pkl'
if not os.path.exists(model_path):
    print('Model not found. Train first: python training/train.py')
    exit(1)
model = joblib.load(model_path)
X = pd.DataFrame({'total_spend':[499.0,199.0,0.0],'orders_count':[2,1,0]})
pred = model.predict_proba(X)[:,0]
out = pd.DataFrame({'customer_id':['C001','C002','C003'],'churn_prob':pred})
os.makedirs('predictions', exist_ok=True)
out.to_csv('predictions/predictions.csv', index=False)
print('Wrote predictions/predictions.csv')
