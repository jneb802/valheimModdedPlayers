from fastapi import FastAPI, HTTPException
import requests
import json
from datetime import datetime

app = FastAPI()

# Get total downloads for a Thunderstore package
@app.get("/get-mod-downloads")
async def get_valheim_bepinex_downloads(namespace: str, name: str):
    url = f"https://thunderstore.io/api/v1/package-metrics/{namespace}/{name}/"
    response = requests.get(url)
    return {"data": response.json()}

# Write Thunderstore total downloads to a json file
@app.post("/post-mod-downloads")
async def post_mod_downloads(namespace: str, name: str, game: str, downloads: int):

    with open("downloads.json", "r", encoding="utf-8") as file:
        mod_downloads = json.load(file)

    mod_found = False
    message = ""

    for mod in mod_downloads:
        if mod.get("game") == game and mod.get("namespace") == namespace and mod.get("name") == name:
            mod_found = True
            mod.setdefault("download_history", []).append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "downloads": downloads
            })
            message = f"Found mod {name}: wrote {downloads} downloads to file"
            break

    if not mod_found:
        new_mod = {
            "game": game,
            "namespace": namespace,
            "name": name,
            "download_history": [{
                "date": datetime.now().strftime("%Y-%m-%d"),
                "downloads": downloads
            }]
        }
        mod_downloads.append(new_mod)
        message = f"Mod not found; created new entry {name} with downloads count {downloads}"


    with open("downloads.json", "w", encoding="utf-8") as file:
        json.dump(mod_downloads, file, ensure_ascii=False, indent=4)

    return {"message": message}