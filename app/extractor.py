import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

SYSTEM_PROMPT = """
Tu es un agent de qualification commerciale spécialisé dans les séminaires d'entreprise.
Tu reçois un email client. Ta mission :
1) Extraire les besoins et contraintes.
2) Identifier ce qui manque pour finaliser une proposition.
3) Produire une sortie STRICTEMENT en JSON valide, sans texte autour.

Règles:
- Ne rien inventer: si une info n'est pas mentionnée, mets null ou liste vide.
- Les champs numeriques: budget_eur_min/max entiers ou null.
- preferred_dates: liste de strings (même si vague: "mi-mars", "Semaine du 12").
- format ∈ ["in_person","remote","hybrid","unknown"]
- intent ∈ ["request_quote","request_info","change_request","complaint","other"]
- urgency ∈ ["low","medium","high"]
- confidence entre 0 et 1.
"""

USER_PROMPT = """
EMAIL:
{email_text}

Retourne uniquement un JSON respectant exactement ce schéma (mêmes clés):
{schema_json}
"""

def build_chain(model_name: str, temperature: float = 0.2):
    llm = ChatOpenAI(model=model_name, temperature=temperature)
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", USER_PROMPT),
    ])
    return prompt | llm | StrOutputParser()

def safe_json_load(s: str) -> dict:
    # Nettoyage minimal si le modèle renvoie des backticks (on évite mais on protège)
    s = s.strip()
    if s.startswith("```"):
        s = s.strip("`")
        # parfois "json\n{...}"
        if "\n" in s:
            s = s.split("\n", 1)[1]
    return json.loads(s)

def qualify_email(email_text: str, model_name: str, schema_json: str) -> dict:
    chain = build_chain(model_name=model_name)
    raw = chain.invoke({"email_text": email_text, "schema_json": schema_json})
    return safe_json_load(raw)
