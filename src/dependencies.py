from fastapi import Header, HTTPException
import os

async def get_token_header(x_token: str = Header(...)):
    if os.environ.get("AUTH_TOKEN") != x_token:
        raise HTTPException(status_code=400, detail="Require a valid token and provided x_token does not match")

