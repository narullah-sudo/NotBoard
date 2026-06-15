
from fastapi import Request
import secrets
import hashlib

class Sessions:
    def hash_token(self, token: str) -> str:
        return hashlib.sha256(token.encode("utf-8")).hexdigest()

    def create_session_token(self) -> tuple[str, str]:
        token = secrets.token_urlsafe(32)
        return token, self.hash_token(token)

session_man = Sessions()