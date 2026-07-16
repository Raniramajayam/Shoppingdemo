# 🏗️ PROJECT ARCHITECTURE & FOLDER STRUCTURE EXPLAINED

> **For every folder, we explain: WHAT IS IT? WHY DO WE NEED IT? WHAT GOES IN IT?**

---

## 📂 COMPLETE FOLDER STRUCTURE

```
shopping-automation/                    ← Root folder (your project)
│
├── .github/                           ← GitHub-specific configuration
│   └── workflows/
│       └── playwright.yml             ← CI/CD Pipeline definition (GitHub Actions)
│
├── pages/                             ← Page Object Model (POM)
│   ├── __init__.py                   ← Makes this folder a Python package
│   ├── base_page.py                  ← Parent class for all pages
│   ├── home_page.py                  ← Homepage actions
│   ├── search_page.py                ← Search results actions
│   ├── cart_page.py                  ← Shopping cart actions
│   └── checkout_page.py              ← Checkout flow actions
│
├── tests/                            ← Test files (actual tests)
│   ├── __init__.py                  ← Makes this a package
│   ├── test_add_to_cart.py          ← Tests for cart functionality
│   ├── test_checkout.py             ← Tests for checkout flow
│   ├── test_search.py               ← Tests for search functionality
│   └── __pycache__/                 ← Auto-generated (compiled Python files)
│
├── utils/                           ← Utility functions & configuration
│   ├── __init__.py
│   ├── config.py                    ← Environment configuration (URLs, timeouts)
│   ├── logger.py                    ← Logging setup
│   └── __pycache__/
│
├── data/                            ← Test data
│   └── test_data.json               ← Test datasets (usernames, products, etc.)
│
├── .git/                            ← Git repository (hidden folder)
│   └── [Version history, commits, branches]
│
├── .gitignore                       ← Tells Git what to ignore (WE JUST CREATED)
├── .pytest_cache/                   ← Pytest cache (auto-generated, ignored)
├── conftest.py                      ← Pytest fixtures & hooks
├── pytest.ini                       ← Pytest configuration
├── requirements.txt                 ← Python dependencies
├── README.md                        ← Project documentation
├── LEARNING_GUIDE.md               ← This tutorial (WE JUST CREATED)
└── reports/                         ← Test execution reports (auto-generated)
    └── report.html                  ← HTML test report
```

---

## 🎯 WHAT EACH FOLDER DOES

### 1. **`.github/workflows/`** - GitHub Actions Configuration

**WHAT IS IT?**
This folder tells GitHub how to run your tests automatically.

**WHY?**
Without this, you'd manually run tests every time someone pushes code. With this, GitHub automatically:
- Pulls your code
- Sets up a virtual machine
- Installs dependencies
- Runs tests
- Generates reports
- Sends results back to you

**INSIDE:**
```
.github/workflows/playwright.yml

name: Playwright Tests                 ← What GitHub shows in the UI

on:
  push:                               ← Run on every push
  pull_request:                       ← Run on every PR
  schedule:                           ← Run on schedule (like a cron job)

jobs:
  test:                               ← Define jobs
    runs-on: ubuntu-latest            ← Use Ubuntu virtual machine
    steps:                            ← Steps to execute
      - uses: actions/checkout@v4     ← Clone your repo
      - uses: actions/setup-python    ← Install Python
      - run: pytest                   ← Run tests
      - uses: actions/upload-artifact ← Save reports
```

**In STEP 4, we'll explain every line.**

---

### 2. **`pages/`** - Page Object Model (POM)

**WHAT IS IT?**
Separates test logic from UI interactions. Each page = one class.

**WHY?**
If the website redesigns, you only update one file per page, not 50 test files.

**STRUCTURE:**
```
base_page.py
  ↓
  Common methods (click, fill, wait, etc.)
  ↓
Inherited by home_page.py, search_page.py, etc.
```

**EXAMPLE:**
```python
# Instead of this scattered everywhere:
page.click("[class='add-to-cart']")
page.fill("[name='quantity']", "2")
page.click("[type='button']")

# We do this in search_page.py:
def add_first_result_to_cart(self):
    self.click("[class='add-to-cart']")
    self.fill("[name='quantity']", "2")
    self.click("[type='button']")

# And in tests, we call:
search_page.add_first_result_to_cart()  ← Readable!
```

**Interview Answer:**
> "Page Object Model separates concerns. Page classes encapsulate UI details. Tests become readable and maintainable. If the UI changes, we update one place."

---

### 3. **`tests/`** - Test Files

**WHAT IS IT?**
The actual test cases. This is what runs on GitHub Actions.

**WHY?**
Organizes tests by feature (cart, checkout, search).

**STRUCTURE:**
```
test_add_to_cart.py
  - test_add_single_product_to_cart()
  - test_add_multiple_products_to_cart()
  - test_remove_item_from_cart()

test_checkout.py
  - test_checkout_with_valid_data()
  - test_checkout_missing_address()
  - etc.

test_search.py
  - test_search_by_name()
  - test_search_by_category()
  - etc.
```

