from sdk.client import ConnectorFactoryClient

def test_sdk_client():
    client = ConnectorFactoryClient()
    available = client.available_connectors()
    assert "salesforce" in available
    assert "stripe" in available

    sf = client.get_connector("salesforce", {"api_key": "valid"})
    assert sf.authenticate() is True
    records = sf.fetch_records("Account")
    assert records["records_count"] == 2

    stripe = client.get_connector("stripe", {"stripe_secret": "valid"})
    assert stripe.authenticate() is True
    charge = stripe.write_record("charge", {"amount": 100})
    assert charge["status"] == "CHARGE_CREATED"
