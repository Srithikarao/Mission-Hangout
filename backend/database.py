# # import pandas as pd

# # import os

# # print("Current Working Directory:")
# # print(os.getcwd())

# # FILE = r"C:\Users\srith\OneDrive\Desktop\hangout fastapi\Warangal_Hangout_Dataset.xlsx"

# # food_df = pd.read_excel(FILE, sheet_name="Food")
# # chill_df = pd.read_excel(FILE, sheet_name="Chillout")
# # events_df = pd.read_excel(FILE, sheet_name="Events_Workshops")
# # family_df = pd.read_excel(FILE, sheet_name="Family")
# # friends_df = pd.read_excel(FILE, sheet_name="Friends")





# from pathlib import Path
# import pandas as pd


# # ==========================================================
# # EXCEL FILE LOCATION
# # ==========================================================

# BASE_DIR = Path(__file__).resolve().parent.parent

# FILE = BASE_DIR / "Warangal_Hangout_Dataset.xlsx"


# # ==========================================================
# # CHECK WHETHER EXCEL FILE EXISTS
# # ==========================================================

# # print("Excel file location:")
# # print(FILE)

# # print("Excel file exists:")
# # print(FILE.exists())


# # ==========================================================
# # LOAD EXCEL SHEETS
# # ==========================================================

# food_df = pd.read_excel(
#     FILE,
#     sheet_name="Food"
# )

# chill_df = pd.read_excel(
#     FILE,
#     sheet_name="Chillout"
# )

# family_df = pd.read_excel(
#     FILE,
#     sheet_name="Family"
# )

# friends_df = pd.read_excel(
#     FILE,
#     sheet_name="Friends"
# )

# events_df = pd.read_excel(
#     FILE,
#     sheet_name="Events_Workshops"
# )



import pandas as pd
from pathlib import Path


# =========================================================
# EXCEL FILE PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

FILE = BASE_DIR / "data" / "Warangal_Hangout_Dataset.xlsx"


# =========================================================
# CHECK WHETHER FILE EXISTS
# =========================================================

print("Excel file location:")
print(FILE)

print("Does Excel file exist?")
print(FILE.exists())


# =========================================================
# LOAD FOOD
# =========================================================

food_df = pd.read_excel(
    FILE,
    sheet_name="Food"
)


# =========================================================
# LOAD CHILLOUT
# =========================================================

chill_df = pd.read_excel(
    FILE,
    sheet_name="Chillout"
)


# =========================================================
# LOAD FAMILY
# =========================================================

family_df = pd.read_excel(
    FILE,
    sheet_name="Family"
)


# =========================================================
# LOAD FRIENDS
# =========================================================

friends_df = pd.read_excel(
    FILE,
    sheet_name="Friends"
)


# =========================================================
# LOAD EVENTS & WORKSHOPS
# =========================================================

events_df = pd.read_excel(
    FILE,
    sheet_name="Events_Workshops"
)



# =========================================================
# PRINT DATA INFORMATION
# =========================================================

# print("\n================ DATABASE LOADED ================\n")

# print("Food rows:", len(food_df))
# print("Chillout rows:", len(chill_df))
# print("Family rows:", len(family_df))
# print("Friends rows:", len(friends_df))
# print("Events rows:", len(events_df))

# print("\n=================================================\n")