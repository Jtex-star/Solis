"""
SOLIS Data Ingestion Module v1.0.0
====================================

Production-grade ETL pipeline for financial data collection.

Supports:
- Stocks (Alpha Vantage, Yahoo Finance)
- Crypto (CoinGecko)
- Commodities (Polygon.io)
- Real-time streaming (Kafka)
- S3 storage with partitioning

Author: SOLIS Team
Date: 2025-01-21
License: MIT
"""

from .data_ingestion import DataIngestionPipeline
from .config import DataIngestionConfig

__version__ = "1.0.0"
__all__ = ["DataIngestionPipeline", "DataIngestionConfig"]
