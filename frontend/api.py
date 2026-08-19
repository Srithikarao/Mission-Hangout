
# import requests


# API_URL="https://mission-hangout.onrender.com"

import os
import requests

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)


# -----------------------------
# Get All Food Places
# -----------------------------
def get_all_food():

    try:

        response = requests.get(f"{API_URL}/food")

        return response.json()

    except:

        return []


# -----------------------------
# Search by Name
# -----------------------------
def search_food(name):

    try:

        response = requests.get(
            f"{API_URL}/food/search/{name}"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Category Filter
# -----------------------------
def category_food(category):

    try:

        response = requests.get(
            f"{API_URL}/food/category/{category}"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Cuisine Filter
# -----------------------------
def cuisine_food(cuisine):

    try:

        response = requests.get(
            f"{API_URL}/food/cuisine/{cuisine}"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Rating Filter
# -----------------------------
def rating_food(rating):

    try:

        response = requests.get(
            f"{API_URL}/food/rating/{rating}"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Newly Opened
# -----------------------------
def new_food():

    try:

        response = requests.get(
            f"{API_URL}/food/new"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Sort Rating
# -----------------------------
def sort_rating():

    try:

        response = requests.get(
            f"{API_URL}/food/sort/rating"
        )

        return response.json()

    except:

        return []


# -----------------------------
# Sort Name
# -----------------------------
def sort_name():

    try:

        response = requests.get(
            f"{API_URL}/food/sort/name"
        )

        return response.json()

    except:
        return []








# ==========================================================
# CHILLOUT API FUNCTIONS
# ==========================================================


# ----------------------------------------------------------
# GET ALL CHILLOUT PLACES
# ----------------------------------------------------------

def get_all_chill_places():

    response = requests.get(

        f"{API_URL}/chill"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SEARCH PLACE
# ----------------------------------------------------------

def search_chill_place(place_name):

    response = requests.get(

        f"{API_URL}/chill/search/{place_name}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY CATEGORY
# ----------------------------------------------------------

def category_chill_place(category):

    response = requests.get(

        f"{API_URL}/chill/category/{category}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY MINIMUM RATING
# ----------------------------------------------------------

def rating_chill_place(rating):

    response = requests.get(

        f"{API_URL}/chill/rating/{rating}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FREE ENTRY PLACES
# ----------------------------------------------------------

def free_chill_places():

    response = requests.get(

        f"{API_URL}/chill/free"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# PAID ENTRY PLACES
# ----------------------------------------------------------

def paid_chill_places():

    response = requests.get(

        f"{API_URL}/chill/paid"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT BY RATING
# ----------------------------------------------------------

def sort_chill_rating():

    response = requests.get(

        f"{API_URL}/chill/sort/rating"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT ALPHABETICALLY
# ----------------------------------------------------------

def sort_chill_name():

    response = requests.get(

        f"{API_URL}/chill/sort/name"

    )

    if response.status_code == 200:

        return response.json()

    return []



# 
# ==========================================================
# FAMILY API FUNCTIONS
# ==========================================================


# ----------------------------------------------------------
# GET ALL FAMILY PLACES
# ----------------------------------------------------------

def get_all_family_places():

    response = requests.get(

        f"{API_URL}/family"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SEARCH FAMILY PLACE
# ----------------------------------------------------------

def search_family_place(place_name):

    response = requests.get(

        f"{API_URL}/family/search/{place_name}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY CATEGORY
# ----------------------------------------------------------

def category_family_place(category):

    response = requests.get(

        f"{API_URL}/family/category/{category}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY MINIMUM RATING
# ----------------------------------------------------------

def rating_family_place(rating):

    response = requests.get(

        f"{API_URL}/family/rating/{rating}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET FREE ENTRY FAMILY PLACES
# ----------------------------------------------------------

def free_family_places():

    response = requests.get(

        f"{API_URL}/family/free"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET PAID ENTRY FAMILY PLACES
# ----------------------------------------------------------

def paid_family_places():

    response = requests.get(

        f"{API_URL}/family/paid"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT BY RATING
# ----------------------------------------------------------

def sort_family_rating():

    response = requests.get(

        f"{API_URL}/family/sort/rating"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT ALPHABETICALLY
# ----------------------------------------------------------

def sort_family_name():

    response = requests.get(

        f"{API_URL}/family/sort/name"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET FAMILY PLACE BY ID
# ----------------------------------------------------------

def get_family_by_id(place_id):

    response = requests.get(

        f"{API_URL}/family/{place_id}"

    )

    if response.status_code == 200:

        return response.json()

    return {}


# ----------------------------------------------------------
# ADD NEW FAMILY PLACE
# ----------------------------------------------------------

def add_family_place(data):

    response = requests.post(

        f"{API_URL}/family",

        json=data

    )

    if response.status_code in [200, 201]:

        return response.json()

    return None


# ----------------------------------------------------------
# UPDATE FAMILY PLACE
# ----------------------------------------------------------

def update_family_place(place_id, data):

    response = requests.put(

        f"{API_URL}/family/{place_id}",

        json=data

    )

    if response.status_code == 200:

        return response.json()

    return None


# ----------------------------------------------------------
# DELETE FAMILY PLACE
# ----------------------------------------------------------

def delete_family_place(place_id):

    response = requests.delete(

        f"{API_URL}/family/{place_id}"

    )

    if response.status_code == 200:

        return response.json()

    return None



# ==========================================================
# FRIENDS API FUNCTIONS
# ==========================================================


# ----------------------------------------------------------
# GET ALL FRIENDS HANGOUT PLACES
# ----------------------------------------------------------

def get_all_friends_places():

    response = requests.get(

        f"{API_URL}/friends"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SEARCH FRIENDS PLACE
# ----------------------------------------------------------

def search_friends_place(place_name):

    response = requests.get(

        f"{API_URL}/friends/search/{place_name}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY CATEGORY
# ----------------------------------------------------------

def category_friends_place(category):

    response = requests.get(

        f"{API_URL}/friends/category/{category}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# FILTER BY MINIMUM RATING
# ----------------------------------------------------------

def rating_friends_place(rating):

    response = requests.get(

        f"{API_URL}/friends/rating/{rating}"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET FREE ENTRY FRIENDS PLACES
# ----------------------------------------------------------

def free_friends_places():

    response = requests.get(

        f"{API_URL}/friends/free"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET PAID ENTRY FRIENDS PLACES
# ----------------------------------------------------------

def paid_friends_places():

    response = requests.get(

        f"{API_URL}/friends/paid"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT FRIENDS PLACES BY RATING
# ----------------------------------------------------------

def sort_friends_rating():

    response = requests.get(

        f"{API_URL}/friends/sort/rating"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# SORT FRIENDS PLACES ALPHABETICALLY
# ----------------------------------------------------------

def sort_friends_name():

    response = requests.get(

        f"{API_URL}/friends/sort/name"

    )

    if response.status_code == 200:

        return response.json()

    return []


# ----------------------------------------------------------
# GET FRIENDS PLACE BY ID
# ----------------------------------------------------------

def get_friends_by_id(place_id):

    response = requests.get(

        f"{API_URL}/friends/{place_id}"

    )

    if response.status_code == 200:

        return response.json()

    return {}


# ----------------------------------------------------------
# ADD NEW FRIENDS PLACE
# ----------------------------------------------------------

def add_friends_place(data):

    response = requests.post(

        f"{API_URL}/friends",

        json=data

    )

    if response.status_code in [200, 201]:

        return response.json()

    return None


# ----------------------------------------------------------
# UPDATE FRIENDS PLACE
# ----------------------------------------------------------

def update_friends_place(place_id, data):

    response = requests.put(

        f"{API_URL}/friends/{place_id}",

        json=data

    )

    if response.status_code == 200:

        return response.json()

    return None


# ----------------------------------------------------------
# DELETE FRIENDS PLACE
# ----------------------------------------------------------

def delete_friends_place(place_id):

    response = requests.delete(

        f"{API_URL}/friends/{place_id}"

    )

    if response.status_code == 200:

        return response.json()

    return None





# ==========================================================
# EVENTS & WORKSHOPS
# ==========================================================

def get_all_events():

    try:

        response = requests.get(
            f"{API_URL}/events/all"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# EVENT BY ID
# ==========================================================

def get_event_by_id(place_id):

    try:

        response = requests.get(
            f"{API_URL}/events/{place_id}"
        )

        if response.status_code == 200:

            return response.json()

        return None

    except Exception:

        return None


# ==========================================================
# SEARCH EVENTS
# ==========================================================

def search_events(keyword):

    try:

        response = requests.get(
            f"{API_URL}/events/search/{keyword}"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# EVENTS BY CATEGORY
# ==========================================================

def get_events_by_category(category):

    try:

        response = requests.get(
            f"{API_URL}/events/category/{category}"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# EVENTS BY AREA
# ==========================================================

def get_events_by_area(area):

    try:

        response = requests.get(
            f"{API_URL}/events/area/{area}"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# EVENTS BY TYPE
# ==========================================================

def get_events_by_type(event_type):

    try:

        response = requests.get(
            f"{API_URL}/events/type/{event_type}"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# EVENTS BY RATING
# ==========================================================

def get_events_by_rating(minimum_rating):

    try:

        response = requests.get(
            f"{API_URL}/events/rating/{minimum_rating}"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# TOP RATED EVENTS
# ==========================================================

def get_top_rated_events():

    try:

        response = requests.get(
            f"{API_URL}/events/top-rated"
        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []