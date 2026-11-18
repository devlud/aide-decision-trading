# Aide à la décision pour le trading

Un système d'aide à la décision pour le forex, construit sur MetaTrader 5 : télécharger
l'historique des prix, estimer la probabilité qu'un trade atteigne son objectif avant son stop,
juger le modèle hors échantillon et après coûts, puis envoyer les signaux sur Discord.
Les ordres restent passés à la main.

Projet en construction, un commit par étape.

> Projet personnel d'apprentissage : rien ici n'est un conseil en investissement.

## Installation

```bash
git clone https://github.com/devlud/aide-decision-trading.git
cd aide-decision-trading
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Licence

Code sous licence MIT.
