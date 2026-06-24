import os
from datetime import datetime
from core.config import *


UNKNOWN_DIR = "market_data/unknown_classification"
os.makedirs(UNKNOWN_DIR, exist_ok=True)


def save_unknown_classification(stocks):

    # ==========================================
    # FILTER UNKNOWN EMERGING LEADERS ONLY
    # ==========================================

    unknown_stocks = stocks[

        (stocks["Mapped_Theme"] == "Unknown")

        &

        (stocks["RS_Rating"] >= UNKNOWN_RS_THRESHOLD)

        &

        (stocks["Long_Score"] >= UNKNOWN_LONG_SCORE_THRESHOLD)

        &

        (

            stocks["Price as a % of 52 Wk H-L Range"]

            >=

            UNKNOWN_PRICE_POSITION_THRESHOLD

        )

        &

        (

            stocks["Market Cap (mil)"]

            >=

            UNKNOWN_MARKET_CAP_THRESHOLD

        )

    ].copy()

    # ==========================================
    # KEEP ONLY RESEARCH USEFUL COLUMNS
    # ==========================================

    output = unknown_stocks[[
        "Ticker",
        "Company Name",
        "Sector",
        "Industry",
        "RS_Rating",
        "Long_Score",
        "Last Close",
        "Price as a % of 52 Wk H-L Range",
        "Market Cap (mil)"
    ]]

    # ==========================================
    # SAVE CSV
    # ==========================================

    today = datetime.today().strftime("%Y-%m-%d")

    output = output.sort_values(
        by=["RS_Rating", "Long_Score"],
        ascending=False
)

    filename = os.path.join(
        UNKNOWN_DIR,
        f"{today}_unknown_emerging_leaders.csv"
    )

    output.to_csv(filename, index=False)

    print()
    print("UNKNOWN EMERGING LEADERS SAVED:", filename)