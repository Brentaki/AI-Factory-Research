from core.schema import Company, RiskDetail


class RiskAdjustmentAgent:
    """
    Risk Adjustment Agent:
    Applies execution, cyclicality, and customer concentration discounts (0-30% total risk discount).
    """

    def evaluate_risk(self, company: Company) -> RiskDetail:
        ticker = company.ticker.upper()
        
        if ticker in ["NVDA", "AVGO"]:
            exec_risk = 0.04
            conc_risk = 0.05
            cyc_risk = 0.03
            summary = "Low execution risk backed by tech leadership; minor customer concentration discount."
        elif ticker in ["ANET", "VRT"]:
            exec_risk = 0.05
            conc_risk = 0.07
            cyc_risk = 0.03
            summary = "Moderate customer concentration discount (cloud titans MSFT, META); fast capacity ramp execution."
        elif ticker == "SMCI":
            exec_risk = 0.12
            conc_risk = 0.05
            cyc_risk = 0.05
            summary = "Elevated execution and corporate control discount offset by high growth rate."
        elif ticker in ["GEV", "ENR"]:
            exec_risk = 0.08
            conc_risk = 0.03
            cyc_risk = 0.06
            summary = "Gas turbine manufacturing lead time constraints and environmental permitting risks."
        elif ticker in ["EME", "PWR", "WSP"]:
            exec_risk = 0.06
            conc_risk = 0.03
            cyc_risk = 0.07
            summary = "Skilled trade labor shortage and fixed-price contracting risk."
        else:
            exec_risk = 0.05
            conc_risk = 0.05
            cyc_risk = 0.05
            summary = "Standard industrial execution and macroeconomic cyclicality risks."

        total_discount = min(exec_risk + conc_risk + cyc_risk, 0.30)
        
        return RiskDetail(
            execution_risk=exec_risk,
            customer_concentration_risk=conc_risk,
            cyclicality_risk=cyc_risk,
            total_risk_discount_pct=round(total_discount, 4),
            risk_summary=summary
        )
