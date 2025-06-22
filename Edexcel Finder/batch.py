from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import polars as pl
import os
import re

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"\033[43m\033[30m Directory created: {path} \033[0m")
    else:
        print(f"\033[43m\033[30m Directory already exists: {path} \033[0m")
driver = webdriver.Chrome()

driver.get(f"https://qualifications.pearson.com/en/support/support-topics/results-certification/understanding-marks-and-grades/converting-marks-points-and-grades.html?QualFamily=International%20A%20Level&ExamSeries=June%202019&Qualification=Mathematics&Unit=WME01%2F01%20-%20Mechanics%20M1#gcstep4")
wait = WebDriverWait(driver, 10)
accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
accept_btn.click()

file = open("years.txt", "r")
years = file.read()
years = years.split("\n")

todo = []
for file in os.listdir("D:\GB\Subjects"):
    subject = re.sub(".txt","", file)
    data = open(f"D:/GB/Subjects/{file}", "r")
    data = data.read().split("\n")
    todo.append([subject, data])
for i in range(0, len(todo)):
    for j in range (1, len(todo[i])):
        for k in range(0, len(todo[i][j])):
            for year in years:
                driver.get(f"https://qualifications.pearson.com/en/support/support-topics/results-certification/understanding-marks-and-grades/converting-marks-points-and-grades.html?QualFamily=International%20A%20Level&ExamSeries={year}&Qualification={todo[i][0]}&Unit={todo[i][j][k]}")


                wait = WebDriverWait(driver, 10)
                all_scores_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'All scores')]")))
                all_scores_link.click()


                wait = WebDriverWait(driver, 10)
                grade_tab = wait.until(EC.visibility_of_element_located((By.ID, "allScores")))


                children = grade_tab.find_elements(By.XPATH, "./*")

                scores =[]
                for child in children:
                    data = child.text.split("\n")
                    scores.append(data)

                df = pl.DataFrame(scores[1:], schema=scores[0])
                df = df.with_columns([
                    pl.col("RAW").cast(pl.Int64),
                    pl.col("UMS").cast(pl.Int64)
                ])
                unit = re.sub(":", "", todo[i][j][k])
                ensure_directory(f"D:/GB/{todo[i][0]}/{unit}")
                df.write_json(f"D:/GB/{todo[i][0]}/{unit}/{year}.json")
                print(f"\033[1;32m{year} {todo[i][0]} {todo[i][j][k]} completed\033[0m")
