import requests

def get_hp_model(serial, model=""):
    headers = {
        #[[ REDACTED ]]
    }
    response = requests.get(
        f'https://pro-psurf-app.glb.inc.hp.com/partsurferapi/Search/GenericSearch/{serial}/country/US/usertype/EXT',
        headers=headers,
    )
    if response:
        new_model = ""
        body = response.json()["Body"]
        if "SNRProductLists" in body:
            models = [p["product_Id"] for p in body["SNRProductLists"]]
            if model not in models:
                new_model = models                  
        else:
            new_model = body["SerialNumberBOM"]["wwsnrsinput"]["product_no"]
        if new_model != model:
            model = new_model
        return model
    else:
        return "not found"    