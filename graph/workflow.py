from typing import Dict, Any, List
from agents.market_mapping import MarketMappingAgent
from agents.ingestion import CompanyIngestionAgent
from agents.ranking_agent import RankingAgent
from agents.report_agent import ReportAgent
from core.schema import Top20Ranking


class AIFactoryResearchGraph:
    """
    State Graph Workflow Orchestrator:
    Executes the multi-agent research pipeline:
    1. Market Mapping Agent: Maps Stargate capex allocations
    2. Company Ingestion Agent: Ingests eligible public equity universe
    3. Moat, Margin, Growth, & Risk Analysis Agents (via Ranking Agent)
    4. Ranking Agent: Computes TAFGS scores and sorts Top 20
    5. Report Agent: Synthesizes investor report and Markdown summary
    """

    def __init__(self):
        self.market_map_agent = MarketMappingAgent()
        self.ingestion_agent = CompanyIngestionAgent()
        self.ranking_agent = RankingAgent()
        self.report_agent = ReportAgent()

    def run_full_pipeline(self) -> Dict[str, Any]:
        logs: List[str] = []
        
        # 1. Market Mapping Step
        logs.append("[Market Mapping Agent] Mapping Stargate 12-layer capital allocation ($60.97B baseline)...")
        market_map = self.market_map_agent.map_market_allocation()
        logs.append(f"[Market Mapping Agent] Mapped {len(market_map['sector_weights'])} infrastructure categories.")

        # 2. Company Ingestion Step
        logs.append("[Company Ingestion Agent] Ingesting global public equities with direct AI Factory exposure...")
        companies = self.ingestion_agent.ingest_universe()
        logs.append(f"[Company Ingestion Agent] Ingested and validated {len(companies)} target companies.")

        # 3. Moat, Margin, Growth, Risk Analysis & Ranking Step
        logs.append("[Moat Analysis Agent] Scoring architectural lock-in, reference architectures, and supply chain scarcity...")
        logs.append("[Margin Analysis Agent] Normalizing operating margins (Score 1-5) and pricing power...")
        logs.append("[Growth Forecast Agent] Projecting 3-Year AI-driven revenue CAGR %...")
        logs.append("[Risk Adjustment Agent] Calculating execution, concentration, and cyclicality risk discounts...")
        logs.append("[Ranking Agent] Computing Total AI Factory Growth Score (TAFGS = Moat * Margin * Growth * (1-Risk))...")
        
        ranking_result: Top20Ranking = self.ranking_agent.rank_universe(companies)
        logs.append(f"[Ranking Agent] Ranked top 20 equities. Rank #1: {ranking_result.top_20[0].company_name} ({ranking_result.top_20[0].ticker}) with TAFGS {ranking_result.top_20[0].risk_adjusted_tafgs}.")

        # 4. Investor Report Step
        logs.append("[Report Agent] Synthesizing investor-ready Top 20 Markdown report & structured JSON feeds...")
        markdown_report = self.report_agent.generate_markdown_report(ranking_result.top_20)
        logs.append("[Report Agent] Pipeline execution completed successfully.")

        return {
            "market_map": market_map,
            "ranking": ranking_result.model_dump(),
            "markdown_report": markdown_report,
            "execution_logs": logs
        }
