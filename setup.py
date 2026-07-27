from setuptools import setup, find_packages

setup(
    name="connector-factory",
    version="1.0.0",
    description="Enterprise Dynamic SaaS Connector Factory & Plugin Registry SDK",
    author="Devopstrio",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.5.0",
        "httpx>=0.26.0",
        "pyyaml>=6.0.1",
        "structlog>=24.1.0"
    ],
    python_requires=">=3.9",
)
