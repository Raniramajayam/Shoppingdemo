# Shopping Site Automation Framework
### Playwright + Python + Pytest | Page Object Model

End-to-end UI automation suite for an e-commerce site (target: https://automationexercise.com),
built to demonstrate real-world test architecture: Page Object Model, fixtures, data-driven
tests, parallel execution, and HTML/Allure reporting.

## Tech Stack
- Python 3.11+
- Playwright (sync API)
- Pytest + pytest-playwright + pytest-xdist (parallel) + pytest-html (reporting)
- Faker (test data generation)

## Setup
```bash
python -m venv venv
source venv/bin/activate          # venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install                # downloads browser binaries
```

## Run tests
```bash
pytest                                    # all tests, headless
pytest --headed                           # see the browser
pytest -m smoke                           # only smoke-tagged tests
pytest -n 4                               # 4 parallel workers
pytest --html=reports/report.html         # HTML report
```

## Project layout
See the folder-by-folder breakdown in the accompanying explanation.
