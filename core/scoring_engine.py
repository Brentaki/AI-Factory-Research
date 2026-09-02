from core.schema import (
    MoatDetail, OperatingMarginDetail, GrowthDetail, RiskDetail, TAFGSEvaluation, SectorCategory
)


def normalize_operating_margin(operating_margin_pct: float) -> int:
    """
    Normalizes actual operating margin percentage into a 1 to 5 score:
    - > 40%: 5
    - 30% - 40%: 4
    - 20% - 30%: 3
    - 10% - 20%: 2
    - < 10%: 1
    """
    if operating_margin_pct >= 40.0:
        return 5
    elif operating_margin_pct >= 30.0:
        return 4
    elif operating_margin_pct >= 20.0:
        return 3
    elif operating_margin_pct >= 10.0:
        return 2
    else:
        return 1


def compute_tafgs_evaluation(
    ticker: str,
    company_name: str,
    primary_sector: SectorCategory,
    secondary_sectors: list,
    moat_score: float,
    moat_rationale: str,
    architectural_lockin: bool,
    ecosystem_dominance: bool,
    switching_cost_rating: str,
    bottleneck_position: bool,
    actual_operating_margin_pct: float,
    margin_expansion_3yr: float,
    pricing_power_rating: str,
    margin_rationale: str,
    ai_revenue_exposure_pct: float,
    forecast_3yr_cagr_pct: float,
    order_backlog_growth_pct: float,
    key_catalysts: list,
    product_cycle_drivers: list,
    execution_risk: float = 0.05,
    customer_concentration_risk: float = 0.05,
    cyclicality_risk: float = 0.05,
    risk_summary: str = "Standard execution and supply chain risks."
) -> TAFGSEvaluation:
    """
    Computes the Total AI Factory Growth Score (TAFGS) using the formula:
    TAFGS = (Moat Score * Operating Margin Score) * Forecast AI Growth CAGR %
    Adjusted by: Risk Discount Factor (1 - Risk Discount)
    """
    # 1. Normalize Operating Margin Score (1-5)
    margin_score = normalize_operating_margin(actual_operating_margin_pct)
    
    margin_detail = OperatingMarginDetail(
        actual_operating_margin_pct=actual_operating_margin_pct,
        score=margin_score,
        margin_expansion_3yr=margin_expansion_3yr,
        pricing_power_rating=pricing_power_rating,
        rationale=margin_rationale
    )
    
    # 2. Build Moat Detail (0-5)
    moat_detail = MoatDetail(
        score=min(max(moat_score, 0.0), 5.0),
        architectural_lockin=architectural_lockin,
        ecosystem_dominance=ecosystem_dominance,
        switching_cost_rating=switching_cost_rating,
        bottleneck_position=bottleneck_position,
        rationale=moat_rationale
    )
    
    # 3. Build Growth Detail
    growth_detail = GrowthDetail(
        ai_revenue_exposure_pct=ai_revenue_exposure_pct,
        forecast_3yr_cagr_pct=forecast_3yr_cagr_pct,
        order_backlog_growth_pct=order_backlog_growth_pct,
        key_catalysts=key_catalysts,
        product_cycle_drivers=product_cycle_drivers
    )
    
    # 4. Compute Risk Discount
    total_risk_discount = min(execution_risk + customer_concentration_risk + cyclicality_risk, 0.30)
    risk_detail = RiskDetail(
        execution_risk=execution_risk,
        customer_concentration_risk=customer_concentration_risk,
        cyclicality_risk=cyclicality_risk,
        total_risk_discount_pct=round(total_risk_discount, 4),
        risk_summary=risk_summary
    )
    
    # 5. Core TAFGS Calculations
    raw_tafgs = round((moat_detail.score * margin_detail.score) * growth_detail.forecast_3yr_cagr_pct, 2)
    risk_adjusted_tafgs = round(raw_tafgs * (1.0 - total_risk_discount), 2)
    
    return TAFGSEvaluation(
        ticker=ticker,
        company_name=company_name,
        primary_sector=primary_sector,
        secondary_sectors=secondary_sectors,
        moat=moat_detail,
        margin=margin_detail,
        growth=growth_detail,
        risk=risk_detail,
        raw_tafgs=raw_tafgs,
        risk_adjusted_tafgs=risk_adjusted_tafgs
    )
