from core.schema import Company, MoatDetail


class MoatAnalysisAgent:
    """
    Moat Analysis Agent:
    Evaluates economic moat defensibility (0-5 score) based on:
    - Architectural lock-in (e.g. CUDA, EOS, NVLink)
    - Ecosystem dominance (design wins, reference architectures)
    - High switching costs / standard setting
    - Supply chain scarcity / bottleneck position
    """

    def analyze_moat(self, company: Company) -> MoatDetail:
        # Heuristic scoring based on company profile characteristics
        ticker = company.ticker.upper()
        
        if ticker == "NVDA":
            score = 5.0
            lockin = True
            dominance = True
            switching = "Extremely High"
            bottleneck = True
            rationale = "CUDA software ecosystem standard creates impenetrable developer lock-in. Monopoly position in rack-scale NVLink architectures (GB200/NVL72) and co-designed liquid-cooled AI factory building blocks."
        
        elif ticker == "AVGO":
            score = 4.8
            lockin = True
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Dominant co-developer of custom AI XPUs for Google and Meta, combined with near-monopoly on high-end Tomahawk/Jericho Ethernet switch silicon and optical DSPs."
        
        elif ticker == "ANET":
            score = 4.6
            lockin = True
            dominance = True
            switching = "High"
            bottleneck = False
            rationale = "EOS modular network operating system is the standard for cloud titan backend networks. Leading the Ultra Ethernet Consortium standard for scale-out GPU interconnects."

        elif ticker == "VRT":
            score = 4.5
            lockin = True
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Primary liquid cooling CDU and thermal management partner for NVIDIA Blackwell NVL72 architectures. Deep patent portfolio in high-density cooling distribution skids."

        elif ticker == "GEV":
            score = 4.4
            lockin = False
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Heavy-frame HA gas turbine manufacturing capacity booked out 4+ years. Crucial bottleneck solver for power-starved gigawatt AI data centers facing 5+ year grid interconnection queues."

        elif ticker == "MOD":
            score = 4.2
            lockin = False
            dominance = True
            switching = "Medium"
            bottleneck = True
            rationale = "Airedale liquid cooling brand and specialized chillers purpose-built for high-density AI data centers, securing rapid OEM reference design integrations."

        elif ticker == "ETN":
            score = 4.3
            lockin = False
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Unmatched product depth across medium-voltage switchgear, substation transformers, and high-amp busways essential for gigawatt power drops."

        elif ticker == "CAT":
            score = 4.1
            lockin = False
            dominance = True
            switching = "Medium"
            bottleneck = True
            rationale = "Unrivaled global dealer and service network for multi-megawatt 3516/C175 diesel and dual-fuel backup generator sets."

        elif ticker == "EME":
            score = 3.8
            lockin = False
            dominance = True
            switching = "Medium"
            bottleneck = True
            rationale = "Scarcity position in unionized master electrician and specialized pipefitter labor required to install complex liquid cooling manifolds in data centers."

        elif ticker == "WSP":
            score = 3.7
            lockin = False
            dominance = True
            switching = "Medium"
            bottleneck = False
            rationale = "Premier mission-critical engineering consultant for sovereign and hyperscale AI campus permitting, microgrid design, and environmental modeling."

        elif ticker == "SMCI":
            score = 3.5
            lockin = False
            dominance = False
            switching = "Medium"
            bottleneck = True
            rationale = "First-to-market modular building block server architecture enabling rapid customer deployment of novel liquid-cooled GPU racks, though facing OEM competition."

        elif ticker == "MRVL":
            score = 4.2
            lockin = True
            dominance = False
            switching = "High"
            bottleneck = True
            rationale = "Leading PAM4 electro-optics DSP technology and custom AI compute ASIC platform, serving key hyperscale customized silicon needs."

        elif ticker == "GLW":
            score = 4.0
            lockin = True
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Proprietary high-density optical fiber ribbon patents (Lumina) engineered specifically to handle up to 10x higher fiber density required in Blackwell rack architectures."

        elif ticker == "SU":
            score = 4.2
            lockin = False
            dominance = True
            switching = "High"
            bottleneck = True
            rationale = "Global leader in complete data center electrical distribution and EcoStruxure architecture, backed by global service level coverage."

        elif ticker == "TT":
            score = 4.0
            lockin = False
            dominance = True
            switching = "Medium"
            bottleneck = False
            rationale = "High-efficiency oil-free magnetic levitation chillers and proprietary thermal software controls integrated into hyperscale cooling loops."

        else:
            # General fallback heuristic based on company data
            score = 3.2 if company.ai_revenue_exposure_pct > 30 else 2.8
            lockin = company.ai_revenue_exposure_pct > 50
            dominance = company.market_cap_billions > 30.0
            switching = "Medium"
            bottleneck = False
            rationale = f"Solid competitive position in {company.primary_sector.value} with strong customer relationships and product execution."

        return MoatDetail(
            score=score,
            architectural_lockin=lockin,
            ecosystem_dominance=dominance,
            switching_cost_rating=switching,
            bottleneck_position=bottleneck,
            rationale=rationale
        )
