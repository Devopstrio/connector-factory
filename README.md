<div align="center">

<img src="https://raw.githubusercontent.com/Devopstrio/.github/main/assets/Browser_logo.png" height="90" alt="Devopstrio Logo" />

# Connector Factory

### Dynamic SaaS Plugin Extensibility Framework & Python SDK

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=flat-square)](https://python.org)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square)](https://devopstrio.co.uk)

</div>

---

## 🚀 Quickstart

Install the package and instantiate SaaS connectors dynamically using the unified client SDK:

```python
from sdk.client import ConnectorFactoryClient

# Initialize SDK Client
client = ConnectorFactoryClient()

# List registered plugins
print("Available plugins:", client.available_connectors())

# Instantiate Salesforce Plugin
sf = client.get_connector("salesforce", {"api_key": "secret-key-123"})
if sf.authenticate():
    records = sf.fetch_records("Opportunity")
    print("Salesforce Records:", records)
```

---

## 🏛️ Architecture Overview

The **Connector Factory** decoupling architecture allows developers to build plug-and-play connectors for enterprise SaaS systems without altering core SDK logic.

![Connector Factory Architecture](docs/images/architecture_diagram.jpg)

```mermaid
flowchart TD
    Client[Developer SDK Client] -->|1. Request Connector Instance| Registry[Connector Registry Factory]
    Registry -->|2. Instantiate Plugin| Salesforce[Salesforce SaaS Plugin]
    Registry -->|3. Instantiate Plugin| Stripe[Stripe Financial Plugin]
    
    Salesforce --> Auth[OAuth2 / API Key Auth Manager]
    Stripe --> Auth
    
    Auth -->|4. Authenticated Request| TargetSaaS[Upstream SaaS API Platform]
```

---

## 🧪 Testing Suite

Run the automated test suite locally:

```bash
python -m pytest -v tests/
```

<div align="center">

<sub>&copy; 2026 Devopstrio &mdash; Engineering Uninterrupted Global Workforce Productivity.</sub>

</div>
