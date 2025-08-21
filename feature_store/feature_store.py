import json, os
os.makedirs('feature_store', exist_ok=True)
FEATURES = {
    'orders_last_30d': {'desc':'orders count last 30 days', 'source':'orders', 'version':1},
    'spend_last_90d': {'desc':'spend last 90 days', 'source':'orders', 'version':1},
}
with open('feature_store/metadata.json','w') as f:
    json.dump(FEATURES,f,indent=2)
print('Wrote feature metadata to feature_store/metadata.json')
