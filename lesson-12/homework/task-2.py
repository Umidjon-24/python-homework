import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


url = "https://realpython.github.io/fake-jobs"
driver = webdriver.Chrome()
driver.get(url)

conn = sqlite3.connect(r"D:\Python\python-homework\lesson-12\homework\jobs.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Jobs (
        title TEXT,
        company TEXT,
        location TEXT, 
        description TEXT,
        apply_link TEXT
    )
""")

# Extract job postings
jobs = driver.find_elements(By.CLASS_NAME, "card-content")

job_data = []
for job in jobs:
    title = job.find_element(By.TAG_NAME, "h2").text
    company = job.find_element(By.CLASS_NAME, "subtitle").text
    location = job.find_element(By.CLASS_NAME, "location").text
    apply_link = job.find_element(By.LINK_TEXT, "Apply").get_attribute("href")
    job_data.append((title, company, location, apply_link))

# Visit each job page sequentially
for title, company, location, apply_link in job_data:
    driver.get(apply_link)  

    try:
        description =   driver.find_element(By.XPATH, "//div[@class='content']/p").text

    except Exception as e:
        print("Error extracting job details:", e)
        description = "N/A"

     # Check if job already exists
    cursor.execute("""
        SELECT description, apply_link FROM Jobs 
        WHERE title = ? AND company = ? AND location = ?
    """, (title, company, location))

    existing_job = cursor.fetchone()

    if existing_job:
        old_description, old_apply_link = existing_job
        if description != old_description or apply_link != old_apply_link:
            # Update job listing if description or apply link has changed
            cursor.execute("""
                UPDATE Jobs 
                SET description = ?, apply_link = ?
                WHERE title = ? AND company = ? AND location = ?
            """, (description, apply_link, title, company, location))
    else:
        # Insert new job if it doesn't exist
        cursor.execute("""
            INSERT INTO Jobs (title, company, location, description, apply_link)
            VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, apply_link))


conn.commit()
conn.close()

driver.quit()

def export_jobs(filter_by=None, value=None, output_file="filtered_jobs.csv"):
    # Connect to database
    conn = sqlite3.connect(r"D:\Python\python-homework\lesson-12\homework\jobs.db")
    cursor = conn.cursor()

    if filter_by == "company":
        cursor.execute("SELECT * FROM Jobs WHERE company = ?", (value,))
    elif filter_by == "location":
        cursor.execute("SELECT * FROM Jobs WHERE location = ?", (value,))
    else:
        cursor.execute("SELECT * FROM Jobs")

    jobs = cursor.fetchall()
    conn.close()

    # Write jobs to CSV file
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)

    print(f"Data exported to {output_file}")

#export_jobs(filter_by="location", value="Stewartbury, AA")


