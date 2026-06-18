def build_short_watchlist(stocks):

    # ==========================================
    # SHORT CANDIDATES
    # Weak themes only
    # ==========================================

    short_watchlist = stocks[

        (stocks["Theme_Class"].isin(["Weakening", "Lagging"])) &

        (stocks["Composite_Score"] < 50)

    ]


    # ==========================================
    # SORT WEAKEST FIRST
    # ==========================================

    short_watchlist = short_watchlist.sort_values(

        ["Composite_Score", "RS_Rating"],

        ascending=True
    )


    return short_watchlist