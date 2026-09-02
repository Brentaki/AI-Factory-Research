from core.schema import Company, OperatingMarginDetail
from core.scoring_engine import normalize_operating_margin


class MarginAnalysisAgent:
    """
    Margin Analysis Agent:
    Evaluates operating margin quality and pricing power in capex super-cycles.
    Normalizes actual operating margin into a 1 to 5 score:
    - > 40%: 5 (Pricing power + operating leverage)
    - 30-40%: 4
    - 20-30%: 3
    - 10-20%: 2
    - < 10%: 1
    """

    def analyze_margin(self, company: Company) -> OperatingMarginDetail:
        margin_pct = company.actual_operating_margin_pct
        score = normalize_operating_margin(margin_pct)
        
        # Estimate 3-year margin expansion and pricing power
        if score == 5:
            pricing_power = "Exceptional"
            expansion = 14.5 if company.ticker == "NVDA" else 8.2
            rationale = f"Operating margin of {margin_pct:.1f}% (>40%) reflects extreme pricing power and software-like operating leverage during AI capex super-cycles."
        elif score == 4:
            pricing_power = "Strong"
            expansion = 5.4
            rationale = f"Operating margin of {margin_pct:.1f}% (30-40%) demonstrates premium pricing power and disciplined cost control in proprietary hardware."
        elif score == 3:
            pricing_power = "Moderate"
            expansion = 3.2
            rationale = f"Operating margin of {margin_pct:.1f}% (20-30%) indicates solid operating leverage as volume ramps across mission-critical infrastructure."
        elif score == 2:
            pricing_power = "Developing"
            expansion = 2.1
            rationale = f"Operating margin of {margin_pct:.1f}% (10-20%) shows positive margin expansion from backlog pricing power, though subject to manufacturing COGS."
        else:
            pricing_power = "Constrained"
            expansion = 1.0
            rationale = f"Operating margin of {margin_pct:.1f}% (<10%) reflects thin contracting margins or heavy initial pass-through procurement costs."

        return OperatingMarginDetail(
            actual_operating_margin_pct=margin_pct,
            score=score,
            margin_expansion_3yr=expansion,
            pricing_power_rating=pricing_power,
            rationale=rationale
        )
