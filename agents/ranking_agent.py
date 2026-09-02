from typing import List, Dict
from datetime import datetime
from core.schema import Company, TAFGSEvaluation, Top20Ranking
from core.scoring_engine import compute_tafgs_evaluation
from agents.moat_analysis import MoatAnalysisAgent
from agents.margin_analysis import MarginAnalysisAgent
from agents.growth_forecast import GrowthForecastAgent
from agents.risk_adjustment import RiskAdjustmentAgent


class RankingAgent:
    """
    Ranking Agent:
    Computes Total AI Factory Growth Score (TAFGS) across all companies,
    ranks the universe, and generates the Top 20 Growth Leaderboard.
    """

    def __init__(self):
        self.moat_agent = MoatAnalysisAgent()
        self.margin_agent = MarginAnalysisAgent()
        self.growth_agent = GrowthForecastAgent()
        self.risk_agent = RiskAdjustmentAgent()

    def evaluate_company(self, company: Company) -> TAFGSEvaluation:
        moat = self.moat_agent.analyze_moat(company)
        margin = self.margin_agent.analyze_margin(company)
        growth = self.growth_agent.forecast_growth(company)
        risk = self.risk_agent.evaluate_risk(company)

        return compute_tafgs_evaluation(
            ticker=company.ticker,
            company_name=company.name,
            primary_sector=company.primary_sector,
            secondary_sectors=company.secondary_sectors,
            moat_score=moat.score,
            moat_rationale=moat.rationale,
            architectural_lockin=moat.architectural_lockin,
            ecosystem_dominance=moat.ecosystem_dominance,
            switching_cost_rating=moat.switching_cost_rating,
            bottleneck_position=moat.bottleneck_position,
            actual_operating_margin_pct=margin.actual_operating_margin_pct,
            margin_expansion_3yr=margin.margin_expansion_3yr,
            pricing_power_rating=margin.pricing_power_rating,
            margin_rationale=margin.rationale,
            ai_revenue_exposure_pct=growth.ai_revenue_exposure_pct,
            forecast_3yr_cagr_pct=growth.forecast_3yr_cagr_pct,
            order_backlog_growth_pct=growth.order_backlog_growth_pct,
            key_catalysts=growth.key_catalysts,
            product_cycle_drivers=growth.product_cycle_drivers,
            execution_risk=risk.execution_risk,
            customer_concentration_risk=risk.customer_concentration_risk,
            cyclicality_risk=risk.cyclicality_risk,
            risk_summary=risk.risk_summary
        )

    def rank_universe(self, companies: List[Company]) -> Top20Ranking:
        evaluations: List[TAFGSEvaluation] = [
            self.evaluate_company(company) for company in companies
        ]
        
        # Sort descending by risk_adjusted_tafgs
        sorted_evals = sorted(evaluations, key=lambda x: x.risk_adjusted_tafgs, reverse=True)
        
        # Assign rank 1..N
        top_20 = sorted_evals[:20]
        for idx, eval_item in enumerate(top_20, start=1):
            eval_item.rank = idx
            
        # Calculate sector distribution in top 20
        sector_counts: Dict[str, int] = {}
        for item in top_20:
            sec = item.primary_sector.value
            sector_counts[sec] = sector_counts.get(sec, 0) + 1

        return Top20Ranking(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_universe_scanned=len(companies),
            top_20=top_20,
            sector_distribution=sector_counts
        )
