from trading.config import DATA_DIR, RACINE


def test_racine_est_le_dossier_du_projet():
    # Si config.py changeait de place, RACINE pointerait ailleurs : on vérifie
    # qu'elle désigne bien le dossier qui contient pyproject.toml.
    assert (RACINE / "pyproject.toml").exists()
    assert DATA_DIR == RACINE / "data"


def test_donnees_et_secrets_jamais_sur_github():
    # Dépôt public : les données du broker et les secrets doivent rester hors de Git.
    # Si ces lignes disparaissaient du .gitignore, ce test échouerait.
    lignes = (RACINE / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert "data/" in lignes
    assert ".env" in lignes
