# displays images, name, rating , category, timings, maps, favourites, view details of 4 pages



# ==========================================================
# MISSION HANGOUT
# PLACE CARD COMPONENT
# ==========================================================

"""
This component displays a complete place card.

Every page (Food, Chillout, Family, Friends,
Search and Dice) will use this component.

Advantages

✓ One design everywhere
✓ Easy maintenance
✓ No duplicate code
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


from components.recent import add_recent

# ==========================================================
# IMAGE PATH
# ==========================================================

BASE_DIR = os.path.dirname(

    os.path.dirname(

        os.path.abspath(__file__)

    )

)

# ==========================================================
# SHOW IMAGE
# ==========================================================

def show_image(place):

    """
    Displays place image.

    Image name should match Place_ID.

    Example

    images/

        F001.jpg

        F002.jpg

        C001.jpg

    If image is missing,

    default.jpg will be shown.
    """

    image_path = os.path.join(

        BASE_DIR,

        "images",

        f"{place['Place_ID']}.jpg"

    )

    image = load_image(image_path)

    if image:

        st.image(

            image,

            use_container_width=True

        )

    else:

        st.warning(

            "Image not available"

        )

# ==========================================================
# BASIC DETAILS
# ==========================================================

def show_basic_details(place):

    """
    Displays the important details
    about the selected place.
    """

    st.subheader(

        place["Place_Name"]

    )

    # ------------------------------------------------------
    # Rating
    # ------------------------------------------------------

    if "Ratings" in place:

        st.write(

            "⭐ Rating :",

            place["Ratings"]

        )

    # ------------------------------------------------------
    # Cuisine
    # ------------------------------------------------------

    if "Cuisine" in place:

        st.write(

            "🍜 Cuisine :",

            place["Cuisine"]

        )

    # ------------------------------------------------------
    # Category
    # ------------------------------------------------------

    if "Category" in place:

        st.write(

            "🏷 Category :",

            place["Category"]

        )

    # ------------------------------------------------------
    # Price
    # ------------------------------------------------------

    if "Average_Price" in place:

        st.write(

            "💰 Price :",

            place["Average_Price"]

        )

    elif "Entry_Fee" in place:

        st.write(

            "💰 Entry Fee :",

            place["Entry_Fee"]

        )

    # ------------------------------------------------------
    # Timings
    # ------------------------------------------------------

    opening = place.get(

        "Opening_Time",

        ""

    )

    closing = place.get(

        "Closing_Time",

        ""

    )

    if opening != "" and closing != "":

        st.write(

            "🕒 Timings :",

            opening,

            "-",

            closing

        )

    # ------------------------------------------------------
    # Best Known For
    # ------------------------------------------------------

    if "Best_Known_For" in place:

        st.write(

            "🔥 Best Known For :",

            place["Best_Known_For"]

        )

    elif "Description" in place:

        st.write(

            "📖 Description :",

            place["Description"]

        )

    st.write("")



# ==========================================================
# GOOGLE MAPS BUTTON
# ==========================================================

def show_google_maps(place):

    """
    Displays the Google Maps button
    if the place contains a Google Maps link.
    """

    google_link = place.get("Google_Maps_Link", "")

    if google_link != "":

        st.link_button(

            "📍 Open in Google Maps",

            google_link,

            use_container_width=True

        )


# ==========================================================
# FAVOURITE BUTTON
# ==========================================================

def show_favourite_button(place, module_name="Place"):

    """
    Displays Add/Remove Favourite button.

    This function works for all modules
    like Food, Chillout, Family and Friends.
    """

    # st.button(
    #     "❤️ TEST BUTTON",
    #     key=f"test_{place['Place_ID']}"
    # )



    st.write("✅ Favourite Function Running")

    place_id = place.get("Place_ID", "")

    if place_id == "":

        return

    # ------------------------------------------------------
    # Already Favourite
    # ------------------------------------------------------

    if is_favourite(place_id):

        if st.button(

            "💔 Remove Favourite",

            key=f"{module_name}_remove_{place_id}"

        ):

            remove_favourite(place_id)

            st.success("Removed from favourites.")

            st.rerun()

    else:

        if st.button(

            "❤️ Add Favourite",

            key=f"{module_name}_add_{place_id}"

        ):

            add_favourite(place)

            st.success("Added to favourites.")

            st.balloons()

            st.rerun()






    # if is_favourite(place_id):

    #     if st.button(

    #         "💔 Remove Favourite",

    #         key=f"{module_name}_remove_{place_id}"

    #     ):

    #         remove_favourite(place_id)

    #         st.toast(

    #             "Removed from favourites."

    #         )

    #         st.rerun()

    # ------------------------------------------------------
    # Not Favourite
    # ------------------------------------------------------

    # else:

    #     if st.button(

    #         "❤️ Add Favourite",

    #         key=f"{module_name}_add_{place_id}"

    #     ):

    #         add_favourite(place)

    #         st.toast(

    #             "Added to favourites."

    #         )

    #         st.balloons()

    #         st.rerun()


# ==========================================================
# VIEW DETAILS
# ==========================================================

def show_details(place,module_name):

    """
    Shows all additional details inside
    an expandable section.
    """

    with st.expander("📄 View Complete Details"):
        if module_name != "Recent":
            add_recent(place)

        # ----------------------------------------------
        # Address
        # ----------------------------------------------

        if "Address" in place:

            st.write(

                "📍 Address :",

                place["Address"]

            )

        # ----------------------------------------------
        # Area
        # ----------------------------------------------

        if "Area" in place:

            st.write(

                "🏙 Area :",

                place["Area"]

            )

        # ----------------------------------------------
        # Popular Dishes
        # ----------------------------------------------

        if "Popular_Dishes" in place:

            st.write(

                "🍽 Popular Dishes :",

                place["Popular_Dishes"]

            )

        # ----------------------------------------------
        # Veg / Non-Veg
        # ----------------------------------------------

        if "Veg_NonVeg" in place:

            st.write(

                "🥗 Veg / Non-Veg :",

                place["Veg_NonVeg"]

            )

        # ----------------------------------------------
        # Indoor Seating
        # ----------------------------------------------

        if "Indoor" in place:

            st.write(

                "🪑 Indoor Seating :",

                place["Indoor"]

            )

        # ----------------------------------------------
        # Outdoor Seating
        # ----------------------------------------------

        if "Outdoor" in place:

            st.write(

                "🌳 Outdoor Seating :",

                place["Outdoor"]

            )

        # ----------------------------------------------
        # Family Friendly
        # ----------------------------------------------

        if "Family_Friendly" in place:

            st.write(

                "👨‍👩‍👧 Family Friendly :",

                place["Family_Friendly"]

            )

        # ----------------------------------------------
        # Friends Friendly
        # ----------------------------------------------

        if "Friends_Friendly" in place:

            st.write(

                "👨‍👩‍👦 Friends Friendly :",

                place["Friends_Friendly"]

            )

        # ----------------------------------------------
        # Couples Friendly
        # ----------------------------------------------

        if "Couples_Friendly" in place:

            st.write(

                "❤️ Couples Friendly :",

                place["Couples_Friendly"]

            )

        # ----------------------------------------------
        # Parking
        # ----------------------------------------------

        if "Parking" in place:

            st.write(

                "🚗 Parking :",

                place["Parking"]

            )

        # ----------------------------------------------
        # Newly Opened
        # ----------------------------------------------

        if "Newly_Opened" in place:

            st.write(

                "🆕 Newly Opened :",

                place["Newly_Opened"]

            )

        # ----------------------------------------------
        # Reviews
        # ----------------------------------------------

        if "Reviews" in place:

            st.write(

                "⭐ Reviews :",

                place["Reviews"]

            )

        # ----------------------------------------------
        # Generic Fields
        # (Useful for Chillout, Family & Friends)
        # ----------------------------------------------

        ignore = {

            "Place_ID",

            "Place_Name",

            "Ratings",

            "Cuisine",

            "Category",

            "Average_Price",

            "Opening_Time",

            "Closing_Time",

            "Best_Known_For",

            "Google_Maps_Link"

        }

        for key, value in place.items():

            if key not in ignore:

                if value != "":

                    st.write(

                        f"**{key.replace('_',' ')} :**",

                        value

                    )



# ==========================================================
# SHOW BADGES
# ==========================================================

def show_badges(place):

    """
    Displays badges like:
    ⭐ Highly Recommended
    🆕 Newly Opened
    """

    # ------------------------------------------------------
    # HIGHLY RATED
    # ------------------------------------------------------

    try:

        rating = float(place.get("Ratings", 0))

        if rating >= 4.5:

            st.success(

                "🌟 Highly Recommended Place"

            )

    except:

        pass

    # ------------------------------------------------------
    # NEWLY OPENED
    # ------------------------------------------------------

    if place.get("Newly_Opened", "") == "Yes":

        st.info(

            "🆕 Newly Opened"

        )


# ==========================================================
# COMPLETE PLACE CARD
# ==========================================================

def show_place_card(place, module_name="Place"):

    """
    Displays one complete place card.

    Parameters
    ----------
    place : dict

    module_name : str

    Examples

    show_place_card(place, "Food")

    show_place_card(place, "Family")

    show_place_card(place, "Friends")

    show_place_card(place, "Chillout")
    """


    # --------------------------------------------------
    # ADD TO RECENTLY VIEWED
    # --------------------------------------------------

    # Do not add again while viewing
    # the Recent page itself.

    # if module_name != "Recent":

    #     add_recent(place)






    with st.container():

        # --------------------------------------------------
        # TWO COLUMN LAYOUT
        # --------------------------------------------------

        left, right = st.columns([1,3])

        # ==================================================
        # IMAGE
        # ==================================================

        with left:

            show_image(place)

        # ==================================================
        # DETAILS
        # ==================================================

        with right:

            show_basic_details(place)

            show_google_maps(place)

            show_favourite_button(

                place,

                module_name

            )

            show_details(place, module_name)

            show_badges(place)

        # --------------------------------------------------
        # CARD SEPARATOR
        # --------------------------------------------------

        st.divider()


# ==========================================================
# END OF FILE
# ==========================================================