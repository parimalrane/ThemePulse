from core.config import SHORT_FILTERS


def build_short_watchlist(stocks):

    short_watchlist = stocks[

        (

            stocks["Short_Score"]

            >= SHORT_FILTERS["MIN_SHORT_SCORE"]

        )

        &

        (

            (stocks["Theme_Class"] == "Weakening")

            |

            (stocks["Theme_Class"] == "Lagging")

        )

        &

        (

            stocks["Weakness_Score"] >= 70

        )

    ]


    short_watchlist = short_watchlist.sort_values(

        "Short_Score",

        ascending=False

    )


    return short_watchlist