from fastapi import APIRouter, HTTPException
from backend.database import family_df
from backend.models import Family

router = APIRouter(
    prefix="/family",
    tags=["Family Places"]
)

# ----------------------------------------
# View All Family Places
# ----------------------------------------
@router.get("/")
def get_all_family_places():
    return family_df.fillna("").to_dict(orient="records")



# ----------------------------------------
# Search by Place Name
# ----------------------------------------
@router.get("/search/{name}")
def search_place(name: str):

    result = family_df[
        family_df["Place_Name"].str.contains(
            name,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Filter by Category
# ----------------------------------------
@router.get("/category/{category}")
def category_filter(category: str):

    result = family_df[
        family_df["Category"].str.contains(
            category,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Filter by Rating
# ----------------------------------------
@router.get("/rating/{rating}")
def rating_filter(rating: float):

    result = family_df[
        family_df["Ratings"] >= rating
    ]

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Filter by Budget
# ----------------------------------------
@router.get("/budget/{budget}")
def budget_filter(budget: str):

    result = family_df[
        family_df["Average_Price"].str.contains(
            budget,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Filter by Suitable Age
# ----------------------------------------
@router.get("/age/{age}")
def age_filter(age: str):

    result = family_df[
        family_df["Suitable_Age"].str.contains(
            age,
            case=False,
            na=False
        )
    ]

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Sort by Rating
# ----------------------------------------
@router.get("/sort/rating")
def sort_rating():

    result = family_df.sort_values(
        by="Ratings",
        ascending=False
    )

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# Sort by Place Name
# ----------------------------------------
@router.get("/sort/name")
def sort_name():

    result = family_df.sort_values(
        by="Place_Name"
    )

    return result.fillna("").to_dict(orient="records")


# ----------------------------------------
# View Place by ID
# ----------------------------------------
@router.get("/{place_id}")
def get_family_place(place_id: str):

    result = family_df[
        family_df["Place_ID"] == place_id
    ]

    if result.empty:
        raise HTTPException(
            status_code=404,
            detail="Family place not found."
        )

    return result.fillna("").to_dict(orient="records")








# ----------------------------------------
# Add New Family Place
# ----------------------------------------
@router.post("/")
def add_family_place(place: Family):

    global family_df

    family_df.loc[len(family_df)] = place.dict()

    return {
        "message": "Family place added successfully."
    }


# ----------------------------------------
# Update Family Place
# ----------------------------------------
@router.put("/{place_id}")
def update_family_place(place_id: str, place: Family):

    global family_df

    index = family_df[
        family_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Family place not found."
        )

    family_df.loc[index[0]] = place.dict()

    return {
        "message": "Family place updated successfully."
    }


# ----------------------------------------
# Delete Family Place
# ----------------------------------------
@router.delete("/{place_id}")
def delete_family_place(place_id: str):

    global family_df

    index = family_df[
        family_df["Place_ID"] == place_id
    ].index

    if len(index) == 0:
        raise HTTPException(
            status_code=404,
            detail="Family place not found."
        )

    family_df.drop(index=index, inplace=True)

    return {
        "message": "Family place deleted successfully."
    }