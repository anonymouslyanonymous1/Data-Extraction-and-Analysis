from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import polars as pl
import os
import re

driver = webdriver.Chrome()

driver.get(f"https://qualifications.pearson.com/en/support/support-topics/results-certification/understanding-marks-and-grades/converting-marks-points-and-grades.html?QualFamily=International%20A%20Level&ExamSeries=January%202025&Qualification=Physics%20(2018)&Unit=WPH12%2F01%20-%20Waves%20and%20Electricity#gcstep4")
wait = WebDriverWait(driver, 10)
accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
accept_btn.click()

driver.get(f"https://qualifications.pearson.com/en/support/support-topics/results-certification/understanding-marks-and-grades/converting-marks-points-and-grades.html?QualFamily=International%20A%20Level&ExamSeries=January%202025&Qualification=Physics%20(2018)&Unit=WPH12%2F01%20-%20Waves%20and%20Electricity#gcstep4")


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
print(df)
df.write_json(f"si.json")
