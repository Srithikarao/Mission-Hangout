# ==========================================================
# backend/routers/events.py
# MISSION HANGOUT
# Events & Workshops API
# ==========================================================

from fastapi import APIRouter, HTTPException
from backend.database import events_df


# ==========================================================
# CREATE ROUTER
# ==========================================================

router = APIRouter(
    prefix="/events",
    tags=["Events & Workshops"]
)


# ==========================================================
# GET ALL EVENTS
# URL:
# http://127.0.0.1:8000/events/all
# ==========================================================

@router.get("/all")
def get_all_events():

    try:

        # Check whether Events data exists
        if events_df is None:
            raise HTTPException(
                status_code=500,
                detail="Events data is not loaded."
            )

        # Check whether the DataFrame is empty
        if events_df.empty:
            return []

        # Replace NaN values with empty strings
        clean_df = events_df.fillna("")

        # Convert DataFrame into list of dictionaries
        events = clean_df.to_dict(
            orient="records"
        )

        return events

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to load Events_Workshops data: {str(e)}"
        )


# ==========================================================
# GET EVENT BY PLACE / EVENT NAME
#
# Example:
# /events/search/workshop
# ==========================================================

@router.get("/search/{keyword}")
def search_events(keyword: str):

    try:

        # Check whether data exists
        if events_df is None:
            raise HTTPException(
                status_code=500,
                detail="Events data is not loaded."
            )

        # If DataFrame is empty
        if events_df.empty:
            return []

        # Work on a copy
        df = events_df.fillna("").copy()

        # Convert every column to string for safe searching
        df = df.astype(str)

        # Search keyword in every column
        mask = df.apply(
            lambda column: column.str.contains(
                keyword,
                case=False,
                na=False
            )
        ).any(axis=1)

        result = df[mask]

        # Convert result to JSON-compatible format
        return result.to_dict(
            orient="records"
        )

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to search Events & Workshops: {str(e)}"
        )


# ==========================================================
# GET EVENT BY ID
#
# NOTE:
# This works if your Events sheet contains one of these
# columns:
#
# Place_ID
# Event_ID
# ID
#
# ==========================================================

@router.get("/{event_id}")
def get_event_by_id(event_id: str):

    try:

        # Check whether data exists
        if events_df is None:
            raise HTTPException(
                status_code=500,
                detail="Events data is not loaded."
            )

        # Check whether DataFrame is empty
        if events_df.empty:
            raise HTTPException(
                status_code=404,
                detail="No Events & Workshops data found."
            )

        df = events_df.fillna("").copy()

        # Possible ID columns
        possible_id_columns = [
            "Place_ID",
            "Event_ID",
            "ID"
        ]

        id_column = None

        # Find the ID column that actually exists
        for column in possible_id_columns:

            if column in df.columns:
                id_column = column
                break

        # If no ID column exists
        if id_column is None:

            raise HTTPException(
                status_code=500,
                detail=(
                    "No ID column found in Events & Workshops data. "
                    f"Available columns: {list(df.columns)}"
                )
            )

        # Search for matching ID
        result = df[
            df[id_column].astype(str).str.lower()
            == str(event_id).lower()
        ]

        # Event not found
        if result.empty:

            raise HTTPException(
                status_code=404,
                detail=f"Event with ID '{event_id}' not found."
            )

        # Return first matching event
        return result.iloc[0].to_dict()

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to load event: {str(e)}"
        )