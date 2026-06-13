# stock_mapper.py


def map_stock_theme(industry, sector):

    industry = str(industry).lower().strip()
    sector = str(sector).lower().strip()

    # ==========================================
    # LEVEL 1 — SEMICONDUCTORS / AI / SOFTWARE
    # ==========================================

    if "semiconductor" in industry:
        return "Semiconductors"

    elif "chip" in industry:
        return "Semiconductors"

    elif "artificial intelligence" in industry:
        return "Artificial Intelligence"

    elif "machine learning" in industry:
        return "Artificial Intelligence"

    elif "security software" in industry:
        return "Software"

    elif "internet - security" in industry:
        return "Software"

    elif "cybersecurity" in industry:
        return "Software"

    elif "cloud" in industry:
        return "Cloud Computing"

    elif "software" in industry:
        return "Software"

    elif "internet - software" in industry:
        return "Software"

    elif "computer - software" in industry:
        return "Software"

    # ==========================================
    # LEVEL 2 — HEALTHCARE
    # ==========================================

    elif "medical" in industry:
        return "Medical Devices"

    elif "biomedical" in industry:
        return "Biotech"

    elif "genetics" in industry:
        return "Biotech"

    elif "pharmaceutical" in industry:
        return "Pharma"

    elif "pharma" in industry:
        return "Pharma"

    elif "biotech" in industry:
        return "Biotech"

    elif "drug manufacturers" in industry:
        return "Pharma"

    # ==========================================
    # LEVEL 3 — FINANCIALS
    # ==========================================

    elif "insurance" in industry:
        return "Insurance"

    elif "bank" in industry:
        return "Banking"

    elif "financial" in industry:
        return "Banking"

    elif "capital markets" in industry:
        return "Brokers/ Capital markets"

    elif "asset management" in industry:
        return "Banking"

    # ==========================================
    # LEVEL 4 — REAL ESTATE
    # ==========================================

    elif "reit" in industry:
        return "REITs"

    elif "real estate" in industry:
        return "REITs"

    # ==========================================
    # LEVEL 5 — ENERGY
    # ==========================================

    elif "pipeline" in industry:
        return "Infrastructure"

    elif "oil services" in industry:
        return "Equipment and services"

    elif "oil equipment" in industry:
        return "Equipment and services"

    elif "oil" in industry:
        return "Exploration"

    elif "gas" in industry:
        return "natural gas"

    elif "solar" in industry:
        return "Infrastructure"

    elif "uranium" in industry:
        return "Uranium Mining"

    elif "coal" in industry:
        return "Exploration"

    elif "renewable energy" in industry:
        return "Infrastructure"

    # ==========================================
    # LEVEL 6 — MATERIALS / MINING
    # ==========================================

    elif "rare earth" in industry:
        return "Rare Earth/Lithium"

    elif "lithium" in industry:
        return "Rare Earth/Lithium"

    elif "copper" in industry:
        return "Copper Mining"

    elif "gold" in industry:
        return "Gold Mining"

    elif "silver" in industry:
        return "Silver Mining"

    elif "metal products" in industry:
        return "Copper Mining"

    elif "steel" in industry:
        return "Copper Mining"

    elif "aluminum" in industry:
        return "Copper Mining"

    elif "mining" in industry:
        return "Gold Mining"

    # ==========================================
    # LEVEL 7 — INDUSTRIALS / TRANSPORT
    # ==========================================

    elif "aerospace" in industry:
        return "Aerospace & Defense"

    elif "defense" in industry:
        return "Aerospace & Defense"

    elif "airline" in industry:
        return "Transportation/Shipping"

    elif "transportation" in industry:
        return "Transportation/Shipping"

    elif "shipping" in industry:
        return "Transportation/Shipping"

    elif "logistics" in industry:
        return "Transportation/Shipping"

    elif "agriculture" in industry:
        return "Agribusiness"

    elif "construction" in industry:
        return "Infrastructure"

    elif "building products" in industry:
        return "Infrastructure"

    elif "building materials" in industry:
        return "Infrastructure"

    elif "engineering" in industry:
        return "Infrastructure"

    elif "manufacturing" in industry:
        return "Infrastructure"

    # ==========================================
    # LEVEL 8 — INTERNET / TELECOM
    # ==========================================

    elif "technology services" in industry:
        return "Broad"

    elif "internet - services" in industry:
        return "Internet"

    elif "communications equipment" in industry:
        return "Telecom"

    elif "networking" in industry:
        return "Internet"

    elif "internet" in industry:
        return "Internet"

    elif "telecommunications" in industry:
        return "Telecom"

    elif "wireless communications" in industry:
        return "Telecom"

    elif "cable television" in industry:
        return "Telecom"

    elif "broadband" in industry:
        return "Telecom"

    # ==========================================
    # LEVEL 9 — CONSUMER / RETAIL
    # ==========================================

    elif "apparel" in industry:
        return "Broad"

    elif "footwear" in industry:
        return "Broad"

    elif "retail" in industry:
        return "Broad"

    elif "consumer products" in industry:
        return "Broad"

    elif "beverages" in industry:
        return "Broad"

    elif "food products" in industry:
        return "Broad"

    elif "packaged foods" in industry:
        return "Broad"

    elif "restaurants" in industry:
        return "Broad"

    elif "casual dining" in industry:
        return "Broad"

    elif "gaming" in industry:
        return "Broad"

    elif "entertainment" in industry:
        return "Broad"

    elif "travel services" in industry:
        return "Transportation/Shipping"

    # ==========================================
    # LEVEL 10 — UTILITIES
    # ==========================================

    elif "electric utilities" in industry:
        return "Infrastructure"

    elif "power generation" in industry:
        return "Infrastructure"

    elif "renewable utilities" in industry:
        return "Infrastructure"

    elif "water utilities" in industry:
        return "Water"

    # ==========================================
    # SECTOR FALLBACK
    # ==========================================

    elif "technology" in sector:
        return "Broad"

    elif "medical" in sector:
        return "Healthcare"

    elif "finance" in sector:
        return "Banking"

    elif "utilities" in sector:
        return "Infrastructure"

    elif "energy" in sector:
        return "Exploration"

    elif "industrial" in sector:
        return "Infrastructure"

    elif "consumer" in sector:
        return "Broad"

    elif "communication" in sector:
        return "Telecom"

    elif "real estate" in sector:
        return "REITs"

    # ==========================================
    # UNKNOWN
    # ==========================================

    else:
        return "Unknown"