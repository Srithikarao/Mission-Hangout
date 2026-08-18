# ==========================================================
# MISSION HANGOUT
# Dice The Place Component
# ==========================================================

"""
This component is responsible for

1. Fetching all places from every category
2. Combining all places
3. Picking one random place
4. Displaying rolling animation
5. Returning the selected place

This component can be used anywhere by simply calling

show_dice()
"""

# ==========================================================
# IMPORT REQUIRED LIBRARIES
# ==========================================================

import streamlit as st
import random
import time
import os


from components.recommendation import show_recommendation


# ----------------------------------------------------------
# Import API Functions
# ----------------------------------------------------------

from api import (

    get_all_food,

    get_all_chill_places,

    get_all_family_places,

    get_all_friends_places

)

from components.place_card import show_place_card

# ----------------------------------------------------------
# Image Loader
# ----------------------------------------------------------

from utils import load_image


# ==========================================================
# FUNCTION 1
# GET ALL PLACES
# ==========================================================

def get_all_places():

    """
    Fetch places from all categories
    and merge them into one list.
    """

    food_places = get_all_food()

    chill_places = get_all_chill_places()

    family_places = get_all_family_places()

    friends_places = get_all_friends_places()

    all_places = []

    if food_places:

        all_places.extend(food_places)

    if chill_places:

        all_places.extend(chill_places)

    if family_places:

        all_places.extend(family_places)

    if friends_places:

        all_places.extend(friends_places)

    return all_places


# ==========================================================
# FUNCTION 2
# PICK RANDOM PLACE
# ==========================================================

def random_place():

    """
    Returns one random place
    from all available places.
    """

    places = get_all_places()

    if len(places) == 0:

        return None

    return random.choice(places)


# ==========================================================
# FUNCTION 3
# SHOW DICE
# ==========================================================

def show_dice():

    """
    Displays the Dice button.

    When clicked,

    -> Shows rolling animation

    -> Picks random place

    -> Displays recommendation
    """

    # ------------------------------------------------------
    # Dice Button
    # ------------------------------------------------------

    left, right = st.columns([8,1])

    with right:

        dice = st.button(

            "🎲 Dice",

            use_container_width=True

        )

    # ------------------------------------------------------
    # User did not click
    # ------------------------------------------------------

    if not dice:

        return

    # ------------------------------------------------------
    # Rolling Animation
    # ------------------------------------------------------

    with st.spinner("🎲 Rolling Dice..."):

        progress = st.progress(0)

        status = st.empty()

        rolling_names = [

            "Restaurant",

            "Cafe",

            "Lake",

            "Temple",

            "Park",

            "Gaming Zone",

            "Resort",

            "View Point",

            "Bakery",

            "Adventure Park"

        ]

        for i in range(100):

            progress.progress(i + 1)

            if i % 10 == 0:

                status.info(

                    f"Searching : {random.choice(rolling_names)}"

                )

            time.sleep(0.02)

        progress.empty()

        status.empty()

    # ------------------------------------------------------
    # Select Random Place
    # ------------------------------------------------------

    place = random_place()

    # ------------------------------------------------------
    # No Data Available
    # ------------------------------------------------------

    if place is None:

        st.error(

            "No places available."

        )

        return

    # ------------------------------------------------------
    # Celebration
    # ------------------------------------------------------

    st.balloons()

    st.toast(

        "🎉 Destination Selected!"

    )

    st.success(

        "We Found A Place For You!"
    )


    show_place_card(

            place,

            "Dice"

    )







    # show_recommendation(place)






#     st.write("")
#     st.divider()

#     st.header("🎯 Today's Recommendation")

#     st.write("") 


#         # ==========================================================
#     # DISPLAY RECOMMENDED PLACE
#     # ==========================================================

#     BASE_DIR = os.path.dirname(
#         os.path.dirname(os.path.abspath(__file__))
#     )

#     image_path = os.path.join(

#         BASE_DIR,

#         "images",

