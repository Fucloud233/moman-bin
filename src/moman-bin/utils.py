from typing import Dict, Any
from pathlib import Path

import yaml


def read_yaml(file_path: Path) -> Dict:
    with open(file_path, "r", encoding="utf-8") as f:
        result = yaml.safe_load(f)

        return result


def write_yaml(file_path: Path, data: Dict[str, Any]):
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f)
