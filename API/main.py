from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Literal
app = FastAPI()

@app.get("/Papers/{qualification}")
def Papers(qualification:Literal["IGCSE", "IAL"], year:int, session: Literal["January", "June", "October", "November"], subject: str, subject_pin: str):
    series = f"{session}-{year}"
    driver = webdriver.Chrome()
    if (qualification == "IGCSE"):
        url = f"https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html?Qualification-Family=International-GCSE&Qualification-Subject={subject}&Status=Pearson-UK:Status%2FLive&Specification-Code=Pearson-UK:Specification-Code%2F{subject_pin}&Exam-Series={series}"
    elif (qualification == "IAL"):
        url = f"https://qualifications.pearson.com/en/support/support-topics/exams/past-papers.html?Qualification-Family=International-Advanced-Level&Qualification-Subject={subject}&Status=Pearson-UK:Status%2FLive&Specification-Code=Pearson-UK:Specification-Code%2F{subject_pin}&Exam-Series={series}"
    else:
        return {"response": "Not a supported qualification level"}    
    driver.get(url)
    
    wait = WebDriverWait(driver, 4)
    accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_btn.click()
    time.sleep(2)
    everything = driver.find_elements(By.XPATH, '//*[@id="resultsTable"]/*')
    data = []
    for one in everything:
        name = one.find_element(By.TAG_NAME, "span").text
        link = one.find_element(By.TAG_NAME, "a").get_attribute("href")
        detail = f"{name}: {link}"
        if len(detail) > 20:
            data.append({"Name": name, "Link": link})
        
    driver.quit()

    return {"response": data}    
