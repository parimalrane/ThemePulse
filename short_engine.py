def build_short_watchlist(stocks):

    # ==========================================
    # PRIMARY SHORTS
    # Weak theme + weak composite
    # ==========================================

    primary_shorts = stocks[

        (stocks["Theme_Class"].isin(["Weakening", "Lagging"])) &

        (stocks["Composite_Score"] < 60)

    ]


    # ==========================================
    # RELATIVE WEAKNESS SHORTS
    # Weak stock even if theme not weak
    # ==========================================

    relative_weakness = stocks[

        (stocks["RS_Rating"] < 70) &

        (stocks["Zacks_Score"] <= 60)

    ]


    # ==========================================
    # COMBINE BOTH
    # Remove duplicates
    # ==========================================

    short_watchlist = primary_shorts.copy()

    short_watchlist = short_watchlist._append(

        relative_weakness

    ).drop_duplicates(subset=["Ticker"])


    # ==========================================
    # SORT WEAKEST FIRST
    # ==========================================

    short_watchlist = short_watchlist.sort_values(

        ["Composite_Score", "RS_Rating"],

        ascending=True
    )


    return short_watchlist