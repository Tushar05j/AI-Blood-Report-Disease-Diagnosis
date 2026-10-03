# Flask Blood Report ML Demo
Educational interface for the project's existing Random Forest CBC classifier.

## Setup
1. Copy `random_forest_pipeline.joblib` from your trained project into this folder, beside `app.py`.
2. Open a terminal in this folder.
3. (Recommended) create and activate a virtual environment.
4. Install packages: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open `http://127.0.0.1:5000` in a browser.

The feature names in `app.py` must match the model training columns: WBC, RBC, HGB, PLT, NEUT, LYMPH, MONO, EOS, BASO. Confirm the numeric class-ID mapping and input units against your dataset/training code.

Educational prototype only; not a medical device or clinical diagnosis. Use synthetic or anonymized examples only. Flask debug server is local development only.
