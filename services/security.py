import hashlib

import bcrypt

class Securyti:
    def _password_hash(self, password: str) -> str:
        digest = self._password_digest(password)
        return bcrypt.hashpw(digest, bcrypt.gensalt())

    def _password_digest(self, password:str) -> bytes:
        return hashlib.sha256(password.encode("utf-8")).digest()


    def check_password(self, password: str, password_hash) -> bool:
        digest = self._password_digest(password)
        return bcrypt.checkpw(digest, password_hash)
        
security = Securyti()