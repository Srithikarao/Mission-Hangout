# ==========================================================
# MISSION HANGOUT
# GLOBAL SEARCH COMPONENT
# ==========================================================

"""
Global Search Component

Purpose:
---------
Searches across all categories

✔ Food
✔ Chillout
✔ Family
✔ Friends

Displays all matching places in one location.
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import streamlit as st

from api import (

    search_food,

    search_chill_place,

    search_family_place,

    search_friends_place

)

from components.recommendation import show_recommendation

from components.place_card import show_place_card
# ==========================================================
# SEARCH EVERY CATEGORY
# ==========================================================

def search_everything(search_text):

    """
    Searches every category and combines results.
    """

    all_results = []

    # ------------------------------------------------------
    # FOOD
    # ------------------------------------------------------

    try:

        food = search_food(search_text)
        st.write(food)

        if food:

            for item in food:

                item["Module"] = "Food"

            all_results.extend(food)

    except Exception:

        pass

    # ------------------------------------------------------
    # CHILLOUT
    # ------------------------------------------------------

    try:

        chill = search_chill_place(search_text)

        st.write(chill)

        if chill:

            for item in chill:

                item["Module"] = "Chillout"

            all_results.extend(chill)

    except Exception:

        pass

    # ------------------------------------------------------
    # FAMILY
    # ------------------------------------------------------

    try:

        family = search_family_place(search_text)

        st.write(family)
        if family:

            for item in family:

                item["Module"] = "Family"

            all_results.extend(family)

    except Exception:

        pass

    # ------------------------------------------------------
    # FRIENDS
    # ------------------------------------------------------

    try:

        friends = search_friends_place(search_text)

        st.write(friends)

        if friends:

            for item in friends:

                item["Module"] = "Friends"

            all_results.extend(friends)

    except Exception:

        pass

    return all_results


# ==========================================================
# DISPLAY SEARCH BAR
# ==========================================================

def show_search():

    """
    Displays the Global Search UI.
    """

    st.subheader("🔍 Global Search")

    st.caption(

        "Search restaurants, cafes, lakes, parks, temples and more."

    )

    search_text = st.text_input(

        "Search Any Place",

        placeholder="Example : Cream Stone, Bhadrakali Lake..."

    )

    # ------------------------------------------------------
    # NO SEARCH
    # ------------------------------------------------------

    if search_text.strip() == "":

        return

    # ------------------------------------------------------
    # SEARCHING
    # ------------------------------------------------------

    with st.spinner("Searching all places..."):

        results = search_everything(search_text)
        st.write(results)

    st.write("")

    # ------------------------------------------------------
    # NO RESULTS
    # ------------------------------------------------------

    if len(results) == 0:

        st.warning(

            "No places found."

        )

        return

    # ------------------------------------------------------
    # TOTAL RESULTS
    # ------------------------------------------------------

    st.success(

        f"Found {len(results)} matching place(s)."

    )

    st.write("")

    # ======================================================
    # DISPLAY RESULTS
    # ======================================================

    for place in results:

        module = place.get(

            "Module",

            "Unknown"

        )

        st.markdown(

            f"### 📂 Category : {module}"

        )

        # show_recommendation(place)

        # st.divider()

        show_place_card(

            place,

            place.get("Module", "Search")

        )