from factory.auth_manager import AuthManager

def test_auth_manager_issue_token():
    auth = AuthManager()
    token_meta = auth.issue_token("client_a", "secret_a", ttl_seconds=100)
    assert "access_token" in token_meta
    assert auth.get_valid_token("client_a") == token_meta["access_token"]

def test_auth_manager_invalid():
    auth = AuthManager()
    assert auth.get_valid_token("unknown_client") is None
