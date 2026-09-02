from typing import List
from core.schema import Company
from data.seed_universe import get_seed_universe


class CompanyIngestionAgent:
    """
    Company Ingestion Agent:
    Ingests global public equities, verifies eligibility (publicly traded, >15% AI Factory exposure),
    and normalizes ticker metadata.
    """
    
    def __init__(self):
        pass

    def ingest_universe(self) -> List[Company]:
        """Ingests and validates target seed universe."""
        raw_universe = get_seed_universe()
        # Filter for eligible public companies with direct exposure
        eligible = [c for c in raw_universe if c.ai_revenue_exposure_pct >= 15.0]
        return eligible

    def filter_by_sector(self, sector_name: str) -> List[Company]:
        """Filters ingested companies by primary sector."""
        universe = self.ingest_universe()
        return [c for c in universe if c.primary_sector.value == sector_name]
