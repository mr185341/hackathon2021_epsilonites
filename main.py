from fastapi import FastAPI
from starlette.responses import RedirectResponse
import utils


db = utils.get_dbconn()
app = FastAPI()
site_id = 2233


@app.get("/", tags=["ROOT"])
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/terminals")
def get_terminals() -> list:
    collection = db["sitedetails"]
    site_collection = collection.find_one({"site_id": site_id})
    return list(site_collection["terminals"])


@app.get("/pumps/")
def get_pumps() -> list:
    collection = db["sitedetails"]
    site_collection = collection.find_one({"site_id": site_id})
    return list(site_collection["pumps"])


@app.get("/cards")
def get_cards() -> dict:
    collection = db["sitedetails"]
    site_collection = collection.find_one({"site_id": site_id})
    return site_collection["cards"]


@app.get("/terminal/{item_id}")
def get_terminal_info(item_id: int) -> dict:
    collection = db["sitedetails"]
    item = collection.find_one(
        {"site_id": site_id, "terminals.id": item_id}, {"terminals.$": 1}
    )
    return dict(item)["terminals"][0]


@app.get("/pump/{item_id}")
def get_pump_info(item_id: int) -> dict:
    collection = db["sitedetails"]
    item = collection.find_one(
        {"site_id": site_id, "pumps.id": item_id}, {"pumps.$": 1}
    )
    return dict(item)["pumps"][0]
