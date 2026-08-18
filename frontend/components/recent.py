# ==========================================================
# MISSION HANGOUT
# RECENTLY VIEWED COMPONENT
# ==========================================================

"""
This component manages Recently Viewed Places.

Responsibilities
-----------------

✔ Create recent.json

✔ Load recent places

✔ Save recent places

✔ Add place

✔ Remove place

✔ Remove duplicates

✔ Keep latest 20 places

✔ Clear history

NO STREAMLIT UI HERE
"""

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import os
import json

# ==========================================================
# PROJECT PATH
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

RECENT_FILE = os.path.join(
    DATA_FOLDER,
    "recent.json"
)

MAX_RECENT = 20


# ==========================================================
# CREATE recent.json
# ==========================================================

def initialize_recent():

    """
    Creates recent.json
    if it doesn't exist.
    """

    if not os.path.exists(DATA_FOLDER):

        os.makedirs(DATA_FOLDER)

    if not os.path.exists(RECENT_FILE):

        with open(

            RECENT_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                [],

                file,

                indent=4

            )


# ==========================================================
# LOAD RECENT
# ==========================================================

def load_recent():

    """
    Returns all recently viewed places.
    """

    initialize_recent()

    try:

        with open(

            RECENT_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)

    except Exception:

        return []


# ==========================================================
# SAVE RECENT
# ==========================================================

def save_recent(recent):

    """
    Saves recent places.
    """

    with open(

        RECENT_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            recent,

            file,

            indent=4,

            ensure_ascii=False

        )


# ==========================================================
# ADD RECENT PLACE
# ==========================================================

def add_recent(place):

    """
    Adds a place into Recently Viewed.

    If already exists,

    remove old copy

    and move it to top.
    """

    recent = load_recent()

    place_id = place.get(

        "Place_ID",

        ""

    )

    if place_id == "":

        return

    # ----------------------------------------
    # Remove old copy
    # ----------------------------------------

    recent = [

        item

        for item in recent

        if item.get("Place_ID") != place_id

    ]

    # ----------------------------------------
    # Insert at beginning
    # ----------------------------------------

    place["Viewed_Time"] = str(

        __import__("datetime")

        .datetime.now()

    )

    recent.insert(

        0,

        place

    )
    # ----------------------------------------
    # Keep latest MAX_RECENT places
    # ----------------------------------------

    recent = recent[:MAX_RECENT]

    save_recent(recent)


# ==========================================================
# REMOVE ONE PLACE
# ==========================================================

def remove_recent(place_id):

    """
    Removes one place from history.
    """

    recent = load_recent()

    recent = [

        item

        for item in recent

        if item.get("Place_ID") != place_id

    ]

    save_recent(recent)


# ==========================================================
# CLEAR HISTORY
# ==========================================================

def clear_recent():

    """
    Clears entire history.
    """

    save_recent([])


# ==========================================================
# TOTAL HISTORY
# ==========================================================

def total_recent():

    """
    Returns total viewed places.
    """

    return len(

        load_recent()

    )


# ==========================================================
# CHECK IF EXISTS
# ==========================================================

def recent_exists(place_id):

    """
    Returns True
    if place already exists.
    """

    recent = load_recent()

    for item in recent:

        if item.get("Place_ID") == place_id:

            return True

    return False