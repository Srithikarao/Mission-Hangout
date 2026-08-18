

# ==========================================================
# MISSION HANGOUT
# FAVOURITES COMPONENT
# ==========================================================

"""
This file ONLY manages favourite data.

Responsibilities
----------------
✔ Create favourites.json
✔ Load favourites
✔ Save favourites
✔ Add favourite
✔ Remove favourite
✔ Check favourite
✔ Clear favourites

NOTE:
This file DOES NOT display any Streamlit UI.
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import json
import os


# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FOLDER = os.path.join(
    BASE_DIR,
    "data"
)

FAVOURITES_FILE = os.path.join(
    DATA_FOLDER,
    "favourites.json"
)


# ==========================================================
# CREATE JSON FILE
# ==========================================================

def initialize_favourites():

    """
    Creates favourites.json if it does not exist.
    """

    if not os.path.exists(DATA_FOLDER):

        os.makedirs(DATA_FOLDER)

    if not os.path.exists(FAVOURITES_FILE):

        with open(
            FAVOURITES_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file, indent=4)


# ==========================================================
# LOAD FAVOURITES
# ==========================================================

def load_favourites():

    """
    Returns all saved favourites.
    """

    initialize_favourites()

    try:

        with open(
            FAVOURITES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return []


# ==========================================================
# SAVE FAVOURITES
# ==========================================================

def save_favourites(favourites):

    """
    Saves favourites into JSON file.
    """

    with open(
        FAVOURITES_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            favourites,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================================
# CHECK FAVOURITE
# ==========================================================

def is_favourite(place_id):

    """
    Returns True if place already exists.
    """

    favourites = load_favourites()

    for place in favourites:

        if place.get("Place_ID") == place_id:

            return True

    return False


# ==========================================================
# ADD FAVOURITE
# ==========================================================

def add_favourite(place):

    """
    Adds a place to favourites.
    """

    favourites = load_favourites()

    if is_favourite(place["Place_ID"]):

        return False

    favourites.append(place)

    save_favourites(favourites)

    return True


# ==========================================================
# REMOVE FAVOURITE
# ==========================================================

def remove_favourite(place_id):

    """
    Removes a place from favourites.
    """

    favourites = load_favourites()

    favourites = [

        place

        for place in favourites

        if place.get("Place_ID") != place_id

    ]

    save_favourites(favourites)

    return True


# ==========================================================
# CLEAR FAVOURITES
# ==========================================================

def clear_favourites():

    """
    Removes every favourite.
    """

    save_favourites([])


# ==========================================================
# TOTAL FAVOURITES
# ==========================================================

def total_favourites():

    """
    Returns total number of favourites.
    """

    return len(load_favourites())