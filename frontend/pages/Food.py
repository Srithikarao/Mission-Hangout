# ==========================================================
# Import Required Libraries
# ==========================================================

import streamlit as st
from api import get_all_food


# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# Import all Food-related API functions
from api import (
    API_URL , 
    get_all_food,
    search_food,
    category_food,
    cuisine_food,
    rating_food,
    new_food,
    sort_rating,
    sort_name
)

# # Import image loading helper
# from utils import load_image



# from components.favourites import (

#     add_favourite,

#     remove_favourite,

#     is_favourite

# )


from components.place_card import show_place_card


# ==========================================================
# FOOD PAGE FUNCTION
# Everything related to the Food page is written inside
# this function.
# ==========================================================

def show_food_page():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("🍽 Food Places")

    st.write(
        """
        Discover the best restaurants, cafes, bakeries,
        dessert shops and food courts in Warangal.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # SEARCH BAR
    # ------------------------------------------------------

    search = st.text_input(
        "🔍 Search Place",
        placeholder="Enter restaurant or cafe name..."
    )

    st.write("")

    # ------------------------------------------------------
    # FILTERS
    # ------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    # -----------------------------
    # CATEGORY
    # -----------------------------

    with col1:

        category = st.selectbox(

            "Category",

            [
                "All",
                "Restaurant",
                "Cafe",
                "Dessert Shop",
                "Bakery",
                "Food Court"
            ]

        )

    # -----------------------------
    # CUISINE
    # -----------------------------

    with col2:

        cuisine = st.selectbox(

            "Cuisine",

            [
                "All",
                "Indian",
                "Chinese",
                "Italian",
                "Fast Food",
                "Cafe",
                "Desserts"
            ]

        )

    # -----------------------------
    # SORTING
    # -----------------------------

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
    # SECOND FILTER ROW
    # ------------------------------------------------------

    col4, col5 = st.columns([3,2])

    # -----------------------------
    # RATING
    # -----------------------------

    with col4:

        rating = st.slider(

            "⭐ Minimum Rating",

            min_value=0.0,

            max_value=5.0,

            value=0.0,

            step=0.1

        )

    # -----------------------------
    # NEWLY OPENED
    # -----------------------------

    with col5:

        new = st.checkbox(

            "🆕 Newly Opened Only"

        )

    st.divider()

    # ------------------------------------------------------
    # LOADING DATA FROM BACKEND
    # ------------------------------------------------------

    with st.spinner("Loading Food Places..."):

        # Default

        food_places = get_all_food()

        # Search

        if search.strip() != "":

            food_places = search_food(search)

        # Category

        elif category != "All":

            food_places = category_food(category)

        # Cuisine

        elif cuisine != "All":

            food_places = cuisine_food(cuisine)

        # Rating

        elif rating > 0:

            food_places = rating_food(rating)

        # Newly Opened

        elif new:

            food_places = new_food()

        # Sort by Rating

        elif sort == "Rating":

            food_places = sort_rating()

        # Sort Alphabetically

        elif sort == "Alphabetical":

            food_places = sort_name()

    # ------------------------------------------------------
    # ERROR HANDLING
    # ------------------------------------------------------

    if not food_places:

        st.error("Unable to fetch data from the backend.")

        return

    # ------------------------------------------------------
    # SHOW TOTAL PLACES
    # ------------------------------------------------------

    st.success(

        f"Showing {len(food_places)} Food Places"

    )

    st.write("")

    # ======================================================
    # DISPLAY FOOD CARDS
    # ======================================================

    for place in food_places:
        show_place_card(

            place,

            "Food"

        )


    # ==========================================================
    # END OF FOOD PAGE
    # ==========================================================        








        # with st.container():

        #     col1, col2 = st.columns([1,3])

        #     # --------------------------------------------
        #     # LEFT COLUMN
        #     # IMAGE
        #     # --------------------------------------------

        #     with col1:

        #         # Image name should match Place_ID
        #         # Example:
        #         #
        #         # images/
        #         #      F001.jpg
        #         #      F002.jpg
        #         #      F003.jpg
        #         #
        #         # If image is missing,
        #         # default.jpg will be shown.

        #         image_path = os.path.join(
        #              BASE_DIR,
        #              "images",
        #              f"{place['Place_ID']}.jpg"
        #                     )

        #         image = load_image(image_path)

        #         if image:
        #             st.image(image, use_container_width=True)
        #         else:
        #             st.warning("Image not available")

        #     # --------------------------------------------
        #     # RIGHT COLUMN
        #     # PLACE DETAILS
        #     # --------------------------------------------

        #     with col2:

        #         st.subheader(

        #             place["Place_Name"]

        #         )

        #         st.write(

        #             "⭐ Rating :",

        #             place["Ratings"]

        #         )

        #         st.write(

        #             "🍜 Cuisine :",

        #             place["Cuisine"]

        #         )

        #         st.write(

        #             "🏷 Category :",

        #             place["Category"]

        #         )

        #         st.write(

        #             "💰 Price :",

        #             place["Average_Price"]

        #         )

        #         st.write(

        #             "🕒 Timings :",

        #             place["Opening_Time"],

        #             "-",

        #             place["Closing_Time"]

        #         )

        #         st.write(

        #             "🔥 Best Known For :",

        #             place["Best_Known_For"]

        #         )

        #         # -------------------------------------------------
        #         # GOOGLE MAPS BUTTON
        #         # -------------------------------------------------

        #         # Check whether the Google Maps link exists.
        #         # If the link is available, display a button
        #         # that opens the location in Google Maps.

                

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

        #                 key=f"food_remove_{place['Place_ID']}"

        #             ):
        #                 remove_favourite(

        #                     place["Place_ID"]

        #                 )

        #                 st.rerun()

        #         else:

        #             if st.button(

        #                  "❤️ Add Favourite",

        #                 key=f"food_add_{place['Place_ID']}"

        #             ):

        #                 add_favourite(

        #                     place

        #                 )

        #                 st.rerun()






        #     #     # -------------------------------------------------
        #     #     # VIEW DETAILS
        #     #     # -------------------------------------------------

        #     #     # The expander keeps the UI clean.
        #     #     # The user can click "View Details"
        #     #     # to see more information about the place.

        #     #     with st.expander("📄 View Details"):

        #     #         st.write(
        #     #             "📍 Address:",
        #     #             place["Address"]
        #     #         )

        #     #         st.write(
        #     #             "🏙 Area:",
        #     #             place["Area"]
        #     #         )

        #     #         st.write(
        #     #             "🍽 Popular Dishes:",
        #     #             place["Popular_Dishes"]
        #     #         )

        #     #         st.write(
        #     #             "🥗 Veg / Non-Veg:",
        #     #             place["Veg_NonVeg"]
        #     #         )

        #     #         st.write(
        #     #             "🪑 Indoor Seating:",
        #     #             place["Indoor"]
        #     #         )

        #     #         st.write(
        #     #             "🌳 Outdoor Seating:",
        #     #             place["Outdoor"]
        #     #         )

        #     #         st.write(
        #     #             "👨‍👩‍👧 Family Friendly:",
        #     #             place["Family_Friendly"]
        #     #         )

        #     #         st.write(
        #     #             "👨‍👩‍👦 Friends Friendly:",
        #     #             place["Friends_Friendly"]
        #     #         )

        #     #         st.write(
        #     #             "❤️ Couples Friendly:",
        #     #             place["Couples_Friendly"]
        #     #         )

        #     #         st.write(
        #     #             "🚗 Parking:",
        #     #             place["Parking"]
        #     #         )

        #     #         st.write(
        #     #             "🆕 Newly Opened:",
        #     #             place["Newly_Opened"]
        #     #         )

        #     #         st.write(
        #     #             "⭐ Reviews:",
        #     #             place["Reviews"]
        #     #         )

        #     #     # -------------------------------------------------
        #     #     # HIGHLIGHT HIGHLY RATED PLACES
        #     #     # -------------------------------------------------

        #     #     if float(place["Ratings"]) >= 4.5:

        #     #         st.success(
        #     #             "🌟 Highly Recommended Place"
        #     #         )

        #     #     # -------------------------------------------------
        #     #     # HIGHLIGHT NEWLY OPENED PLACES
        #     #     # -------------------------------------------------

        #     #     if place["Newly_Opened"] == "Yes":

        #     #         st.info(
        #     #             "🆕 Newly Opened"
        #     #         )

        #     # # -------------------------------------------------
        #     # # SEPARATOR
        #     # # -------------------------------------------------

        #     # st.divider()
