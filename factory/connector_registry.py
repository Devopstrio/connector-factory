from typing import Dict, Any, List, Optional, Union, Type
from factory.base_connector import BaseConnector

class ConnectorRegistry:
    """
    Dynamic Plugin Registry & Factory Loader.
    Registers connector plugin implementations and instantiates them dynamically by type name.
    """

    def __init__(self):
        self._registry: Dict[str, Type[BaseConnector]] = {}

    def register_connector(self, name: str, connector_cls: Type[BaseConnector]) -> None:
        self._registry[name.lower()] = connector_cls

    def create_connector(self, name: str, config: Dict[str, Any]) -> BaseConnector:
        cls = self._registry.get(name.lower())
        if not cls:
            raise ValueError(f"Unregistered connector plugin '{name}'. Available: {list(self._registry.keys())}")
        return cls(connector_name=name, config=config)

    def list_registered(self) -> List[str]:
        return list(self._registry.keys())
