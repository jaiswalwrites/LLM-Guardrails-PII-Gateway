import re
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PII Gateway Proxy")

class RequestPayload(BaseModel):
    user_prompt: str

@app.post("/guardrails/sanitize")
async def sanitize_prompt(payload: RequestPayload):
    text = payload.user_prompt
    text = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[MASKED_EMAIL]", text)
    return {"sanitized_prompt": text}

if __name__ == "__main__":
    pass
