import fitz  
import re
import polars as pl
from colorama import Fore
import os
import json
import requests

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{Fore.BLUE} {path} created")
    else:
        pass
subjects = ["Mathematics (2018)", 
            "Old Mathematics",
            "Physics (2018)",
            "Old Physics",
            "Chemistry (2018)",
            "Old Chemistry",
            "Biology (2018)",
            "Old Biology"]
for subject in subjects:
    for unit in os.listdir(f"static/Papers/{subject}"):
        for file in os.listdir(f"static/Papers/{subject}/{unit}"):
            data = []
            doc = fitz.open(f"static/Papers/{subject}/{unit}/{file}")
            if file.find("Sample") != -1:
                if file.find("MS") != -1:
                    continue
                else:
                    name = "Sample Assessment"
                    QP_link = f"static/Papers/{subject}/{unit}/Sample Assessment.pdf"
                    MS_link = f"static/Papers/{subject}/{unit}/Sample Assessment MS.pdf"
                    for page_num in range(1, len(doc)):
                        page = doc[page_num]
                        content = page.get_text().lower()
                        content = re.sub("\.{10,}", "", content)
                        content = re.sub("\_{10,}", "", content)
                        content = re.sub("\n", "", content)            
                        data.append([page_num, content, QP_link, MS_link])
            else:
                fetch_file_name = re.sub(".pdf", ".json", file)
                fetch_file_name = fetch_file_name.split("-")
                fetch_file = re.sub(" ", "-", fetch_file_name[2][1:])
                fetch_data = open(f"static/Fetch/{subject}/{fetch_file}", "r")
                fetched_data = json.load(fetch_data)
                for row in fetched_data:
                    info = row["Name"].split("-")
                    # Unit = info[1].find("Unit")
                    # Unit = info[1][Unit: Unit + 6]
                    finder = re.sub(".pdf", "", file)
                    array = finder.split("-")
                    del array[0]
                    array = "-".join(array)
                    check = "-".join(info[1:])
                    if info[0].lower().find("question") != -1 and check.lower().find(array.lower()) != -1:
                        response = requests.get(row["Link"])
                        if response.url == 'https://qualifications.pearson.com/en/campaigns/404.html':
                            link = row["Link"]
                            link = link.split("/")
                            link[-1] = re.sub("_", "-", link[-1].lower())
                            QP_link = "/".join(link)
                        else:
                            QP_link = row["Link"]
                    if info[0].lower().find("mark") != -1 and check.lower().find(array.lower()) != -1:
                        if finder.find("Unused") != -1 and row["Link"].lower().find("unused") != -1:
                            MS_link = row["Link"]
                        elif finder.find("Unused") == -1 and row["Link"].lower().find("unused") == -1:
                            MS_link = row["Link"]
                        response = requests.get(MS_link)
                        if response.url == 'https://qualifications.pearson.com/en/campaigns/404.html':
                            link = MS_link
                            link = link.split("/")
                            link[-1] = re.sub("_", "-", link[-1].lower())
                            MS_link = "/".join(link)
                for page_num in range(1, len(doc)):
                    page = doc[page_num]
                    content = page.get_text().lower()
                    content = re.sub("\.{10,}", "", content)
                    content = re.sub("\_{10,}", "", content)
                    content = re.sub("\-{10,}", "", content)
                    content = re.sub("\n", "", content)
                    data.append([page_num, content, QP_link, MS_link])
            df = pl.DataFrame(data, schema=["Page", "Content", "QP_Link", "MS_Link"], orient="row")
            df = df.with_columns([pl.col("Page").cast(pl.Int64)])
            ensure_directory(f"static/Data/{subject}/{unit}")
            file_name = re.sub(".pdf", "", file)
            df.write_json(f"static/Data/{subject}/{unit}/{file_name}.json")
            print(f"{Fore.MAGENTA} {df}")
            print(f"{Fore.YELLOW} Information has been extracted from {file_name}, {subject} {unit}")
    doc.close()
