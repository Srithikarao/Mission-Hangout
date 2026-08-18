# ==========================================================
# MISSION HANGOUT
# Recommendation Component
# ==========================================================

"""
This component displays a beautiful recommendation card
for any place received from the Dice feature or any other
module.

Usage

from components.recommendation import show_recommendation

show_recommendation(place)
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st
import os

from utils import load_image


from components.favourites import (

    add_favourite,

    remove_favourite,

    is_favourite

)

# ==========================================================
# SHOW RECOMMENDATION
# ==========================================================

def show_recommendation(place):

    """
    Displays the selected place in a beautiful card.
    """

    # ------------------------------------------------------
    # CHECK DATA
    # ------------------------------------------------------

    if place is None:

        st.error("No recommendation available.")

        return

    # ------------------------------------------------------
    # IMAGE PATH
    # ------------------------------------------------------

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    image_path = os.path.join(

        BASE_DIR,

        "images",

        f"{place.get('Place_ID','default')}.jpg"

    )

    image = load_image(image_path)

    # ------------------------------------------------------
    # TITLE
    # ------------------------------------------------------

    st.header("🎯 Today's Recommendation")

    st.divider()

    # ------------------------------------------------------
    # LAYOUT
    # ------------------------------------------------------

    col1, col2 = st.columns([1,2])

    # ======================================================
    # IMAGE
    # ======================================================

    with col1:

        st.image(

            image,

            use_container_width=True

        )

    # ======================================================
    # DETAILS
    # ======================================================

    with col2:

        st.subheader(

            place.get("Place_Name","Unknown Place")

        )

        if "Category" in place:

            st.write(

                "🏷 Category :",

                place["Category"]

            )

        if "Ratings" in place:

            st.write(

                "⭐ Rating :",

                place["Ratings"]

            )

        opening = place.get("Opening Time","")

        closing = place.get("Closing Time","")

        if opening != "" and closing != "":

            st.write(

                "🕒 Timings :",

                opening,

                "-",

                closing

            )

        if "Cuisine" in place:

            st.write(

                "🍽 Cuisine :",

                place["Cuisine"]

            )

        if "Price_Range" in place:

            st.write(

                "💰 Price Range :",

                place["Price_Range"]

            )

        elif "Entry_Fee" in place:

            st.write(

                "💰 Entry Fee :",

                place["Entry_Fee"]

            )

        if "Best_0Known_For" in place:

            st.write(

                "🔥 Best Known For :",

                place["Best_Known_For"]

            )

        if place.get("Google_Maps_Link","") != "":

            st.link_button(

                "📍 Open in Google Maps",

                place["Google_Maps_Link"]

            )

    # ======================================================
    # VIEW DETAILS
    # ======================================================

    with st.expander("📄 View Complete Details"):

        for key, value in place.items():

            if key not in [

                "Google_Maps_Link",

                "Place_ID"

            ]:

                st.write(

                    f"**{key}:**",

                    value

                )



    # ======================================================
    # FAVOURITE BUTTON
    # ======================================================

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if is_favourite(

            place["Place_ID"]

        ):

            if st.button(

                "💔 Remove Favourite",

                key=f"remove_favourite_{place['Place_ID']}"

            ):

                remove_favourite(

                    place["Place_ID"]

                )

                st.rerun()

        else:

            if st.button(

                "❤️ Add Favourite",

                key=f"add_favourite_{place['Place_ID']}"

            ):

                add_favourite(

                    place

                )

                st.rerun()


    

    # ======================================================
    # BADGES
    # ======================================================

    st.write("")

    badge1, badge2, badge3 = st.columns(3)

    # ------------------------------------------------------
    # HIGHLY RATED
    # ------------------------------------------------------

    with badge1:

        try:

            if float(place.get("Ratings",0)) >= 4.5:

                st.success(

                    "⭐ Highly Rated"

                )

        except:

            pass

    # ------------------------------------------------------
    # NEWLY OPENED
    # ------------------------------------------------------

    with badge2:

        if place.get("Newly_Opened","") == "Yes":

            st.info(

                "🆕 Newly_Opened"

            )

    # ------------------------------------------------------
    # FREE ENTRY
    # ------------------------------------------------------

    with badge3:

        if place.get("Entry_Fee","") == "Free":

            st.success(

                "🆓 Free Entry"

            )

    st.divider()

    st.success(

        "🎉 Enjoy your visit!"
    )