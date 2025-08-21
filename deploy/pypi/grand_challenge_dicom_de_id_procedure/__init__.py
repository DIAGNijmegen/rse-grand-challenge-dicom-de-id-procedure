import json
from pathlib import Path

script_dir = Path(__file__).resolve().parent

with open(script_dir / "procedure.json", "r") as f:
    procedure = json.load(f)
