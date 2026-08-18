from fastapi import APIRouter
from backend.database import food_df
from backend.models import Food

router = APIRouter(
    prefix="/food",
    tags=["Food"]
)

# view all
@router.get("/")
def get_all_food():

    return food_df.fillna("").to_dict(
        orient="records"
    )




# search by name
@router.get("/search/{name}")

def search_food(name:str):
    result = food_df[
    food_df["Place_Name"]
    .astype(str)
    .str.contains(
        name,
        case=False,
        na=False
    )
]

    return result.fillna("").to_dict(
        orient="records"
    )


# filter by name
@router.get("/category/{category}")

def category(category:str):

    result = food_df[
        food_df["Category"]
        .str.lower()==category.lower()
    ]

    return result.fillna("").to_dict(
        orient="records"
    )


# filter by cuisine
@router.get("/cuisine/{cuisine}")

def cuisine(cuisine:str):

    result = food_df[
        food_df["Cuisine"]
        .str.contains(cuisine,
        case=False)
    ]

    return result.fillna("").to_dict(
        orient="records"
    )

# rating filter
@router.get("/rating/{rating}")

def rating(rating:float):

    result = food_df[
        food_df["Ratings"]>=rating
    ]

    return result.fillna("").to_dict(
        orient="records"
    )

# newly opened
@router.get("/new")

def newly_opened():

    result = food_df[
        food_df["Newly_Opened"]=="Yes"
    ]

    return result.fillna("").to_dict(
        orient="records"
    )

# sort by rating
@router.get("/sort/rating")

def sort_rating():

    result = food_df.sort_values(
        by="Ratings",
        ascending=False
    )

    return result.fillna("").to_dict(
        orient="records"
    )

# sort alphabetically
@router.get("/sort/name")

def sort_name():

    result = food_df.sort_values(
        by="Place_Name"
    )

    return result.fillna("").to_dict(
        orient="records"
    )


# get by ID
@router.get("/{place_id}")

def get_food(place_id:str):

    result = food_df[
        food_df["Place_ID"]==place_id
    ]

    if result.empty:
        return {"message":"Place not found"}

    return result.fillna("").to_dict(
        orient="records"
    )




# add place
@router.post("/")

def add_place(place:Food):

    global food_df

    food_df.loc[len(food_df)] = place.dict()

    return {
        "message":"Place Added"
    }

# update 
@router.put("/{place_id}")

def update_place(place_id:str,
                 place:Food):

    global food_df

    index = food_df[
        food_df["Place_ID"]==place_id
    ].index

    if len(index)==0:

        return {
            "message":"Not Found"
        }

    food_df.loc[index[0]] = place.dict()

    return {
        "message":"Updated"
    }

# delete 
@router.delete("/{place_id}")

def delete_place(place_id:str):

    global food_df

    index = food_df[
        food_df["Place_ID"]==place_id
    ].index

    if len(index)==0:

        return {
            "message":"Not Found"
        }

    food_df = food_df.drop(index)

    return {
        "message":"Deleted"
    }