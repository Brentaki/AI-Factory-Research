from typing import List, Dict, Any
from core.schema import CompanyProfile, TAFGSEvaluation, Company
from agents.moat_analysis import MoatAnalysisAgent


class ReportAgent:
    """
    Report Agent:
    Synthesizes investor-ready Top 20 ranking reports, structured company profiles,
    growth catalyst narratives (2026-2029), and Markdown summaries.
    """

    def generate_company_profile(self, company: Company, eval_item: TAFGSEvaluation) -> CompanyProfile:
        narrative = (
            f"**{company.name} ({company.ticker})** holds rank #{eval_item.rank} with a Total AI Factory Growth Score (TAFGS) of "
            f"**{eval_item.risk_adjusted_tafgs}**. Operating as a primary leader in **{eval_item.primary_sector.value}**, the company displays "
            f"a Moat Score of {eval_item.moat.score}/5.0 ({eval_item.moat.rationale}) and an Operating Margin Score of {eval_item.margin.score}/5 "
            f"({eval_item.margin.actual_operating_margin_pct:.1f}% margin). Driven by a 3-Year forecast CAGR of {eval_item.growth.forecast_3yr_cagr_pct:.1f}%, "
            f"it is primed to capture significant AI Factory capex."
        )

        timeline = [
            f"2026: {eval_item.growth.product_cycle_drivers[0] if eval_item.growth.product_cycle_drivers else 'Product ramp'}",
            f"2027: Hyper-scale expansion of AI Factory infrastructure orders",
            f"2028-2029: Next-gen architecture replacement cycle and recurring service monetization"
        ]

        return CompanyProfile(
            company=company,
            evaluation=eval_item,
            thesis_narrative=narrative,
            catalyst_timeline_2026_2029=timeline
        )

    def generate_markdown_report(self, top_20_evals: List[TAFGSEvaluation]) -> str:
        md = []
        md.append("# Top 20 AI Factory Growth Equity Leaderboard")
        md.append("*Ranked by Total AI Factory Growth Score (TAFGS)*\n")
        md.append("| Rank | Ticker | Company Name | Primary Role | Moat (0-5) | Margin Score | 3-Yr CAGR % | TAFGS |")
        md.append("| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |")

        for item in top_20_evals:
            md.append(
                f"| **#{item.rank}** | **{item.ticker}** | {item.company_name} | {item.primary_sector.value} | "
                f"{item.moat.score:.1f} | {item.margin.score} ({item.margin.actual_operating_margin_pct:.1f}%) | "
                f"{item.growth.forecast_3yr_cagr_pct:.1f}% | **{item.risk_adjusted_tafgs:.2f}** |"
            )

        md.append("\n## Detailed Company Profiles\n")
        for item in top_20_evals:
            md.append(f"### #{item.rank}. {item.company_name} ({item.ticker})")
            md.append(f"- **Primary Sector**: {item.primary_sector.value}")
            md.append(f"- **Total AI Growth Score (TAFGS)**: **{item.risk_adjusted_tafgs}** (Raw: {item.raw_tafgs})")
            md.append(f"- **Moat Rationale**: {item.moat.rationale}")
            md.append(f"- **Operating Margin**: {item.margin.actual_operating_margin_pct}% (Score: {item.margin.score}/5, Pricing Power: {item.margin.pricing_power_rating})")
            md.append(f"- **AI Growth Drivers**: {', '.join(item.growth.product_cycle_drivers)}")
            md.append(f"- **Risk Factor Summary**: {item.risk.risk_summary} (Discount: {item.risk.total_risk_discount_pct*100:.1f}%)\n")

        return "\n".join(md)
