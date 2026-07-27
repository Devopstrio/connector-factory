from typing import Dict, Any, List, Optional, Union
from factory.connector_registry import ConnectorRegistry
from factory.base_connector import BaseConnector
from plugins.salesforce_plugin import SalesforceConnector
from plugins.stripe_plugin import StripeConnector

class ConnectorFactoryClient:
    """
    High-Level Developer SDK Client for Connector Factory.
    """

    def __init__(self):
        self.registry = ConnectorRegistry()
        # Default plugin auto-registration
        self.registry.register_connector("salesforce", SalesforceConnector)
        self.registry.register_connector("stripe", StripeConnector)

    def get_connector(self, name: str, config: Dict[str, Any]) -> BaseConnector:
        return self.registry.create_connector(name, config)

    def available_connectors(self) -> List[str]:
        return self.registry.list_registered()
