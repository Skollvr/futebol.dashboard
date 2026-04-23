from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
METADATA_DIR = DATA_DIR / "metadata"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)

DESIRED_METRICS = [
    "goals",
    "shots",
    "onTargetScoringAttempt",
    "fouls",
    "totalTackle",
    "wasFouled",
    "totalPass",
]

BROWSER_VIEWPORT = {"width": 1500, "height": 950}
DEFAULT_TIMEOUT_MS = 45000
EXTRA_WAIT_MS = 2000
