.PHONY: ingest validate prepare train score clean zip
ingest:
	python ingestion/ingest_csv.py

validate:
	python validation/validate_data.py

prepare:
	python preparation/prepare_data.py

train:
	python training/train.py

score:
	python scoring/score_batch.py

clean:
	rm -rf data logs models predictions

zip:
	python -c "import shutil; shutil.make_archive('churn_pipeline_repo','zip','.')"
