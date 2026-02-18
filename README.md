
# 📌 README – Agent IA de Qualification de Séminaires

```markdown
# 🤖 Agent IA de Qualification de Séminaires

Agent intelligent permettant d’analyser automatiquement des e-mails clients
et d’extraire les besoins liés à l’organisation de séminaires d’entreprise.

Le projet combine :
- 🧠 LLM (OpenAI via LangChain)
- ⚡ FastAPI
- 📦 Pydantic (validation forte)
- 🔐 Architecture prête pour intégration interne

---

## 🎯 Objectif

Automatiser la qualification commerciale des demandes de séminaires
afin de :

- Structurer les besoins clients
- Identifier les informations manquantes
- Générer une fiche exploitable par les équipes commerciales
- Réduire le temps de traitement manuel

---

## 🏗 Architecture

Email brut  
⬇  
Agent LLM (LangChain + OpenAI)  
⬇  
Extraction structurée JSON  
⬇  
Validation Pydantic  
⬇  
API FastAPI  

---

## 📁 Structure du projet

```


Projet-Agent-IA-de-Qualification-de-S-minaires
/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── extractor.py
│   └── **init**.py
│
├── requirements.txt
├── .env.example
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/ton-repo/seminar_qualifier_agent.git
cd seminar_qualifier_agent
````

---

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv .venv
```

### Windows :

```bash
.venv\Scripts\activate
```

---

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurer les variables d’environnement

Créer un fichier `.env` :

```
OPENAI_API_KEY=sk-xxxx
OPENAI_MODEL=gpt-4o-mini
```

---

## 🚀 Lancer l’API

```bash
python -m uvicorn app.main:app --reload
```

Accéder à la documentation interactive :

```
http://127.0.0.1:8000/docs
```

---

## 📬 Endpoint principal

### POST `/qualify`

Analyse un e-mail et retourne une fiche de qualification structurée.

### Exemple de requête :

```json
{
  "email_text": "Bonjour, nous souhaitons organiser un séminaire à Lyon fin mars pour 40 personnes. Budget autour de 15k€. Objectif : team building et stratégie."
}
```

### Exemple de réponse :

```json
{
  "summary": "...",
  "intent": "request_quote",
  "urgency": "medium",
  "participants_count": 40,
  "preferred_dates": ["fin mars"],
  "objectives": ["team building", "stratégie"],
  "missing_information": [
    "dates exactes",
    "format (présentiel/distanciel)",
    "profil des participants"
  ],
  "recommended_next_action": "Proposer un call de 15 minutes pour affiner le besoin.",
  "confidence": 0.87
}
```

---

## 🧠 Fonctionnement de l’agent

L’agent :

1. Analyse l’e-mail client
2. Identifie :

   * Objectifs
   * Budget
   * Format
   * Participants
   * Contraintes
3. Détecte les informations manquantes
4. Propose une action commerciale
5. Génère un score de confiance

La sortie est strictement validée par Pydantic.

---

## 🔐 Sécurité & Bonnes pratiques

* Validation stricte des données
* Température faible (0.2) pour stabilité
* JSON strict (pas de texte parasite)
* Architecture prête pour ajout :

  * Auth API key
  * Logs
  * Base PostgreSQL
  * Monitoring

---

## 📈 Améliorations possibles

* Intégration Gmail API
* Stockage PostgreSQL des demandes
* Dashboard commercial
* Scoring priorisation automatique
* Mode batch
* Génération automatique d’email de réponse

---

## 🧪 Cas d’usage

* Agence événementielle
* Service commercial B2B
* Centre de formation
* Organisateur de séminaires
* Cabinet de conseil

---

## 🛠 Stack technique

* Python 3.10+
* FastAPI
* LangChain
* OpenAI API
* Pydantic v2
* Uvicorn

---

## 👨‍💻 Auteur

Projet personnel développé dans le cadre d’une montée en compétences
en Data Engineering & AI Systems.

---

## 📄 Licence

MIT

```

---

```

