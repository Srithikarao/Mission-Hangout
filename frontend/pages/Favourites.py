# ==========================================================
# MISSION HANGOUT
# FAVOURITES PAGE
# ==========================================================

"""
This page displays all the favourite places
saved by the user.

Responsibilities
----------------
✔ Display favourite places
✔ Remove favourite
✔ Clear all favourites
✔ Show total favourites
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st

from components.place_card import show_place_card

from components.favourites import (

    load_favourites,

    remove_favourite,

    clear_favourites

)


# ==========================================================
# SHOW FAVOURITES PAGE
# ==========================================================

def show_favourites_page():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("❤️ Favourite Places")

    st.write(
        """
        All the places that you have saved
        are displayed here.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # LOAD FAVOURITES
    # ------------------------------------------------------

    favourites = load_favourites()

    # ------------------------------------------------------
    # NO FAVOURITES
    # ------------------------------------------------------

    if len(favourites) == 0:

        st.info("No favourite places added yet.")

        return

    # ------------------------------------------------------
    # TOTAL
    # ------------------------------------------------------

    st.success(

        f"Total Favourite Places : {len(favourites)}"

    )

    st.write("")

    # ------------------------------------------------------
    # CLEAR BUTTON
    # ------------------------------------------------------

    if st.button(

        "🗑 Clear All Favourites",

        use_container_width=True

    ):

        clear_favourites()

        st.success("All favourites cleared.")

        st.rerun()

    st.divider()

    # ------------------------------------------------------
    # DISPLAY CARDS
    # ------------------------------------------------------

    for place in favourites:

        show_place_card(

            place,

            "Favourite"

        )

        # ----------------------------------------------
        # REMOVE BUTTON
        # ----------------------------------------------

        if st.button(

            "❌ Remove from Favourites",

            key=f"remove_{place['Place_ID']}"

        ):

            remove_favourite(

                place["Place_ID"]

            )

            st.success(

                "Removed successfully."

            )

            st.rerun()

        st.divider()