#         f"{place['Place _ID']}.jpg"

#     )

#     image = load_image(image_path)

#     # ----------------------------------------------------------
#     # CARD LAYOUT
#     # ----------------------------------------------------------

#     col1, col2 = st.columns([1, 2])

#     # ==========================================================
#     # LEFT COLUMN
#     # ==========================================================

#     with col1:

#         st.image(

#             image,

#             use_container_width=True

#         )

#     # ==========================================================
#     # RIGHT COLUMN
#     # ==========================================================

#     with col2:

#         st.subheader(

#             place["Place Name"]

#         )

#         # ------------------------------------------------------
#         # CATEGORY
#         # ------------------------------------------------------

#         if "Category" in place:

#             st.write(

#                 "🏷 Category :", place["Category"]

#             )

#         # ------------------------------------------------------
#         # RATING
#         # ------------------------------------------------------

#         if "Ratings" in place:

#             st.write(

#                 "⭐ Rating :", place["Ratings"]

#             )

#         # ------------------------------------------------------
#         # TIMINGS
#         # ------------------------------------------------------

#         opening = place.get("Opening Time", "")

#         closing = place.get("Closing Time", "")

#         if opening != "" and closing != "":

#             st.write(

#                 "🕒 Timings :",

#                 opening,

#                 "-",

#                 closing

#             )

#         # ------------------------------------------------------
#         # PRICE
#         # ------------------------------------------------------

#         if "Price Range" in place:

#             st.write(

#                 "💰 Price :", place["Price Range"]

#             )

#         # ------------------------------------------------------
#         # ENTRY FEE
#         # ------------------------------------------------------

#         elif "Entry Fee" in place:

#             st.write(

#                 "💰 Entry Fee :", place["Entry Fee"]

#             )

#         # ------------------------------------------------------
#         # BEST KNOWN FOR
#         # ------------------------------------------------------

#         if "Best Known For" in place:

#             st.write(

#                 "🔥 Best Known For :",

#                 place["Best Known For"]

#             )

#         # ------------------------------------------------------
#         # GOOGLE MAPS
#         # ------------------------------------------------------

#         if place.get("Google Maps Link", "") != "":

#             st.link_button(

#                 "📍 Open in Google Maps",

#                 place["Google Maps Link"]

#             )

#     # ==========================================================
#     # VIEW DETAILS
#     # ==========================================================

#     with st.expander("📄 View Complete Details"):

#         for key, value in place.items():

#             if key not in [

#                 "Google Maps Link",

#                 "Place_ID"

#             ]:

#                 st.write(

#                     f"**{key} :**",

#                     value

#                 )

#     # ==========================================================
#     # BADGES
#     # ==========================================================

#     st.write("")

#     badge1, badge2, badge3 = st.columns(3)

#     # ----------------------------------------------------------
#     # HIGHLY RATED
#     # ----------------------------------------------------------

#     with badge1:

#         try:

#             if float(place.get("Ratings", 0)) >= 4.5:

#                 st.success(

#                     "⭐ Highly Rated"

#                 )

#         except:

#             pass

#     # ----------------------------------------------------------
#     # NEWLY OPENED
#     # ----------------------------------------------------------

#     with badge2:

#         if place.get("Newly Opened", "") == "Yes":

#             st.info(

#                 "🆕 Newly Opened"

#             )

#     # ----------------------------------------------------------
#     # FREE ENTRY
#     # ----------------------------------------------------------

#     with badge3:

#         if place.get("Entry Fee", "") == "Free":

#             st.success(

#                 "🆓 Free Entry"

#             )

#     # ==========================================================
#     # FINAL MESSAGE
#     # ==========================================================

#     st.divider()

#     st.markdown(

#         """
#         ### 🎉 Enjoy Your Visit!

#         We hope you have an amazing experience at this place.

#         Didn't like the recommendation?

#         Click **🎲 Dice** again to discover another place!
#         """

#     )

# # ==========================================================
# # END OF FILE
# # ==========================================================            