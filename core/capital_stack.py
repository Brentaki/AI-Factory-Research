from typing import List, Dict
from core.schema import CapitalStackLayer, SectorCategory

# Stargate Reference Capex Breakdown ($ Millions)
STARGATE_CAPEX_TOTAL = 60970.0  # Total equipment capital inside reference Stargate buildout

STARGATE_CAPITAL_STACK: List[CapitalStackLayer] = [
    CapitalStackLayer(
        category=SectorCategory.COMPUTE,
        stargate_allocation_millions=48750.0,
        percentage_share=round((48750.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="High-density GPU accelerators, custom ASIC nodes, host CPUs, and rack-scale AI server clusters.",
        key_equipment=["GPU Accelerators", "NVLink Switch Nodes", "Host Server Boards", "Liquid Cold Plates"],
        representative_companies=["Dell Technologies", "Hewlett Packard Enterprise", "IEIT Systems", "Super Micro Computer"]
    ),
    CapitalStackLayer(
        category=SectorCategory.NETWORKING,
        stargate_allocation_millions=8385.0,
        percentage_share=round((8385.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Ultra-high bandwidth fabric interconnects (InfiniBand, 800G/1.6T Ethernet switches, optical transceivers).",
        key_equipment=["800G/1.6T Ethernet Switches", "InfiniBand Routers", "Optical Transceivers", "Co-Packaged Optics"],
        representative_companies=["Cisco Systems", "Arista Networks", "Juniper Networks", "Broadcom", "Corning"]
    ),
    CapitalStackLayer(
        category=SectorCategory.UPS,
        stargate_allocation_millions=1755.0,
        percentage_share=round((1755.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Uninterruptible power supply systems providing continuous power conditioning and battery backup.",
        key_equipment=["Megawatt-scale UPS Modules", "Energy Storage Systems", "Flywheels"],
        representative_companies=["Schneider Electric", "Vertiv Holdings", "Eaton Corporation"]
    ),
    CapitalStackLayer(
        category=SectorCategory.CONSTRUCTION,
        stargate_allocation_millions=1755.0,
        percentage_share=round((1755.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="General contracting, shell construction, high-bay modular assembly, and commissioning.",
        key_equipment=["Hyper-scale Data Center Shells", "Modular Skids", "Site Preparation"],
        representative_companies=["Turner Construction", "Holder Construction", "HITT Contracting", "EMCOR Group"]
    ),
    CapitalStackLayer(
        category=SectorCategory.GENERATORS,
        stargate_allocation_millions=1560.0,
        percentage_share=round((1560.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Backup diesel and gas generator gensets for continuous power resilience during outages.",
        key_equipment=["3MW+ Diesel Gensets", "Dual-Fuel Generators", "Transfer Switches"],
        representative_companies=["Caterpillar", "Rolls-Royce Power Systems", "Cummins"]
    ),
    CapitalStackLayer(
        category=SectorCategory.GAS_TURBINES,
        stargate_allocation_millions=1560.0,
        percentage_share=round((1560.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="On-site baseload combined-cycle and simple-cycle gas turbines to bridge grid interconnections.",
        key_equipment=["Industrial Gas Turbines", "Combined-Cycle Gensets", "Hydrogen-blend Turbines"],
        representative_companies=["GE Vernova", "Siemens Energy"]
    ),
    CapitalStackLayer(
        category=SectorCategory.CRAHS,
        stargate_allocation_millions=1170.0,
        percentage_share=round((1170.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Computer Room Air Handlers and direct-to-chip liquid distribution units (CDUs).",
        key_equipment=["In-Row Coolers", "Liquid Coolant Distribution Units (CDUs)", "Air Handlers"],
        representative_companies=["Vertiv Holdings", "Stulz", "Johnson Controls", "Modine Manufacturing"]
    ),
    CapitalStackLayer(
        category=SectorCategory.SWITCHGEAR,
        stargate_allocation_millions=975.0,
        percentage_share=round((975.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Medium and low-voltage electrical switchgear, circuit breakers, and power distribution switchboards.",
        key_equipment=["Medium Voltage Switchgear", "Substation Transformers", "Circuit Breakers"],
        representative_companies=["Schneider Electric", "ABB", "Vertiv Holdings", "Eaton Corporation"]
    ),
    CapitalStackLayer(
        category=SectorCategory.CHILLERS,
        stargate_allocation_millions=780.0,
        percentage_share=round((780.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Industrial centrifugal chillers providing chilled water loops for high-density cooling.",
        key_equipment=["Centrifugal Water Chillers", "Oil-Free Magnetic Chillers", "Modular Chillers"],
        representative_companies=["Johnson Controls", "Trane Technologies", "Carrier", "Daikin"]
    ),
    CapitalStackLayer(
        category=SectorCategory.PDUS_BUSWAY,
        stargate_allocation_millions=780.0,
        percentage_share=round((780.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Rack Power Distribution Units (PDUs) and overhead busway track systems for flexible power drops.",
        key_equipment=["Smart Rack PDUs", "High-Ampere Busway Tracks", "Power Tap Off Boxes"],
        representative_companies=["Schneider Electric", "Vertiv Holdings", "Eaton Corporation"]
    ),
    CapitalStackLayer(
        category=SectorCategory.ENGINEERING,
        stargate_allocation_millions=780.0,
        percentage_share=round((780.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Architectural design, MEP (Mechanical, Electrical, Plumbing) engineering, and environmental permitting.",
        key_equipment=["MEP Engineering", "Thermal Simulation Modeling", "Grid Interconnect Studies"],
        representative_companies=["Jacobs", "Burns & McDonnell", "WSP Global"]
    ),
    CapitalStackLayer(
        category=SectorCategory.COOLING_TOWERS,
        stargate_allocation_millions=195.0,
        percentage_share=round((195.0 / STARGATE_CAPEX_TOTAL) * 100, 2),
        description="Evaporative and dry cooling towers for secondary heat rejection.",
        key_equipment=["Evaporative Cooling Towers", "Closed-Circuit Fluid Coolers"],
        representative_companies=["SPX Technologies", "Ebara", "Kelvion"]
    ),
]


def get_capital_stack_summary() -> Dict[str, Any]:
    """Returns summarized sector allocations and total budget metrics."""
    return {
        "total_stargate_budget_millions": STARGATE_CAPEX_TOTAL,
        "layers_count": len(STARGATE_CAPITAL_STACK),
        "layers": [layer.model_dump() for layer in STARGATE_CAPITAL_STACK]
    }
