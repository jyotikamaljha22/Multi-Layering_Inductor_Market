# Global Multilayer Inductor Market Streamlit App

## Files
- `app.py` — full production-ready Streamlit dashboard with all 20 chapters preserved from the supplied HTML.
- `requirements.txt` — deployment-safe dependencies, including `openpyxl`.
- `.streamlit/config.toml` — premium burgundy theme.
- `client_tracking.db` — created automatically at runtime for local login and chapter-view tracking.

## Local run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud deployment
1. Create a GitHub repo and upload the folder contents.
2. In Streamlit Community Cloud, point the app to `app.py`.
3. Add these secrets in the app settings:
```toml
APP_USERNAME = "your_username"
APP_PASSWORD = "your_password"
APP_CLIENT_NAME = "TDK Corporation"
```

## Why `openpyxl` is included
A common Streamlit Cloud issue is `ModuleNotFoundError: openpyxl` when future workbook loading is added. Including it in `requirements.txt` fixes that dependency upfront.

## Client tracking layer
The app includes a lightweight SQLite tracker for:
- login success / failure
- chapter views
- logout events

For enterprise deployment, swap SQLite for Postgres, Supabase, or Snowflake.
