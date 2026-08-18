# ==========================================================
# MISSION HANGOUT
# EVENTS & WORKSHOPS PAGE
# ==========================================================

import streamlit as st

from api import (
    get_all_events,
    search_events
)

from components.favourites import (
    is_favourite,
    add_favourite,
    remove_favourite
)

# ==========================================================
# HELPER
# ==========================================================

def clean_value(value, default="Not Available"):

    if value is None:

        return default

    value = str(value).strip()

    if value == "":
        return default

    if value.lower() in [
        "nan",
        "none",
        "not available",
        "google maps",
        "instagram_account"
    ]:

        return default

    return value


# ==========================================================
# VALID GOOGLE MAPS URL
# ==========================================================

def valid_maps_url(value):

    if not value:

        return False

    value = str(value).strip()

    return (
        value.startswith("http://")
        or value.startswith("https://")
    )


# ==========================================================
# VALID INSTAGRAM URL
# ==========================================================

def valid_instagram_url(value):

    if not value:

        return False

    value = str(value).strip()

    return (
        "instagram.com"
        in value.lower()
        and
        (
            value.startswith("http://")
            or
            value.startswith("https://")
        )
    )


# ==========================================================
# IMAGE VALIDATION
# ==========================================================

def valid_image_url(value):

    if not value:

        return False

    value = str(value).strip()

    # Reject Google Maps values
    if "maps.google" in value.lower():

        return False

    if "maps.app.goo.gl" in value.lower():

        return False

    if value.lower() == "google maps":

        return False

    # Basic image extension check
    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".gif"
    )

    return value.lower().endswith(
        image_extensions
    )


# ==========================================================
# EVENT CARD
# ==========================================================

def show_event_card(event):

    place_id = clean_value(
        event.get("Place_ID")
    )

    place_name = clean_value(
        event.get("Place_Name")
    )

    category = clean_value(
        event.get("Category")
    )

    address = clean_value(
        event.get("Address")
    )

    area = clean_value(
        event.get("Area")
    )

    event_name = clean_value(
        event.get("Event_Workshop")
    )

    date = clean_value(
        event.get("Date")
    )

    time = clean_value(
        event.get("Time")
    )

    individual_group = clean_value(
        event.get("Individual_Group")
    )

    fee = clean_value(
        event.get("Fee")
    )

    opening_time = clean_value(
        event.get("Opening_Time")
    )

    closing_time = clean_value(
        event.get("Closing_Time")
    )

    rating = clean_value(
        event.get("Ratings")
    )

    reviews = clean_value(
        event.get("Reviews")
    )

    google_maps = event.get(
        "Google_Maps_Link"
    )

    instagram = event.get(
        "Instagram_Account"
    )


# ======================================================
# FAVORITE BUTTON
# ======================================================

    st.divider()

    if is_favourite(place_id):

        if st.button(
            "❤️ Remove from Favorites",
            key=f"event_remove_favourite_{place_id}"
        ):

            remove_favourite(
                place_id
            )

            st.success(
                f"{place_name} removed from Favorites"
            )

            st.rerun()

    else:

        if st.button(
            "🤍 Add to Favorites",
            key=f"event_add_favourite_{place_id}"
        ):

            add_favourite(
                event
            )

            st.success(
                f"{place_name} added to Favorites"
            )

            st.rerun()













    image_url = event.get(
        "Image_URL"
    )


    # ======================================================
    # CARD
    # ======================================================

    with st.container(
        border=True
    ):

        # --------------------------------------------------
        # IMAGE
        # --------------------------------------------------

        if valid_image_url(image_url):

            st.image(
                image_url,
                use_container_width=True
            )

        else:

            st.info(
                "📷 Image not available yet"
            )


        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        st.subheader(
            f"🎨 {event_name}"
        )

        st.write(
            f"📍 **{place_name}**"
        )

        st.write(
            f"🏷️ **Category:** {category}"
        )

        st.write(
            f"📅 **Date:** {date}"
        )

        st.write(
            f"⏰ **Event Time:** {time}"
        )

        st.write(
            f"👥 **Suitable For:** {individual_group}"
        )

        st.write(
            f"💰 **Fee:** {fee}"
        )

        st.write(
            f"⭐ **Rating:** {rating}"
        )

        st.write(
            f"📝 **Reviews:** {reviews}"
        )

        st.write(
            f"📍 **Area:** {area}"
        )

        st.write(
            f"🏠 **Address:** {address}"
        )

        st.write(
            f"🕐 **Opening:** {opening_time}"
        )

        st.write(
            f"🕐 **Closing:** {closing_time}"
        )


        # --------------------------------------------------
        # LINKS
        # --------------------------------------------------

        col1, col2 = st.columns(2)


        # Google Maps
        if valid_maps_url(google_maps):

            with col1:

                st.link_button(
                    "🗺️ Google Maps",
                    google_maps,
                    key=f"event_map_{place_id}"
                )


        # Instagram
        if valid_instagram_url(instagram):

            with col2:

                st.link_button(
                    "📸 Instagram",
                    instagram,
                    key=f"event_instagram_{place_id}"
                )


# ==========================================================
# EVENTS PAGE
# ==========================================================

def show_events_page():

    st.title(
        "🎨 Events & Workshops"
    )

    st.write(
        """
        Discover workshops, creative activities,
        cultural events and special experiences
        around Warangal.
        """
    )

    st.divider()


    # ======================================================
    # SEARCH
    # ======================================================

    search = st.text_input(
        "🔍 Search Events & Workshops",
        placeholder="Try pottery, music, workshop, art..."
    )


    # ======================================================
    # LOAD DATA
    # ======================================================

    if search.strip():

        events = search_events(
            search.strip()
        )

    else:

        events = get_all_events()


    # ======================================================
    # NO RESULTS
    # ======================================================

    if not events:

        st.warning(
            "No events or workshops found."
        )

        return


    # ======================================================
    # RESULT COUNT
    # ======================================================

    st.success(
        f"{len(events)} event(s) found"
    )

    st.divider()


    # ======================================================
    # DISPLAY EVENTS
    # ======================================================

    for event in events:

        show_event_card(
            event
        )

        st.divider()