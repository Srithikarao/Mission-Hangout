# ==========================================================
# Import Required Libraries
# ==========================================================

import streamlit as st
# import os

# Import Friends API functions
from api import (
    get_all_friends_places,
    search_friends_place,
    category_friends_place,
    rating_friends_place,
    free_friends_places,
    paid_friends_places,
    sort_friends_rating,
    sort_friends_name
)

# # Import image loader
# from utils import load_image


# from components.favourites import (

#     add_favourite,

#     remove_favourite,

#     is_favourite

# )


from components.place_card import show_place_card

# ==========================================================
# FRIENDS PAGE
# ==========================================================

def show_friends_page():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("👥 Friends Hangout Places")

    st.write(
        """
        Discover the best places to hang out with friends
        in Warangal including cafes, gaming zones,
        adventure parks, lakes, malls and entertainment spots.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # SEARCH BAR
    # ------------------------------------------------------

    search = st.text_input(

        "🔍 Search Place",

        placeholder="Enter Friends Hangout Place..."

    )

    st.write("")

    # ------------------------------------------------------
    # FILTERS
    # ------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    # ------------------------------------------------------
    # CATEGORY
    # ------------------------------------------------------

    with col1:

        category = st.selectbox(

            "Category",

            [

                "All",

                "Cafe",

                "Gaming Zone",

                "Mall",

                "Adventure",

                "Lake",

                "Park",

                "Entertainment"

            ]

        )

    # ------------------------------------------------------
    # RATING
    # ------------------------------------------------------

    with col2:

        rating = st.slider(

            "⭐ Minimum Rating",

            min_value=0.0,

            max_value=5.0,

            value=0.0,

            step=0.1

        )

    # ------------------------------------------------------
    # SORT
    # ------------------------------------------------------

    with col3:

        sort = st.selectbox(

            "Sort By",

            [

                "Default",

                "Rating",

                "Alphabetical"

            ]

        )

    st.write("")

    # ------------------------------------------------------
    # ENTRY FEE
    # ------------------------------------------------------

    fee = st.radio(

        "💰 Entry Fee",

        [

            "All",

            "Free",

            "Paid"

        ],

        horizontal=True

    )

    st.divider()

    # ------------------------------------------------------
    # LOAD DATA FROM BACKEND
    # ------------------------------------------------------

    with st.spinner("Loading Friends Hangout Places..."):

        friends_places = get_all_friends_places()

        # Search

        if search.strip() != "":

            friends_places = search_friends_place(search)

        # Category

        elif category != "All":

            friends_places = category_friends_place(category)

        # Rating

        elif rating > 0:

            friends_places = rating_friends_place(rating)

        # Entry Fee

        elif fee == "Free":

            friends_places = free_friends_places()

        elif fee == "Paid":

            friends_places = paid_friends_places()

        # Sort

        elif sort == "Rating":

            friends_places = sort_friends_rating()

        elif sort == "Alphabetical":

            friends_places = sort_friends_name()

    # ------------------------------------------------------
    # ERROR HANDLING
    # ------------------------------------------------------

    if not friends_places:

        st.error("Unable to fetch Friends Hangout Places.")

        return

    # ------------------------------------------------------
    # TOTAL PLACES
    # ------------------------------------------------------

    st.success(

        f"Showing {len(friends_places)} Friends Hangout Places"

    )

    st.write("")

    # ======================================================
    # DISPLAY PLACE CARDS
    # ======================================================

    # BASE_DIR = os.path.dirname(
    #     os.path.dirname(os.path.abspath(__file__))
    # )

    for place in friends_places:
        show_place_card(

        place,

        "Friends"

        )

    #     with st.container():

    #         col1, col2 = st.columns([1,3])

    #         # --------------------------------------------------
    #         # IMAGE
    #         # --------------------------------------------------

    #         with col1:

    #             image_path = os.path.join(

    #                 BASE_DIR,

    #                 "images",

    #                 f"{place['Place_ID']}.jpg"

    #             )

    #             image = load_image(image_path)

    #             st.image(

    #                 image,

    #                 use_container_width=True

    #             )

    #         # --------------------------------------------------
    #         # DETAILS
    #         # --------------------------------------------------

    #         with col2:

    #             st.subheader(

    #                 place["Place_Name"]

    #             )

    #             st.write(

    #                 "⭐ Rating :",

    #                 place["Ratings"]

    #             )

    #             st.write(

    #                 "🏷 Category :",

    #                 place["Category"]

    #             )

    #             st.write(

    #                 "💰 Entry Fee :",

    #                 place["Entry_Fee"]

    #             )

    #             st.write(

    #                 "🕒 Timings :",

    #                 place["Opening_Time"],

    #                 "-",

    #                 place["Closing_Time"]

    #             )

    #             st.write(

    #                 "🎉 Best Known For :",

    #                 place["Best_Known_For"]

    #             )

    #             # -------------------------------------------------
    #             # GOOGLE MAPS BUTTON
    #             # -------------------------------------------------

    #             if place["Google_Maps_Link"] != "":

    #                 st.link_button(

    #                     "📍 Open in Google Maps",

    #                     place["Google_Maps_Link"]

    #                 )



    #             # ------------------------------------------------------
    #             # FAVOURITE BUTTON
    #             # ------------------------------------------------------

    #             st.write("")

    #             if is_favourite(place["Place_ID"]):

    #                 if st.button(

    #                     "💔 Remove Favourite",

    #                     key=f"friends_remove_{place['Place_ID']}"

    #                 ):
    #                     remove_favourite(

    #                         place["Place_ID"]

    #                     )

    #                     st.rerun()

    #             else:

    #                 if st.button(

    #                      "❤️ Add Favourite",

    #                     key=f"friends_add_{place['Place_ID']}"

    #                 ):

    #                     add_favourite(

    #                         place

    #                     )

    #                     st.rerun()









    #             # -------------------------------------------------
    #             # VIEW DETAILS
    #             # -------------------------------------------------

    #             with st.expander("📄 View Details"):

    #                 st.write(

    #                     "📍 Address:",

    #                     place["Address"]

    #                 )

    #                 st.write(

    #                     "🏙 Area:",

    #                     place["Area"]

    #                 )

    #                 st.write(

    #                     "🚗 Parking:",

    #                     place["Parking"]

    #                 )

    #                 st.write(

    #                     "🚻 Washroom:",

    #                     place["Washroom"]

    #                 )

    #                 st.write(

    #                     "📸 Photography Allowed:",

    #                     place["Photography"]

    #                 )

    #                 st.write(

    #                     "👨‍👩‍👧 Family Friendly:",

    #                     place["Family_Friendly"]

    #                 )

    #                 st.write(

    #                     "👥 Friends Friendly:",

    #                     place["Friends_Friendly"]

    #                 )

    #                 st.write(

    #                     "❤️ Couples Friendly:",

    #                     place["Couples_Friendly"]

    #                 )

    #                 st.write(

    #                     "🎯 Activities:",

    #                     place["Activities"]

    #                 )

    #                 st.write(

    #                     "👨 Group Size:",

    #                     place["Group_Size"]

    #                 )

    #                 st.write(

    #                     "🌅 Best Time To Visit:",

    #                     place["Best_Time"]

    #                 )

    #                 st.write(

    #                     "📝 Description:",

    #                     place["Description"]

    #                 )

    #             # -------------------------------------------------
    #             # HIGHLY RECOMMENDED
    #             # -------------------------------------------------

    #             if float(place["Ratings"]) >= 4.5:

    #                 st.success(

    #                     "⭐ Highly Recommended Hangout"

    #                 )

    #             # -------------------------------------------------
    #             # FREE ENTRY
    #             # -------------------------------------------------

    #             if place["Entry_Fee"] == "Free":

    #                 st.info(

    #                     "🆓 Free Entry"

    #                 )

    #             # -------------------------------------------------
    #             # PAID ENTRY
    #             # -------------------------------------------------

    #             else:

    #                 st.warning(

    #                     f"💰 Entry Fee : {place['Entry_Fee']}"

    #                 )

    #             # -------------------------------------------------
    #             # BEST FOR GROUPS
    #             # -------------------------------------------------

    #             if "Group Size" in place:

    #                 st.info(

    #                     f"👥 Recommended Group Size: {place['Group_Size']}"

    #                 )

    #         # -------------------------------------------------
    #         # DIVIDER
    #         # -------------------------------------------------

    #         st.divider()

    # # ==========================================================
    # # END OF FRIENDS PAGE
    # # ==========================================================              