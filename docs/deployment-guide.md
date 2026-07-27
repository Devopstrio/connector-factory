# Developer & Integration Guide: Connector Factory SDK

This guide covers local development, SDK installation, and custom plugin development for the Connector Factory framework.

## 1. Installation

```bash
# Clone repository
git clone https://github.com/Devopstrio/connector-factory.git
cd connector-factory

# Install in editable mode
pip install -e .
```

## 2. Usage Example

```python
from sdk.client import ConnectorFactoryClient

client = ConnectorFactoryClient()
sf = client.get_connector("salesforce", {"api_key": "your_api_key"})

if sf.authenticate():
    records = sf.fetch_records("Opportunity")
    print(records)
```

## 3. Running Pytest Suite

```bash
python -m pytest -v tests/
```
