from typing import Dict, Any, List, Optional, Union
import time

class AuthManager:
    """
    Dynamic OAuth2 & API Key Token Manager.
    Manages client credentials, bearer token refresh cycles, and API key authentication headers.
    """

    def __init__(self):
        self._tokens: Dict[str, Dict[str, Any]] = {}

    def issue_token(self, client_id: str, client_secret: str, ttl_seconds: int = 3600) -> Dict[str, Any]:
        access_token = f"tok_cf_{hash(client_id + client_secret) & 0xffffffff:08x}"
        expiry = time.time() + ttl_seconds

        token_meta = {
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_at": expiry,
            "ttl_seconds": ttl_seconds
        }
        self._tokens[client_id] = token_meta
        return token_meta

    def get_valid_token(self, client_id: str) -> Optional[str]:
        meta = self._tokens.get(client_id)
        if not meta:
            return None
        if time.time() > meta["expires_at"]:
            return None  # Expired
        return meta["access_token"]
