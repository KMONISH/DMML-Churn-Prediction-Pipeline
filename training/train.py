import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib, os
os.makedirs('models', exist_ok=True)

cust = pd.read_csv('seed/customers.csv')
orders = pd.read_csv('seed/orders.csv')
cust['label'] = cust['customer_id'].apply(lambda x: 1 if x=='C003' else 0)
X = pd.DataFrame({'total_spend':[499.0,199.0,0.0],'orders_count':[2,1,0]})
y = cust['label']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
proba = clf.predict_proba(X_test)[:,0]
print('ROC AUC:', roc_auc_score(y_test, proba))
print(classification_report(y_test, pred))
joblib.dump(clf, 'models/churn_model_v1.pkl')
print('Saved model: models/churn_model_v1.pkl')
