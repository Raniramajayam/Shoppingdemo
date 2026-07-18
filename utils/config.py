import os

class Config:
    """Central place for environment-specific values.
    In an interview: explain this avoids hardcoding URLs/timeouts across 20+ test files —
    change one value here to point the whole suite at staging vs prod.
    """
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
    # Increase default timeout to 20s to be more stable on CI runners
    DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT_MS", "20000"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
