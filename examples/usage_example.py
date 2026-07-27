from sdk.client import ConnectorFactoryClient

def run_connector_example():
    client = ConnectorFactoryClient()
    print("Available connectors:", client.available_connectors())

    sf = client.get_connector("salesforce", {"api_key": "sf-secret-key"})
    if sf.authenticate():
        records = sf.fetch_records("Opportunity")
        print("Salesforce fetched records:", records)

    stripe = client.get_connector("stripe", {"stripe_secret": "sk_test_123"})
    if stripe.authenticate():
        charge = stripe.write_record("charge", {"amount": 2500})
        print("Stripe charge result:", charge)

if __name__ == "__main__":
    run_connector_example()
