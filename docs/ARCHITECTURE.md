# Connector Factory SDK Architecture

The **Connector Factory Python SDK** provides a plugin extensibility framework, dynamic connector registry, OAuth2 token lifecycle manager, and unified client interface across enterprise SaaS platforms.

![Connector Factory Architecture](images/architecture_diagram.jpg)

## Component Sequence Diagram

```mermaid
flowchart TD
    Client[Developer SDK Client] -->|1. Request Connector Instance| Registry[Connector Registry Factory]
    Registry -->|2. Instantiate Plugin| Salesforce[Salesforce SaaS Plugin]
    Registry -->|3. Instantiate Plugin| Stripe[Stripe Financial Plugin]
    
    Salesforce --> Auth[OAuth2 / API Key Auth Manager]
    Stripe --> Auth
    
    Auth -->|4. Authenticated Request| TargetSaaS[Upstream SaaS API Platform]
```

## Core Modules

1. **Connector Registry (`factory/connector_registry.py`)**
   - Dynamic plugin factory that maintains a registry of plugin classes and instantiates them on demand.

2. **Base Connector Interface (`factory/base_connector.py`)**
   - Abstract base contract establishing mandatory authentication and CRUD methods (`authenticate`, `fetch_records`, `write_record`).

3. **Authentication Manager (`factory/auth_manager.py`)**
   - Handles client credentials, token generation, and automatic expiration cycles.
