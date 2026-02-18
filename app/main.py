from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.schemas import SeminarNeeds
from app.extractor import qualify_email
from app.config import OPENAI_MODEL
import json

app = FastAPI(title="Seminar Qualifier Agent", version="1.0.0")

class QualifyRequest(BaseModel):
    email_text: str = Field(..., min_length=10)

class QualifyBatchRequest(BaseModel):
    emails: list[QualifyRequest]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/qualify", response_model=SeminarNeeds)
def qualify(req: QualifyRequest):
    schema_json = json.dumps(SeminarNeeds.model_json_schema(), ensure_ascii=False)
    try:
        data = qualify_email(
            email_text=req.email_text,
            model_name=OPENAI_MODEL,
            schema_json=schema_json
        )
        # Validation forte via Pydantic:
        return SeminarNeeds.model_validate(data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Sortie IA non-JSON / invalide.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/qualify/batch", response_model=list[SeminarNeeds])
def qualify_batch(req: QualifyBatchRequest):
    schema_json = json.dumps(SeminarNeeds.model_json_schema(), ensure_ascii=False)
    out = []
    for item in req.emails:
        try:
            data = qualify_email(
                email_text=item.email_text,
                model_name=OPENAI_MODEL,
                schema_json=schema_json
            )
            out.append(SeminarNeeds.model_validate(data))
        except Exception as e:
            # En prod: renvoyer un statut partiel + erreurs par item
            raise HTTPException(status_code=500, detail=f"Erreur batch: {str(e)}")
    return out
