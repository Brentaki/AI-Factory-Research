from typing import List
from core.schema import Company, SectorCategory

SEED_COMPANIES: List[Company] = [
    Company(
        ticker="NVDA",
        name="NVIDIA Corporation",
        market_cap_billions=3100.0,
        primary_sector=SectorCategory.COMPUTE,
        secondary_sectors=[SectorCategory.NETWORKING],
        ai_revenue_exposure_pct=88.0,
        actual_operating_margin_pct=62.5,
        order_backlog_growth_pct=140.0,
        moat_qualitative="CUDA software platform architecture lock-in, full-stack NVLink rack solutions (GB200/NVL72 reference standard), and chiplet ecosystem monopoly.",
        growth_catalysts=[
            "Blackwell & Rubin GPU platform deployment cycle (2026-2028)",
            "Spectrum-X Ethernet and Quantum InfiniBand networking expansion",
            "Sovereign AI factory cluster deployment worldwide"
        ],
        risk_factors=[
            "Custom ASIC competition from hyperscalers (Google TPU, AWS Trainium, Meta MTIA)",
            "Geopolitical trade restrictions on high-performance compute export"
        ]
    ),
    Company(
        ticker="AVGO",
        name="Broadcom Inc.",
        market_cap_billions=780.0,
        primary_sector=SectorCategory.NETWORKING,
        secondary_sectors=[SectorCategory.COMPUTE],
        ai_revenue_exposure_pct=42.0,
        actual_operating_margin_pct=58.0,
        order_backlog_growth_pct=85.0,
        moat_qualitative="Dominant position in custom AI XPU accelerators (for Google, Meta, Bytedance) and Jericho/Tomahawk silicon switching ASICs.",
        growth_catalysts=[
            "Tomahawk 6 / 1.6T networking switch silicon volume ramp",
            "Custom XPU AI accelerator design wins across 3 hyperscalers",
            "PCIe Gen6 retimer and optical interconnect interconnect adoption"
        ],
        risk_factors=[
            "Customer concentration with top 2 hyperscale ASIC co-development partners",
            "VMware integration and Enterprise software transition execution"
        ]
    ),
    Company(
        ticker="ANET",
        name="Arista Networks, Inc.",
        market_cap_billions=115.0,
        primary_sector=SectorCategory.NETWORKING,
        secondary_sectors=[],
        ai_revenue_exposure_pct=45.0,
        actual_operating_margin_pct=41.2,
        order_backlog_growth_pct=65.0,
        moat_qualitative="EOS operating system standard across cloud titan data centers; prime architect of AI Ethernet Ultra Ethernet Consortium standard.",
        growth_catalysts=[
            "AI spine-and-leaf Ethernet interconnect migration away from InfiniBand",
            "800G and 1.6T EOS switch deployment across Microsoft and Meta AI clusters",
            "Ethernet for GPU cluster interconnect share gains"
        ],
        risk_factors=[
            "High customer concentration (Microsoft and Meta represent >35% of revenue)",
            "Invasion of white-box switch vendors in lower-tier data centers"
        ]
    ),
    Company(
        ticker="VRT",
        name="Vertiv Holdings Co",
        market_cap_billions=38.5,
        primary_sector=SectorCategory.CRAHs,
        secondary_sectors=[SectorCategory.UPS, SectorCategory.SWITCHGEAR, SectorCategory.PDUS_BUSWAY],
        ai_revenue_exposure_pct=65.0,
        actual_operating_margin_pct=19.8,
        order_backlog_growth_pct=92.0,
        moat_qualitative="Primary liquid cooling and CDU partner for NVIDIA GB200 NVL72 architectures; dominant thermal/power distribution position in hyperscale clusters.",
        growth_catalysts=[
            "Direct-to-chip liquid cooling CDUs and thermal manifold hyper-ramp",
            "NVIDIA Co-Design liquid cooling reference architecture exclusivity",
            "Multi-megawatt modular prefabricated AI data center power skids"
        ],
        risk_factors=[
            "Supply chain component bottlenecks for specialized pumps and cold plates",
            "Rapid capacity expansion execution risks"
        ]
    ),
    Company(
        ticker="GEV",
        name="GE Vernova Inc.",
        market_cap_billions=72.0,
        primary_sector=SectorCategory.GAS_TURBINES,
        secondary_sectors=[SectorCategory.SWITCHGEAR],
        ai_revenue_exposure_pct=30.0,
        actual_operating_margin_pct=11.5,
        order_backlog_growth_pct=78.0,
        moat_qualitative="Heavy-frame HA-class gas turbine monopoly with multi-year manufacturing queue; critical power bridge for AI data centers starved by utility grid delays.",
        growth_catalysts=[
            "Behind-the-meter dedicated gas turbine power plant orders for AI megawatt sites",
            "Electrification grid transformer and switchgear backlog conversion",
            "Multi-year turbine service agreement margin expansion"
        ],
        risk_factors=[
            "Long lead-time manufacturing constraints and raw material inflation",
            "Environmental permitting delays for natural gas power generation"
        ]
    ),
    Company(
        ticker="MOD",
        name="Modine Manufacturing Company",
        market_cap_billions=6.8,
        primary_sector=SectorCategory.CRAHs,
        secondary_sectors=[SectorCategory.COOLING_TOWERS],
        ai_revenue_exposure_pct=52.0,
        actual_operating_margin_pct=15.4,
        order_backlog_growth_pct=110.0,
        moat_qualitative="Airedale liquid cooling brand and specialized chillers engineered specifically for high-density AI computer rooms.",
        growth_catalysts=[
            "High-density liquid coolant distribution units (CDUs) volume deployment",
            "Expansion of manufacturing capacity in North America and Europe for data center cooling",
            "Strategic thermal partnerships with AI server OEMs"
        ],
        risk_factors=[
            "Pure-play execution risk when competing against diversified industrials (Vertiv, Trane)",
            "Legacy auto/commercial industrial exposure drag"
        ]
    ),
    Company(
        ticker="ETN",
        name="Eaton Corporation plc",
        market_cap_billions=135.0,
        primary_sector=SectorCategory.SWITCHGEAR,
        secondary_sectors=[SectorCategory.UPS, SectorCategory.PDUS_BUSWAY],
        ai_revenue_exposure_pct=35.0,
        actual_operating_margin_pct=23.4,
        order_backlog_growth_pct=48.0,
        moat_qualitative="Comprehensive electrical distribution stack (medium voltage switchgear, transformers, busway) essential for gigawatt-scale AI factory grid interconnects.",
        growth_catalysts=[
            "Gigawatt-scale AI facility power distribution skid demand",
            "Substation transformer replacement and microgrid switchgear upgrade cycle",
            "Operating margin leverage from pricing power in high-demand electrical gear"
        ],
        risk_factors=[
            "Utility interconnect approval delays bottlenecking final project turn-on",
            "Cyclical exposure to broader commercial construction"
        ]
    ),
    Company(
        ticker="CAT",
        name="Caterpillar Inc.",
        market_cap_billions=170.0,
        primary_sector=SectorCategory.GENERATORS,
        secondary_sectors=[],
        ai_revenue_exposure_pct=22.0,
        actual_operating_margin_pct=21.8,
        order_backlog_growth_pct=38.0,
        moat_qualitative="Unrivaled global dealer network and high-horsepower (3MW+) generator technology critical for emergency backup power in AI hyperscale builds.",
        growth_catalysts=[
            "Cat 3516 / C175 multi-megawatt backup generator boom for AI campuses",
            "Hydrogen-blend and dual-fuel continuous power generation solutions",
            "High-margin spare parts and maintenance long-term service agreements"
        ],
        risk_factors=[
            "Macroeconomic sensitivity in resource and mining equipment divisions",
            "Engine emissions regulation shifts"
        ]
    ),
    Company(
        ticker="EME",
        name="EMCOR Group, Inc.",
        market_cap_billions=18.2,
        primary_sector=SectorCategory.CONSTRUCTION,
        secondary_sectors=[SectorCategory.ENGINEERING],
        ai_revenue_exposure_pct=38.0,
        actual_operating_margin_pct=10.2,
        order_backlog_growth_pct=54.0,
        moat_qualitative="Leading specialty electrical and mechanical contractor with specialized trade labor force required for complex AI data center mechanical installations.",
        growth_catalysts=[
            "High-density electrical piping and liquid cooling infrastructure installation",
            "Hyperscale fast-track buildouts across US data center alleys (Virginia, Texas, Ohio)",
            "Subcontractor pricing power due to acute skilled labor shortages"
        ],
        risk_factors=[
            "Specialized electrician and pipefitter labor shortages limiting project throughput",
            "Fixed-price contract cost overruns"
        ]
    ),
    Company(
        ticker="WSP",
        name="WSP Global Inc.",
        market_cap_billions=19.5,
        primary_sector=SectorCategory.ENGINEERING,
        secondary_sectors=[],
        ai_revenue_exposure_pct=28.0,
        actual_operating_margin_pct=12.8,
        order_backlog_growth_pct=42.0,
        moat_qualitative="Top-tier environmental, power grid interconnection, and mission-critical engineering consultant for sovereign and hyperscale AI campuses.",
        growth_catalysts=[
            "Complex grid interconnect study and environmental site engineering contracts",
            "Thermal management simulation and structural design for multi-hundred MW AI facilities",
            "M&A aggregation of niche mission-critical engineering firms"
        ],
        risk_factors=[
            "Professional engineering labor recruitment constraints",
            "Foreign exchange translation risks across international branches"
        ]
    ),
    Company(
        ticker="SMCI",
        name="Super Micro Computer, Inc.",
        market_cap_billions=26.0,
        primary_sector=SectorCategory.COMPUTE,
        secondary_sectors=[SectorCategory.CRAHs],
        ai_revenue_exposure_pct=72.0,
        actual_operating_margin_pct=11.3,
        order_backlog_growth_pct=125.0,
        moat_qualitative="Building-block modular server design enabling fastest time-to-market for new GPU architectures and custom direct liquid cooling (DLC) building blocks.",
        growth_catalysts=[
            "Mass shipping of 100kW+ liquid-cooled GPU building block racks",
            "Hyperscale and Tier-2 Neocloud volume deployment (CoreWeave, Lambda Labs)",
            "Green computing energy efficiency rack-scale solutions"
        ],
        risk_factors=[
            "Gross margin compression from competitive server pricing by Dell/HPE",
            "Internal control and accounting compliance scrutiny"
        ]
    ),
    Company(
        ticker="DELL",
        name="Dell Technologies Inc.",
        market_cap_billions=85.0,
        primary_sector=SectorCategory.COMPUTE,
        secondary_sectors=[],
        ai_revenue_exposure_pct=32.0,
        actual_operating_margin_pct=8.9,
        order_backlog_growth_pct=70.0,
        moat_qualitative="Unmatched enterprise sales distribution engine and PowerEdge XE9680 AI server platform backed by global service level support agreements.",
        growth_catalysts=[
            "PowerEdge AI server shipment surge to sovereign AI initiatives and tier-2 clouds",
            "Enterprise AI private cluster deployment bundled with storage and networking",
            "Liquid-assisted server rack deployment scale"
        ],
        risk_factors=[
            "Lower corporate operating margin profile compared to chip design peers",
            "Cyclical enterprise PC refresh headwinds"
        ]
    ),
    Company(
        ticker="TT",
        name="Trane Technologies plc",
        market_cap_billions=78.0,
        primary_sector=SectorCategory.CHILLERS,
        secondary_sectors=[SectorCategory.CRAHs],
        ai_revenue_exposure_pct=26.0,
        actual_operating_margin_pct=17.8,
        order_backlog_growth_pct=45.0,
        moat_qualitative="High-efficiency thermal management systems, centrifugal chillers, and proprietary thermal software controls integrated into hyperscale environments.",
        growth_catalysts=[
            "Next-gen oil-free magnetic levitation chillers for high-ambient data center locations",
            "Hyperscale customer custom thermal management backlog conversion",
            "Thermal equipment energy efficiency service software"
        ],
        risk_factors=[
            "Commercial HVAC sector cyclical slowing outside data centers",
            "Refrigerant transition compliance costs"
        ]
    ),
    Company(
        ticker="CMI",
        name="Cummins Inc.",
        market_cap_billions=42.0,
        primary_sector=SectorCategory.GENERATORS,
        secondary_sectors=[],
        ai_revenue_exposure_pct=20.0,
        actual_operating_margin_pct=13.2,
        order_backlog_growth_pct=36.0,
        moat_qualitative="Leading heavy-duty power generation sets (QSK95 engines) trusted globally for multi-megawatt mission-critical backup power.",
        growth_catalysts=[
            "High-horsepower generator set backlog growth driven by data center power expansion",
            "Accelera clean power division fuel cells and microgrid integration",
            "Aftermarket parts and service pricing power"
        ],
        risk_factors=[
            "Cyclical heavy-duty truck engine demand cycles",
            "Emissions settlement compliance tail risk"
        ]
    ),
    Company(
        ticker="MRVL",
        name="Marvell Technology, Inc.",
        market_cap_billions=58.0,
        primary_sector=SectorCategory.NETWORKING,
        secondary_sectors=[SectorCategory.COMPUTE],
        ai_revenue_exposure_pct=48.0,
        actual_operating_margin_pct=28.5,
        order_backlog_growth_pct=75.0,
        moat_qualitative="Leading PAM4 electro-optics DSP technology and custom AI compute ASIC design platform for AWS and tier-1 cloud providers.",
        growth_catalysts=[
            "800G and 1.6T PAM4 optical DSP chip ramp",
            "Custom AI accelerator compute ASIC production for major hyperscalers",
            "Active Electrical Cable (AEC) retimer expansion"
        ],
        risk_factors=[
            "Invasive competition from Broadcom in electro-optics DSPs",
            "Enterprise networking inventory correction cycles"
        ]
    ),
    Company(
        ticker="GLW",
        name="Corning Incorporated",
        market_cap_billions=33.0,
        primary_sector=SectorCategory.NETWORKING,
        secondary_sectors=[],
        ai_revenue_exposure_pct=25.0,
        actual_operating_margin_pct=18.6,
        order_backlog_growth_pct=52.0,
        moat_qualitative="High-density fiber optic cable patents and specialized interconnect hardware (Lumina, RocketRibbon) enabling 5x denser GPU fiber connectivity.",
        growth_catalysts=[
            "NVIDIA GB200 rack fiber interconnect density demands (requires up to 10x more fiber)",
            "Custom high-density fiber ribbon connectivity solutions for AI data center backbones",
            "Margin expansion in Optical Communications segment"
        ],
        risk_factors=[
            "Display glass legacy business cyclicality",
            "Raw material silica and optical glass input cost swings"
        ]
    ),
    Company(
        ticker="SU",
        name="Schneider Electric SE",
        market_cap_billions=135.0,
        primary_sector=SectorCategory.UPS,
        secondary_sectors=[SectorCategory.SWITCHGEAR, SectorCategory.PDUS_BUSWAY],
        ai_revenue_exposure_pct=32.0,
        actual_operating_margin_pct=18.1,
        order_backlog_growth_pct=42.0,
        moat_qualitative="Global leader in complete data center physical infrastructure (APC, EcoStruxure architecture, medium voltage switchgear, and rack PDUs).",
        growth_catalysts=[
            "EcoStruxure modular data center architecture deployment",
            "Hyperscale multi-megawatt UPS and switchgear turnkey orders",
            "Energy management software subscriptions"
        ],
        risk_factors=[
            "European industrial macroeconomic softness",
            "Supply chain extended lead times for high-voltage gear"
        ]
    ),
    Company(
        ticker="ENR",
        name="Siemens Energy AG",
        market_cap_billions=24.0,
        primary_sector=SectorCategory.GAS_TURBINES,
        secondary_sectors=[SectorCategory.SWITCHGEAR],
        ai_revenue_exposure_pct=24.0,
        actual_operating_margin_pct=7.5,
        order_backlog_growth_pct=60.0,
        moat_qualitative="World-class HL-class gas turbines and high-voltage grid transmission technology essential for connecting gigawatt AI clusters directly to power grids.",
        growth_catalysts=[
            "SGT5/6-9000HL gas turbine orders for dedicated AI power generation",
            "High-Voltage Direct Current (HVDC) transformer grid interconnect boom",
            "Turnaround in grid technology division operating margins"
        ],
        risk_factors=[
            "Siemens Gamesa wind turbine division quality and warranty drag",
            "Historical low operating margins in restructuring phase"
        ]
    ),
    Company(
        ticker="SPXC",
        name="SPX Technologies, Inc.",
        market_cap_billions=6.2,
        primary_sector=SectorCategory.COOLING_TOWERS,
        secondary_sectors=[],
        ai_revenue_exposure_pct=30.0,
        actual_operating_margin_pct=21.0,
        order_backlog_growth_pct=40.0,
        moat_qualitative="Marley brand evaporative cooling towers and specialized heat exchangers engineered for mission-critical hyperscale heat rejection.",
        growth_catalysts=[
            "Marley modular cooling tower shipments for large-scale data center builds",
            "M&A expansion in specialized industrial thermal components",
            "Operating margin leverage from HVAC productivity initiatives"
        ],
        risk_factors=[
            "Smaller market capitalization and lower liquidity",
            "Commercial HVAC demand seasonality"
        ]
    ),
    Company(
        ticker="JCI",
        name="Johnson Controls International plc",
        market_cap_billions=46.0,
        primary_sector=SectorCategory.CHILLERS,
        secondary_sectors=[SectorCategory.CRAHs],
        ai_revenue_exposure_pct=22.0,
        actual_operating_margin_pct=16.2,
        order_backlog_growth_pct=34.0,
        moat_qualitative="York chiller platform and Metasys building automation systems standard across major enterprise data center footprints.",
        growth_catalysts=[
            "York centrifugal chillers tailored for high-density liquid cooling heat loops",
            "Integrated digital automation and cybersecurity monitoring for AI facilities",
            "Portfolio transformation focusing pure-play on HVAC mission critical"
        ],
        risk_factors=[
            "Execution risks during non-core business divestitures",
            "Legacy residential building product drag"
        ]
    ),
    Company(
        ticker="J",
        name="Jacobs Solutions Inc.",
        market_cap_billions=18.5,
        primary_sector=SectorCategory.ENGINEERING,
        secondary_sectors=[SectorCategory.CONSTRUCTION],
        ai_revenue_exposure_pct=22.0,
        actual_operating_margin_pct=11.4,
        order_backlog_growth_pct=30.0,
        moat_qualitative="Global leader in advanced facility engineering, microgrid integration, and water management systems required for giant AI campuses.",
        growth_catalysts=[
            "Turnkey design and engineering for gigawatt-scale AI data center campuses",
            "Water treatment and closed-loop cooling system engineering",
            "Government and sovereign AI infrastructure advisory contracts"
        ],
        risk_factors=[
            "Separation and spin-off execution of government services unit",
            "Labor rate inflation in professional engineering"
        ]
    ),
    Company(
        ticker="PWR",
        name="Quanta Services, Inc.",
        market_cap_billions=41.0,
        primary_sector=SectorCategory.CONSTRUCTION,
        secondary_sectors=[SectorCategory.SWITCHGEAR],
        ai_revenue_exposure_pct=28.0,
        actual_operating_margin_pct=9.8,
        order_backlog_growth_pct=48.0,
        moat_qualitative="Largest electrical utility grid infrastructure contractor in North America; specialized in high-voltage transmission lines connecting AI data centers to power grids.",
        growth_catalysts=[
            "High-voltage transmission line construction connecting remote power generation to AI hubs",
            "Substation engineering and renewable microgrid interconnects",
            "Unrivaled skilled line worker labor force in North America"
        ],
        risk_factors=[
            "Weather disruption to outdoor transmission construction schedules",
            "Utility customer capital expenditure timing delays"
        ]
    ),
    Company(
        ticker="HPE",
        name="Hewlett Packard Enterprise Company",
        market_cap_billions=24.5,
        primary_sector=SectorCategory.COMPUTE,
        secondary_sectors=[SectorCategory.NETWORKING],
        ai_revenue_exposure_pct=26.0,
        actual_operating_margin_pct=10.4,
        order_backlog_growth_pct=50.0,
        moat_qualitative="Cray supercomputing legacy and ProLiant server platform with deep liquid cooling intellectual property and Slingshot interconnect tech.",
        growth_catalysts=[
            "Cray EX supercomputing cluster deployment for national AI labs",
            "Pending acquisition of Juniper Networks enhancing AI networking capability",
            "Enterprise AI server solution bundles"
        ],
        risk_factors=[
            "Regulatory antitrust review of Juniper Networks merger",
            "Lower gross margin profile in commoditized server builds"
        ]
    ),
    Company(
        ticker="CSCO",
        name="Cisco Systems, Inc.",
        market_cap_billions=205.0,
        primary_sector=SectorCategory.NETWORKING,
        secondary_sectors=[],
        ai_revenue_exposure_pct=15.0,
        actual_operating_margin_pct=27.2,
        order_backlog_growth_pct=25.0,
        moat_qualitative="Silicon One architecture and ubiquitous enterprise networking installed base, expanding aggressively into AI Ethernet webscale clusters.",
        growth_catalysts=[
            "Silicon One switch chip orders from hyperscalers exceeding $1B+",
            "Splunk acquisition integration boosting AI telemetry and security software",
            "Enterprise AI infrastructure migration to Cisco validated designs"
        ],
        risk_factors=[
            "Market share erosion in hyperscale cloud backend networks to Arista",
            "Slower growth in core enterprise campus networking"
        ]
    ),
    Company(
        ticker="CARR",
        name="Carrier Global Corporation",
        market_cap_billions=58.0,
        primary_sector=SectorCategory.CHILLERS,
        secondary_sectors=[],
        ai_revenue_exposure_pct=20.0,
        actual_operating_margin_pct=15.2,
        order_backlog_growth_pct=32.0,
        moat_qualitative="AquaEdge chillers and recent acquisition of Viessmann Climate Solutions positioning Carrier for high-efficiency data center thermal management.",
        growth_catalysts=[
            "AquaEdge high-efficiency centrifugal chillers for hyperscale sites",
            "Pure-play HVAC portfolio refocus following security and fire business divestitures",
            "Direct-to-chip liquid cooling technology partnerships"
        ],
        risk_factors=[
            "European residential heat pump market slowdown",
            "Integration execution of Viessmann acquisition"
        ]
    )
]


def get_seed_universe() -> List[Company]:
    """Returns the full seed list of public companies mapped across the AI Factory capital stack."""
    return SEED_COMPANIES
