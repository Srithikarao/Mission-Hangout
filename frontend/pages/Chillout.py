# ==========================================================
# Import Required Libraries
# ==========================================================

import streamlit as st

# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Import Chillout API functions
from api import (
    get_all_chill_places,
    search_chill_place,
    category_chill_place,
    rating_chill_place,
    free_chill_places,
    paid_chill_places,
    sort_chill_rating,
    sort_chill_name
)

# Image Loader
# from utils import load_image


# from components.favourites import (

#     add_favourite,

#     remove_favourite,

#     is_favourite

# )



from components.place_card import show_place_card


# create function

# ==========================================================
# CHILLOUT PAGE
# ==========================================================

def show_chill_page():

    st.title("🌳 Chillout Places")

    st.write(
        """
        Explore peaceful places, lakes, parks,
        viewpoints and relaxing destinations
        in Warangal.
        """
    )

    st.divider()

# search bar 

    # --------------------------------------------------
    # SEARCH
    # --------------------------------------------------

    search = st.text_input(
        "🔍 Search Place",
        placeholder="Search chillout place..."
    )

    st.write("")



# filters

    col1, col2, col3 = st.columns(3)

    # Category

    with col1:

        category = st.selectbox(

            "Category",

            [

                "All",

                "Lake",

                "Park",

                "View Point",

                "Garden",

                "Historical"

            ]

        )

    # Rating

    with col2:

        rating = st.slider(

            "⭐ Minimum Rating",

            0.0,

            5.0,

            0.0,

            0.1

        )

    # Sort

    with col3:

        sort = st.selectbox(

            "Sort By",

            [

                "Default",

                "Rating",

                "Alphabetical"

            ]

        )

# entry fee filter

    st.write("")

    fee = st.radio(

        "Entry Fee",

        [

            "All",

            "Free",

            "Paid"

        ],

        horizontal=True

    )

    st.divider()


# load data

    with st.spinner("Loading Chillout Places..."):

        places = get_all_chill_places()

        if search != "":

            places = search_chill_place(search)

        elif category != "All":

            places = category_chill_place(category)

        elif rating > 0:

            places = rating_chill_place(rating)

        elif fee == "Free":

            places = free_chill_places()

        elif fee == "Paid":

            places = paid_chill_places()

        elif sort == "Rating":

            places = sort_chill_rating()

        elif sort == "Alphabetical":

            places = sort_chill_name()


            # error handling 
    if not places:

        st.error("No places found.")

        return


# total places
    st.success(

        f"Showing {len(places)} Chillout Places"

    )

    st.write("")

    # display cards 

    for place in places:
        show_place_card(

            place,

            "Chillout"

        )        

        # with st.container():

        #     col1, col2 = st.columns([1,3])

        #     # -----------------------------
        #     # IMAGE
        #     # -----------------------------

        #     with col1:

        #         image_path = os.path.join(
        #              BASE_DIR,
        #             "images",
        #             f"{place['Place_ID']}.jpg"
        #                 )

        #         st.write(image_path)

        #         image_path = f"images/{place['Place_ID']}.jpg"
                
        #         image = load_image(image_path)
        #         st.write(image_path)
        #         st.image(

        #             image,

        #             use_container_width=True

        #         )

        #     # -----------------------------
        #     # DETAILS
        #     # -----------------------------

        #     with col2:

        #         st.subheader(

        #             place["Place_Name"]

        #         )

        #         st.write(

        #             "⭐ Rating:",

        #             place["Ratings"]

        #         )

        #         st.write(

        #             "🏞 Category:",

        #             place["Category"]

        #         )

        #         st.write(

        #             "💰 EntryFee:",

        #             place["Entry_Fee"]

        #         )

        #         st.write(

        #             "🕒 Timings:",

        #             place["Opening_Time"],

        #             "-",

        #             place["Closing_Time"]

        #         )

        #         st.write(

        #             "🌟 Best Known For:",

        #             place["Best_Known_For"]

        #         )

        #         # -------------------------------------------------
        #         # GOOGLE MAPS BUTTON
        #         # -------------------------------------------------

        #         if place["Google_Maps_Link"] != "":

        #             st.link_button(

        #                 "📍 Open in Google Maps",

        #                 place["Google_Maps_Link"]

        #             )



        #         # ------------------------------------------------------
        #         # FAVOURITE BUTTON
        #         # ------------------------------------------------------

        #         st.write("")

        #         if is_favourite(place["Place_ID"]):

        #             if st.button(

        #                 "💔 Remove Favourite",

        #                 key=f"chill_remove_{place['Place_ID']}"

        #             ):
        #                 remove_favourite(

        #                     place["Place_ID"]

        #                 )

        #                 st.rerun()

        #         else:

        #             if st.button(

        #                  "❤️ Add Favourite",

        #                 key=f"chill_add_{place['Place_ID']}"

        #             ):

        #                 add_favourite(

        #                     place

        #                 )

        #                 st.rerun()








        #         # -------------------------------------------------
        #         # VIEW DETAILS
        #         # -------------------------------------------------

        #         with st.expander("📄 View Details"):

        #             st.write(

        #                 "📍 Address:",

        #                 place["Address"]

        #             )

        #             st.write(

        #                 "🏙 Area:",

        #                 place["Area"]

        #             )

        #             st.write(

        #                 "🚗 Parking:",

        #                 place["Parking"]

        #             )

        #             st.write(

        #                 "🚻 Washroom:",

        #                 place["Washroom"]

        #             )

        #             st.write(

        #                 "📸 Photography Allowed:",

        #                 place["Photography"]

        #             )

        #             st.write(

        #                 "👨‍👩‍👧 Family Friendly:",

        #                 place["Family_Friendly"]

        #             )

        #             st.write(

        #                 "👥 Friends Friendly:",

        #                 place["Friends_Friendly"]

        #             )

        #             st.write(

        #                 "❤️ Couples Friendly:",

        #                 place["Couples_Friendly"]

        #             )

        #             st.write(

        #                 "🌅 Best Time To Visit:",

        #                 place["Best_Time"]

        #             )

        #             st.write(

        #                 "💡 Description:",

        #                 place["Description"]

        #             )

        #         # -------------------------------------------------
        #         # HIGHLY RATED PLACE
        #         # -------------------------------------------------

        #         if float(place["Ratings"]) >= 4.5:

        #             st.success(

        #                 "⭐ Highly Recommended"

        #             )

        #         # -------------------------------------------------
        #         # FREE ENTRY
        #         # -------------------------------------------------

        #         if place["Entry_Fee"] == "Free":

        #             st.info(

        #                 "🆓 Free Entry"

        #             )

        #         # -------------------------------------------------
        #         # PAID ENTRY
        #         # -------------------------------------------------

        #         elif place["Entry_Fee"] != "Free":

        #             st.warning(

        #                 f"💰 Entry Fee : {place['Entry_Fee']}"

        #             )

        #     # -------------------------------------------------
        #     # SEPARATOR
        #     # -------------------------------------------------

        #     st.divider()

    # =====================================================
    # END OF PAGE
    # =====================================================
        