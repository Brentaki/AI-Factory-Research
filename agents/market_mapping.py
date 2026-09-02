from typing import Dict, Any, List
from core.capital_stack import STARGATE_CAPITAL_STACK, STARGATE_CAPEX_TOTAL
from core.schema import Company, SectorCategory


class MarketMappingAgent:
    """
    Market Mapping Agent:
    Maps AI Factory spend across infrastructure layers based on the reference Stargate capital stack.
    Assigns capital stack weights and categorizes companies by revenue monetization layer.
    """
    
    def __init__(self):
        self.capital_stack = STARGATE_CAPITAL_STACK
        self.total_budget = STARGATE_CAPEX_TOTAL

    def map_market_allocation(self) -> Dict[str, Any]:
        """Generates detailed market spend map across the 12 infrastructure layers."""
        sector_weights = {
            layer.category.value: {
                "stargate_millions": layer.stargate_allocation_millions,
                "percentage_share": layer.percentage_share,
                "key_equipment": layer.key_equipment
            }
            for layer in self.capital_stack
        }
        return {
            "total_budget_millions": self.total_budget,
            "sector_weights": sector_weights,
            "dominant_layer": SectorCategory.COMPUTE.value,
            "fastest_growing_infra_layers": [
                SectorCategory.NETWORKING.value,
                SectorCategory.CRAHS.value,
                SectorCategory.GAS_TURBINES.value,
                SectorCategory.UPS.value
            ]
        }

    def categorize_company(self, company: Company) -> Dict[str, Any]:
        """Maps a single company to its primary and secondary capital stack layers."""
        primary_layer = next(
            (layer for layer in self.capital_stack if layer.category == company.primary_sector),
            None
        )
        return {
            "ticker": company.ticker,
            "company_name": company.name,
            "primary_sector": company.primary_sector.value,
            "primary_layer_stargate_weight_pct": primary_layer.percentage_share if primary_layer else 0.0,
            "secondary_sectors": [sec.value for sec in company.secondary_sectors]
        }
