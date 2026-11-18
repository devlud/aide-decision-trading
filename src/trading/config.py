"""Réglages du projet, regroupés en un seul endroit."""

from pathlib import Path

# Dossier racine du projet, calculé à partir de l'emplacement de ce fichier :
# config.py est dans src/trading/, on remonte donc de deux dossiers.
# Ainsi, les chemins restent justes d'où que l'on lance le code : terminal, notebook, VS Code.
RACINE = Path(__file__).resolve().parents[2]

# Dossier des données (exclu de Git par le .gitignore). Ses sous-dossiers (bougies,
# résultats des backtests...) seront ajoutés au fil des étapes.
DATA_DIR = RACINE / "data"
