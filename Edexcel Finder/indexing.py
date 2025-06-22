from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, NUMERIC
import os
import json
import re
from colorama import Fore
import json

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{Fore.BLUE} {path} created")
    else:
        pass

schema = Schema(
    year = TEXT(stored=True),
    page = NUMERIC(stored=True, numtype=int), 
    content = TEXT, 
    qp_link = TEXT(stored=True),
    ms_link = TEXT(stored=True))

for unit in os.listdir("static/Data/Mathematics (2018)"):
    ensure_directory(f"static/Index/Mathematics (2018)/{unit}")
    ix = create_in(f"static/Index/Mathematics (2018)/{unit}", schema)
    writer = ix.writer()
    for file in os.listdir(f"static/Data/Mathematics (2018)/{unit}"):
        name = re.sub(".json", "", file)
        info = name.split("-")
        if info[0].find("Unused") != -1:
            Year = f"Unused {info[2][1:len(info[2])]}"
            print(f"{Fore.RED} {Year}")
        elif info[0] == "Sample Assessment":
            Year = "Sample Assessment"
        else:
            Year = info[2][1:len(info[2])]
        data = open(f"static/Data/Mathematics (2018)/{unit}/{file}", "r", encoding="utf-8")
        data = json.load(data)
        for row in data:
            writer.add_document(
                year = Year,
                page = row["Page"], 
                content = row["Content"], 
                qp_link = row["QP_Link"],
                ms_link = row["MS_Link"])
            print(f"{Fore.GREEN} {Year}'s {unit}'s Page: {row['Page']} has been completed")
    writer.commit()