from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union

class BaseConnector(ABC):
    """
    Abstract Connector Base Contract.
    All SaaS plugins (Salesforce, Stripe, SAP) implement this interface.
    """

    def __init__(self, connector_name: str, config: Dict[str, Any]):
        self.connector_name = connector_name
        self.config = config

    @abstractmethod
    def authenticate(self) -> bool:
        """Authenticate with the target SaaS API."""
        pass

    @abstractmethod
    def fetch_records(self, entity_type: str, limit: int = 100) -> Dict[str, Any]:
        """Fetch records from the target SaaS platform."""
        pass

    @abstractmethod
    def write_record(self, entity_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Write or update record in the target SaaS platform."""
        pass
