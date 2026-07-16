import os

class Config:
    """Central place for environment-specific values.
    In an interview: explain this avoids hardcoding URLs/timeouts across 20+ test files —
    change one value here to point the whole suite at staging vs prod.
    """
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT_MS", "10000"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
