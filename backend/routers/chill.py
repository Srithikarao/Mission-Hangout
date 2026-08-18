from fastapi import APIRouter, HTTPException
from backend.database import chill_df
from backend.models import Chill

router = APIRouter(
    prefix="/chill",
    tags=["Chillout Places"]
)

# -------------------------------
# View All Chillout Places
# -------------------------------
@router.get("/")
def get_all_places():
    return chill_df.fillna("").to_dict(orient="records")



# -------------------------------
# Search by Place Name
# -------------------------------
@router.get("/search/{name}")
def search_place(name: str):

    result = chill_df[
        chill_df["Place_Name"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Filter by Category
# -------------------------------
@router.get("/category/{category}")
def filter_category(category: str):

    result = chill_df[
        chill_df["Category"].str.contains(
            category,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Filter by Rating
# -------------------------------
@router.get("/rating/{rating}")
def rating_filter(rating: float):

    result = chill_df[
        chill_df["Ratings"] >= rating
    ]

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Filter Free Places
# -------------------------------
@router.get("/free")
def free_places():

    result = chill_df[
        chill_df["Entry_Fee"].str.lower() == "free"
    ]

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Filter Paid Places
# -------------------------------
@router.get("/paid")
def paid_places():

    result = chill_df[
        chill_df["Entry_Fee"].str.lower() != "free"
    ]

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Sort by Ratings
# -------------------------------
@router.get("/sort/rating")
def sort_rating():

    result = chill_df.sort_values(
        by="Ratings",
        ascending=False
    )

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# Sort Alphabetically
# -------------------------------
@router.get("/sort/name")
def sort_name():

    result = chill_df.sort_values(
        by="Place_Name"
    )

    return result.fillna("").to_dict(orient="records")


# -------------------------------
# View Place by ID
# -------------------------------
@router.get("/{place_id}")
def get_place_by_id(place_id: str):

    result = chill_df[chill_df["Place_ID"] == place_id]

    if result.empty:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    return result.fillna("").to_dict(orient="records")







# -------------------------------
# Add New Place
# -------------------------------
@router.post("/")
def add_place(place: Chill):

    global chill_df

    chill_df.loc[len(chill_df)] = place.dict()

    return {
        "message": "New chillout place added successfully."
    }


# -------------------------------
# Update Place
# -------------------------------
@router.put("/{place_id}")
def update_place(place_id: str, place: Chill):

    global chill_df

    index = chill_df[
        chill_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    chill_df.loc[index[0]] = place.dict()

    return {
        "message": "Place updated successfully."
    }


# -------------------------------
# Delete Place
# -------------------------------
@router.delete("/{place_id}")
def delete_place(place_id: str):

    global chill_df

    index = chill_df[
        chill_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    chill_df.drop(index=index, inplace=True)

    return {
        "message": "Place deleted successfully."
    }