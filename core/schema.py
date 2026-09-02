from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SectorCategory(str, Enum):
    COMPUTE = "Compute / Servers"
    NETWORKING = "Networking"
    GAS_TURBINES = "Gas Turbines"
    GENERATORS = "Generators"
    UPS = "UPS (Uninterruptible Power)"
    SWITCHGEAR = "Switchgear"
    CHILLERS = "Chillers"
    CRAHS = "CRAHs (Computer Room Air Handlers)"
    CRAHs = "CRAHs (Computer Room Air Handlers)"
    PDUS_BUSWAY = "PDUs & Busway"
    COOLING_TOWERS = "Cooling Towers"
    CONSTRUCTION = "Construction"
    ENGINEERING = "Engineering"


class CapitalStackLayer(BaseModel):
    category: SectorCategory
    stargate_allocation_millions: float
    percentage_share: float
    description: str
    key_equipment: List[str]
    representative_companies: List[str]


class MoatDetail(BaseModel):
    score: float = Field(..., ge=0.0, le=5.0, description="Moat Score from 0 to 5")
    architectural_lockin: bool = False
    ecosystem_dominance: bool = False
    switching_cost_rating: str  # High, Medium, Low
    bottleneck_position: bool = False
    rationale: str


class OperatingMarginDetail(BaseModel):
    actual_operating_margin_pct: float
    score: int = Field(..., ge=1, le=5, description="Normalized Margin Score 1 to 5")
    margin_expansion_3yr: float  # Percentage points change over 3 years
    pricing_power_rating: str
    rationale: str


class GrowthDetail(BaseModel):
    ai_revenue_exposure_pct: float
    forecast_3yr_cagr_pct: float
    order_backlog_growth_pct: float
    key_catalysts: List[str]
    product_cycle_drivers: List[str]


class RiskDetail(BaseModel):
    execution_risk: float = Field(default=0.05, ge=0.0, le=0.15)
    customer_concentration_risk: float = Field(default=0.05, ge=0.0, le=0.15)
    cyclicality_risk: float = Field(default=0.05, ge=0.0, le=0.15)
    total_risk_discount_pct: float = Field(default=0.10, ge=0.0, le=0.30)
    risk_summary: str


class TAFGSEvaluation(BaseModel):
    ticker: str
    company_name: str
    primary_sector: SectorCategory
    secondary_sectors: List[SectorCategory] = []
    
    # Core Formula Inputs
    moat: MoatDetail
    margin: OperatingMarginDetail
    growth: GrowthDetail
    risk: RiskDetail
    
    # Mathematical Outputs
    raw_tafgs: float  # (Moat Score * Margin Score) * Growth CAGR%
    risk_adjusted_tafgs: float  # Raw TAFGS * (1 - Risk Discount)
    rank: Optional[int] = None


class Company(BaseModel):
    ticker: str
    name: str
    market_cap_billions: float
    primary_sector: SectorCategory
    secondary_sectors: List[SectorCategory] = []
    ai_revenue_exposure_pct: float
    actual_operating_margin_pct: float
    order_backlog_growth_pct: float
    moat_qualitative: str
    growth_catalysts: List[str]
    risk_factors: List[str]


class CompanyProfile(BaseModel):
    company: Company
    evaluation: TAFGSEvaluation
    thesis_narrative: str
    catalyst_timeline_2026_2029: List[str]


class Top20Ranking(BaseModel):
    timestamp: str
    total_universe_scanned: int
    top_20: List[TAFGSEvaluation]
    sector_distribution: Dict[str, int]
