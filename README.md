# COVID-19 Impact Analysis Dashboard

An interactive Dash dashboard that visualizes COVID-19 trends and essential-supply availability by Indian state.

## Portfolio-ready highlights

- Built with **Dash + Plotly** for interactive analytics.
- Tracks **cases, recoveries, and deaths** by state.
- Includes supply views for **masks, sanitizers, and oxygen**.
- Uses a clean single-entry app (`app.py`) and CSV-driven data model.

## Tech Stack

- Python
- Dash
- Plotly
- Pandas
- NumPy
- Bootstrap 4 (via CDN)

## Repository Structure

```text
.
├── app.py
├── state_wise_daily data file IHHPET.csv
├── style.css
├── requirements.txt
└── README.md
```

## Local Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .venv\\Scripts\\activate  # Windows PowerShell
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:

   ```bash
   python app.py
   ```

4. Open in browser:

   `http://127.0.0.1:8050/`

## Notes

- The app reads data from `state_wise_daily data file IHHPET.csv` in the project root.
- Keep the CSV filename unchanged unless you also update the file path in `app.py`.

## Screenshot

![COVID-19 Dashboard](https://github.com/user-attachments/assets/0eec9859-1082-4887-b7e2-6dd8641ce411)
