import pytest
from factory.connector_registry import ConnectorRegistry
from plugins.salesforce_plugin import SalesforceConnector

def test_registry_registration():
    registry = ConnectorRegistry()
    registry.register_connector("salesforce", SalesforceConnector)
    assert "salesforce" in registry.list_registered()

def test_registry_creation():
    registry = ConnectorRegistry()
    registry.register_connector("salesforce", SalesforceConnector)
    sf = registry.create_connector("salesforce", {"api_key": "test"})
    assert sf.connector_name == "salesforce"

def test_registry_unregistered_raises():
    registry = ConnectorRegistry()
    with pytest.raises(ValueError):
        registry.create_connector("unknown", {})
