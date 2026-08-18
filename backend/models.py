from pydantic import BaseModel

class Food(BaseModel):

    Place_ID:str
    Place_Name:str
    Category:str
    Cuisine:str
    Address:str
    Area:str
    Google_Maps_Link:str
    Opening_Time:str
    Closing_Time:str
    Ratings:float
    Reviews:int
    Average_Price:str
    Best_Known_For:str
    Newly_Opened:str
    Popular_Dishes:str
    Veg_NonVeg:str
    Indoor:str
    Outdoor:str
    Family_Friendly:str
    Friends_Friendly:str
    Couples_Friendly:str
    Parking:str
    


class Chill(BaseModel):
    Place_ID:str	
    Place_Name:str
    Category:str	
    Address	:str
    Area:str	
    Google_Maps_Link:str
    Best_Known_For:str	
    Best_Time:str
    Entry_Fee:str	
    Opening_Time:str	
    Closing_Time:str	
    Ratings:float
    Activities:str
    Parking:str
    Suitable_For:str

class Family(BaseModel):
    Place_ID:int	
    Place_Name:str
    Category:str
    Suitable:str
    Age:int
    Ratings:float	
    Average_Price:int
    Timings:str
    Google_Maps_Link:str
    Best_Known_For:str
    Family_Score:int
    Family_Friendly:str
    Friends_Friendly:str
    Couples_Friendly:str
    Parking:str
    Entry_Fee:int

class Friends(BaseModel):
    Place_ID:int
    Place_Name:str	
    Category:str	
    Ratings:float
    Timings:str
    Average_Cost:int	
    Best_Known_For:str	
    Activities:str
    Google_Maps_Link:str
    Group_Size:int
    Entry_Fee:int


