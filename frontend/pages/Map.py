# ==========================================================
# MISSION HANGOUT
# INTERACTIVE MAP
# ==========================================================

import streamlit as st
import folium
import re

from streamlit_folium import st_folium

from api import (
    get_all_food,
    get_all_chill_places,
    get_all_family_places,
    get_all_friends_places
)


# ==========================================================
# EXTRACT COORDINATES FROM GOOGLE MAPS LINK
# ==========================================================

def extract_coordinates(google_link):

    """
    Tries to extract latitude and longitude
    from a Google Maps URL.

    Example:

    https://www.google.com/maps/@17.9784,79.5941,15z

    returns:

    17.9784, 79.5941
    """

    if not google_link:

        return None, None

    try:

        pattern = r"@(-?\d+\.\d+),(-?\d+\.\d+)"

        match = re.search(
            pattern,
            google_link
        )

        if match:

            latitude = float(
                match.group(1)
            )

            longitude = float(
                match.group(2)
            )

            return latitude, longitude

    except Exception:

        pass

    return None, None


# ==========================================================
# GET ALL PLACES
# ==========================================================

def get_all_places():

    places = []

    # ------------------------------------------------------
    # FOOD
    # ------------------------------------------------------

    try:

        food = get_all_food()

        if food:

            for place in food:

                place["Map_Category"] = "Food"

            places.extend(food)

    except Exception:

        pass

    # ------------------------------------------------------
    # CHILLOUT
    # ------------------------------------------------------

    try:

        chill = get_all_chill_places()

        if chill:

            for place in chill:

                place["Map_Category"] = "Chillout"

            places.extend(chill)

    except Exception:

        pass

    # ------------------------------------------------------
    # FAMILY
    # ------------------------------------------------------

    try:

        family = get_all_family_places()

        if family:

            for place in family:

                place["Map_Category"] = "Family"

            places.extend(family)

    except Exception:

        pass

    # ------------------------------------------------------
    # FRIENDS
    # ------------------------------------------------------

    try:

        friends = get_all_friends_places()

        if friends:

            for place in friends:

                place["Map_Category"] = "Friends"

            places.extend(friends)

    except Exception:

        pass

    return places


# ==========================================================
# SHOW MAP PAGE
# ==========================================================

def show_map_page():

    st.title("🗺️ Explore Mission Hangout")

    st.write(
        """
        Explore restaurants, cafes, lakes, parks,
        temples and other hangout places on the map.
        """
    )

    st.divider()

    # ------------------------------------------------------
    # LOAD PLACES
    # ------------------------------------------------------

    with st.spinner("Loading places..."):

        places = get_all_places()

    if not places:

        st.warning(
            "Unable to load places from the backend."
        )

        return

    # ------------------------------------------------------
    # CREATE MAP
    # ------------------------------------------------------

    map_center = [
        17.9784,
        79.5941
    ]

    hangout_map = folium.Map(

        location=map_center,

        zoom_start=12

    )

    marker_count = 0

    # ------------------------------------------------------
    # ADD MARKERS
    # ------------------------------------------------------

    for place in places:

        google_link = place.get(
            "Google_Maps_Link",
            ""
        )

        latitude, longitude = extract_coordinates(
            google_link
        )

        if latitude is None:

            continue

        if longitude is None:

            continue

        name = place.get(
            "Place_Name",
            "Unknown Place"
        )

        rating = place.get(
            "Ratings",
            "N/A"
        )

        category = place.get(
            "Map_Category",
            "Place"
        )

        popup_html = f"""
        <div style="width:220px">

            <h4>{name}</h4>

            <p>
                ⭐ Rating: {rating}
            </p>

            <p>
                🏷 Category: {category}
            </p>

        </div>
        """

        folium.Marker(

            location=[
                latitude,
                longitude
            ],

            tooltip=name,

            popup=folium.Popup(
                popup_html,
                max_width=300
            )

        ).add_to(hangout_map)

        marker_count += 1

    # ------------------------------------------------------
    # DISPLAY MAP
    # ------------------------------------------------------

    st_folium(

        hangout_map,

        width=None,

        height=600

    )

    # ------------------------------------------------------
    # MARKER INFORMATION
    # ------------------------------------------------------

    st.divider()

    st.success(
        f"📍 {marker_count} places available on the map."
    )

    if marker_count == 0:

        st.warning(
            """
            No coordinates were found.

            Make sure your Google Maps links contain
            latitude and longitude coordinates.
            """
        )