**KEY CONCEPT: Pytest Fixtures**
```python
# conftest.py defines reusable fixtures:
@pytest.fixture(scope="function")
def home_page(page):
    home = HomePage(page)
    home.load()
    return home

# Tests use them:
def test_add_to_cart(home_page, search_page):  ← Fixtures injected
    home_page.search_product("Dress")
    assert search_page.get_results_count() > 0
```

**Interview Answer:**
> "Fixtures are setup/teardown on steroids. They're reusable and reduce duplication. Function-scoped fixtures run before each test, ensuring isolation."

---

### 4. **`utils/`** - Utilities & Configuration

**WHAT IS IT?**
Shared code that multiple components use.

**config.py:**
```python
class Config:
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT_MS", "10000"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
```

**WHY?**
- Don't hardcode URLs in tests
- Change environment in one place
- Use environment variables for different environments (dev, staging, prod)

**logger.py:**
```python
def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```

**WHY?**
- Debugging: see what happened at each test step
- CI/CD: logs appear in GitHub Actions output
- Production: audit trail of who accessed what when

---

### 5. **`data/`** - Test Data

**WHAT IS IT?**
Test datasets (products to search, user credentials, etc.)

**WHY?**
- Data-driven testing: same test, different inputs
- Centralize test data
- Easy to update without touching code

**EXAMPLE:**
```json
{
  "products": [
    {"name": "Dress", "category": "women"},
    {"name": "Top", "category": "women"}
  ],
  "users": [
    {"email": "test@example.com", "password": "123456"}
  ]
}
```

---

### 6. **`conftest.py`** - Pytest Configuration & Fixtures

**WHAT IS IT?**
Central configuration for all pytest runs.

**KEY SECTIONS:**

```python
@pytest.fixture(scope="session")
def playwright_instance():
    """ONE browser process for entire session (expensive, do once)"""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def context(browser):
    """FRESH context per test (isolated cookies, storage, cache)"""
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    yield context
    context.close()  ← Cleanup after each test

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Auto-capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/failure_{item.name}.png"
            page.screenshot(path=screenshot_path)
```

**Interview Answer:**
> "Fixtures provide test setup and teardown. Scope controls lifecycle: session (once per run), function (before/after each test). Hooks allow custom behavior like auto-screenshot on failure."

---

### 7. **`pytest.ini`** - Pytest Configuration

**WHAT IS IT?**
Settings for pytest behavior.

```ini
[pytest]
markers =
    smoke: quick critical-path tests      ← Mark tests for category
    regression: full regression suite
    cart: cart-related tests

addopts = -v --tb=short --html=reports/report.html --self-contained-html
├─ -v          : Verbose output
├─ --tb=short  : Shorter error traces
├─ --html=...  : Generate HTML report
└─ --self-contained-html : Make HTML standalone (no external files)

testpaths = tests               ← Look for tests in this folder
```

---

### 8. **`requirements.txt`** - Python Dependencies

**WHAT IS IT?**
List of Python packages needed to run this project.

```
playwright==1.47.0           ← Browser automation library
pytest==8.3.3                ← Test framework
pytest-playwright==0.5.2     ← Pytest + Playwright integration
pytest-xdist==3.6.1         ← Parallel test execution (-n 4)
pytest-html==4.1.1          ← HTML test reports
faker==28.4.1               ← Generate fake test data
python-dotenv==1.0.1        ← Load .env files for secrets
```

**HOW TO USE:**
```powershell
pip install -r requirements.txt     # Install all packages
pip freeze > requirements.txt        # Generate requirements.txt
```

---

### 9. **`README.md`** - Project Documentation

**WHAT IS IT?**
First thing developers read. Setup instructions, quick-start guide.

**SHOULD INCLUDE:**
- What is this project?
- How to set it up?
- How to run tests?
- How to run tests in parallel?
- How to view reports?
- Tech stack
- Contributing guide

---

## 🔗 HOW EVERYTHING CONNECTS

```
1. Developer writes test in tests/test_add_to_cart.py
                    ↓
2. Test calls methods from pages/search_page.py
                    ↓
3. Pages call methods from pages/base_page.py
                    ↓
4. Base page uses Playwright to interact with real browser
                    ↓
5. Test result captured, screenshot taken if failed
                    ↓
6. Developer commits to Git (we'll do this in STEP 2)
                    ↓
7. Pushes to GitHub (STEP 3)
                    ↓
8. GitHub Actions sees the push (STEP 4)
                    ↓
9. Runs .github/workflows/playwright.yml
                    ↓
10. installs dependencies from requirements.txt
                    ↓
11. Runs pytest which loads conftest.py fixtures
                    ↓
12. pytest.ini applies markers and settings
                    ↓
13. Generates HTML report in reports/
                    ↓
14. Uploads artifacts to GitHub (visible in Actions tab)
                    ↓
15. Notifies developer: "All tests passed! ✅"
    or "Tests failed! See report." ❌
```

---

## ✅ YOU NOW UNDERSTAND

- What each folder contains
- Why they're organized this way
- How they interact
- Interview answers for each component

**NEXT:** Commit all these files to Git!


