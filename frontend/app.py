import streamlit as st
import time 

from streamlit_option_menu import option_menu
from styles import load_css

# Import food page functions
from pages.Food import show_food_page

# import chillout page functions
from pages.Chillout import show_chill_page


from pages.Events import show_events_page


# for family 
from pages.Family import show_family_page

# fro friends
from pages.Friends import show_friends_page


# dice part

from components.dice import show_dice

from components.recommendation import show_recommendation

from components.search import show_search

from pages.Favourites import show_favourites_page



from pages.Recent import show_recent_page


# maps
from pages.Map import show_map_page


# Page Configuration
st.set_page_config(
    page_title="MISSION HANGOUT",
    page_icon="🎯",
    layout="wide"
)

# Load CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Sidebar
st.sidebar.title("MISSION HANGOUT")

# Navigation
selected = option_menu(

    menu_title=None,

    options=[

        "Home",

        "Food",

        "Chillout",

        "Events & Workshops",

        "Family",

        "Friends",

        "Favourites",

        "Recently Viewed",

         "Map"

    ],

    icons=[

        "house",

        "cup-hot",

        "tree",

        "ticket",

        "people",

        "person-hearts",

        "heart-fill",


        "clock-history"

    ],

    default_index=0

)






# selected = option_menu(
#     menu_title=None,
#     options=[
#         "Home",
#         "Food",
#         "Chillout",
#         "Family",
#         "Friends"
#     ],
#     icons=[
#         "house",
#         "cup-hot",
#         "tree",
#         "people",
#         "emoji-smile"
#     ],
#     orientation="horizontal"
# )





# -----------------------------
# HOME PAGE
# -----------------------------

if selected == "Home":

    # ------------------------------------------------------
    # TITLE
    # ------------------------------------------------------

    st.title("🎯 MISSION HANGOUT")

    st.write(
        """
        Welcome to Mission Hangout!

        Discover amazing restaurants, cafes,
        lakes, parks, temples and beautiful
        hangout places in Warangal.
        """
    )

    st.divider()

    # ======================================================
    # GLOBAL SEARCH
    # ======================================================

    show_search()

    st.divider()

    # ======================================================
    # DICE FEATURE
    # ======================================================

    show_dice()

    st.divider()

    # ======================================================
    # QUICK STATISTICS
    # ======================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(

            "🍽 Food",

            364

        )

    with col2:

        st.metric(

            "🌳 Chillout",

            110

        )


    with col3:

        st.metric(

            "🌳 Events_Workshops",

            10

        )



    with col4:

        st.metric(

            "👨‍👩‍👧 Family",

            20

        )

    with col5:

        st.metric(

            "👥 Friends",

            20

        )

    st.divider()

    # ======================================================
    # FEATURED CATEGORIES
    # ======================================================

    st.subheader("✨ Explore Categories")

    c1, c2 = st.columns(2)

    with c1:

        st.info("🍽 Restaurants & Cafes")

        st.info("🌳 Chillout Places")

    with c2:

        st.info("👨‍👩‍👧 Family Places")

        st.info("👥 Friends Hangouts")

  

# -----------------------------
# FOOD PAGE
# -----------------------------
elif selected == "Food":
    show_food_page()

# -----------------------------
# Other pages
# -----------------------------

elif selected == "Events & Workshops":
    show_events_page()

elif selected == "Chillout":
    show_chill_page()


elif selected == "Family":
    show_family_page()



elif selected == "Friends":
    show_friends_page()


elif selected == "Favourites":
    show_favourites_page()

elif selected=="Recently Viewed":

    show_recent_page()

elif selected == "Map":

    show_map_page()