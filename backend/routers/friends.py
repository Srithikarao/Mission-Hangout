from fastapi import APIRouter, HTTPException
from backend.database import friends_df
from backend.models import Friends

router = APIRouter(
    prefix="/friends",
    tags=["Friends Hangout Places"]
)

# ----------------------------------------
# View All Friends Places
# ----------------------------------------
@router.get("/")
def get_all_friends_places():

    return friends_df.fillna("").to_dict(
        orient="records"
    )



# ----------------------------------------
# Search by Place Name
# ----------------------------------------
@router.get("/search/{name}")
def search_place(name: str):

    result = friends_df[
        friends_df["Place_Name"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Filter by Category
# ----------------------------------------
@router.get("/category/{category}")
def category_filter(category: str):

    result = friends_df[
        friends_df["Category"].str.contains(
            category,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Filter by Rating
# ----------------------------------------
@router.get("/rating/{rating}")
def rating_filter(rating: float):

    result = friends_df[
        friends_df["Ratings"] >= rating
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Filter by Budget
# ----------------------------------------
@router.get("/budget/{budget}")
def budget_filter(budget: str):

    result = friends_df[
        friends_df["Average_Cost"].str.contains(
            budget,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Filter by Activity
# ----------------------------------------
@router.get("/activity/{activity}")
def activity_filter(activity: str):

    result = friends_df[
        friends_df["Activities"].str.contains(
            activity,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Filter by Group Size
# ----------------------------------------
@router.get("/groupsize/{size}")
def group_size_filter(size: str):

    result = friends_df[
        friends_df["Group_Size"].str.contains(
            size,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Sort by Rating
# ----------------------------------------
@router.get("/sort/rating")
def sort_by_rating():

    result = friends_df.sort_values(
        by="Ratings",
        ascending=False
    )

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# Sort by Name
# ----------------------------------------
@router.get("/sort/name")
def sort_by_name():

    result = friends_df.sort_values(
        by="Place_Name"
    )

    return result.fillna("").to_dict(
        orient="records"
    )


# ----------------------------------------
# View Place by ID
# ----------------------------------------
@router.get("/{place_id}")
def get_place(place_id: str):

    result = friends_df[
        friends_df["Place_ID"] == place_id
    ]

    if result.empty:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    return result.fillna("").to_dict(
        orient="records"
    )







# ----------------------------------------
# Add New Place
# ----------------------------------------
@router.post("/")
def add_place(place: Friends):

    global friends_df

    friends_df.loc[len(friends_df)] = place.dict()

    return {
        "message": "Friends hangout place added successfully."
    }


# ----------------------------------------
# Update Place
# ----------------------------------------
@router.put("/{place_id}")
def update_place(place_id: str, place: Friends):

    global friends_df

    index = friends_df[
        friends_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    friends_df.loc[index[0]] = place.dict()

    return {
        "message": "Friends hangout place updated successfully."
    }


# ----------------------------------------
# Delete Place
# ----------------------------------------
@router.delete("/{place_id}")
def delete_place(place_id: str):

    global friends_df

    index = friends_df[
        friends_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Place not found."
        )

    friends_df.drop(index=index, inplace=True)

    return {
        "message": "Friends hangout place deleted successfully."
    }