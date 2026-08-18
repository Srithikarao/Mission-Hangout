# ==========================================================
# MISSION HANGOUT
# RECENTLY VIEWED PAGE
# ==========================================================

"""
Displays all recently viewed places.

Responsibilities
----------------

✔ Display recent places

✔ Remove one place

✔ Clear history

✔ Show total recent places
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st

from components.place_card import show_place_card

from components.recent import (

    load_recent,

    remove_recent,

    clear_recent

)

# ==========================================================
# SHOW RECENT PAGE
# ==========================================================

def show_recent_page():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("🕒 Recently Viewed")

    st.write(
        """
        Every place you open is automatically
        added here.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # LOAD RECENT PLACES
    # ------------------------------------------------------

    recent_places = load_recent()


    col1,col2,col3=st.columns(3)

    with col1:

        st.metric(

            "Total Viewed",

            len(recent_places)

        )

    with col2:

        if len(recent_places)>0:

            st.metric(

                "Latest",

                recent_places[0]["Place_Name"]

            )

    with col3:

        st.metric(

            "History Limit",

            "20"

    )

    # ------------------------------------------------------
    # NO RECENT PLACES
    # ------------------------------------------------------

    if len(recent_places) == 0:

        st.empty()

        st.info(

            "You haven't viewed any places yet."

        )

        st.snow()

        return

    # ------------------------------------------------------
    # TOTAL PLACES
    # ------------------------------------------------------

    st.success(

        f"Recently Viewed Places : {len(recent_places)}"

    )

    st.write("")

    # ------------------------------------------------------
    # CLEAR HISTORY
    # ------------------------------------------------------

    if st.button(

        "🗑 Clear History",

        use_container_width=True

    ):

        clear_recent()

        st.success(

            "History Cleared Successfully."

        )

        st.rerun()

    st.divider()

    # ======================================================
    # DISPLAY PLACE CARDS
    # ======================================================

    for place in recent_places:

        show_place_card(

            place,

            "Recent"

        )


        if "Viewed_Time" in place:

            st.caption(

                "🕒 Last Viewed : "

                + place["Viewed_Time"]

            )




        col1, col2 = st.columns([5,1])

        with col2:

            if st.button(

                "❌ Remove",

                key=f"recent_remove_{place['Place_ID']}"

            ):

                remove_recent(

                    place["Place_ID"]

                )

                st.success(

                    "Removed Successfully."

                )

                st.rerun()

        st.divider()