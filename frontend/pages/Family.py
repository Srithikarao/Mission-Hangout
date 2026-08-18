# ==========================================================
# Import Required Libraries
# ==========================================================

import streamlit as st
# import os

# Import Family API functions
from api import (
    get_all_family_places,
    search_family_place,
    category_family_place,
    rating_family_place,
    free_family_places,
    paid_family_places,
    sort_family_rating,
    sort_family_name
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
# FAMILY PAGE
# ==========================================================

def show_family_page():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("👨‍👩‍👧 Family Places")

    st.write(
        """
        Discover the best family-friendly places in Warangal
        including parks, temples, museums, resorts,
        picnic spots and entertainment places.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # SEARCH BAR
    # ------------------------------------------------------

    search = st.text_input(

        "🔍 Search Place",

        placeholder="Enter Family Place..."

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

                "Temple",

                "Park",

                "Museum",

                "Resort",

                "Picnic Spot",

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

    with st.spinner("Loading Family Places..."):

        family_places = get_all_family_places()

        # Search

        if search.strip() != "":

            family_places = search_family_place(search)

        # Category

        elif category != "All":

            family_places = category_family_place(category)

        # Rating

        elif rating > 0:

            family_places = rating_family_place(rating)

        # Entry Fee

        elif fee == "Free":

            family_places = free_family_places()

        elif fee == "Paid":

            family_places = paid_family_places()

        # Sort

        elif sort == "Rating":

            family_places = sort_family_rating()

        elif sort == "Alphabetical":

            family_places = sort_family_name()

    # ------------------------------------------------------
    # ERROR HANDLING
    # ------------------------------------------------------

    if not family_places:

        st.error("Unable to fetch Family Places.")

        return

    # ------------------------------------------------------
    # TOTAL PLACES
    # ------------------------------------------------------

    st.success(

        f"Showing {len(family_places)} Family Places"

    )

    st.write("")

    # ======================================================
    # DISPLAY CARDS
    # ======================================================

    # BASE_DIR = os.path.dirname(
    #     os.path.dirname(os.path.abspath(__file__))
    # )

    for place in family_places:
        show_place_card(

        place,

        "Family"

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

    #                 "🌟 Best Known For :",

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

    #                     key=f"family_remove_{place['Place_ID']}"

    #                 ):
    #                     remove_favourite(

    #                         place["Place_ID"]

    #                     )

    #                     st.rerun()

    #             else:

    #                 if st.button(

    #                      "❤️ Add Favourite",

    #                     key=f"family_add_{place['Place_ID']}"

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

    #                     "⭐ Highly Recommended Family Place"

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

    #         # -------------------------------------------------
    #         # DIVIDER
    #         # -------------------------------------------------

    #         st.divider()

    # # ==========================================================
    # # END OF FAMILY PAGE
    # # ==========================================================                