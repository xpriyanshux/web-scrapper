import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_courses(url):
    """
    Scrape course information from the specified URL.

    This function sends a request to the provided URL and parses the HTML response to extract course details,
    including course names and syllabus links. It handles potential errors during the request and processes
    the HTML to collect relevant data from a table format.

    Args:
        url (str): The URL of the page containing course information.

    Returns:
        list: A list of dictionaries, each containing the 'Course Name' and 'Syllabus Link'.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the HTTP request was successful
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from {url}. Error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    courses = []
    
    # Locate the table element in the HTML where course data is expected to be found
    course_table = soup.find('table')
    if course_table:
        rows = course_table.find_all('tr')  # Extract all rows from the table
        for row in rows:
            columns = row.find_all('td')  # Extract all columns from the current row
            # Print columns for debugging purposes
            print(f"Columns: {[col.text.strip() for col in columns]}")
            if len(columns) > 1:  # Ensure there are enough columns in the row to process
                course_name = columns[1].text.strip()  # Extract the course name from the second column
                
                # Check for the presence of an <a> tag for the syllabus link
                syllabus_link_tag = columns[2].find('a') if len(columns) > 2 else None
                syllabus_link = syllabus_link_tag.get('href', '') if syllabus_link_tag else ''
                
                courses.append({
                    "Course Name": course_name,
                    "Syllabus Link": syllabus_link
                })

    return courses

def save_to_excel(data, file_name):
    """
    Save the provided data to an Excel file with multiple sheets.

    This function takes a dictionary of data where each key-value pair represents a sheet name and its corresponding data.
    It uses the pandas library to create an Excel file and write each dataset to a separate sheet.

    Args:
        data (dict): A dictionary where keys are sheet names and values are lists of course data.
        file_name (str): The path and name of the Excel file to be created.
    """
    # Create an Excel writer object using pandas with the OpenPyXL engine
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        # Iterate over each entry in the data dictionary to write to different sheets
        for sheet_name, courses in data.items():
            df = pd.DataFrame(courses)  # Convert the list of course data to a DataFrame
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Data for '{sheet_name}' has been successfully saved to the sheet.")

def print_data_structured(data):
    """
    Print the data in a structured dictionary format.

    This function formats and prints the data to the terminal, providing a clear and organized view of the scraped course
    information. It displays each category and its corresponding list of course entries.

    Args:
        data (dict): A dictionary where keys are categories and values are lists of course data.
    """
    print("\nScraped Course Data:\n")
    for category, courses in data.items():
        print(f"--- {category} ---")
        if courses:
            for index, course in enumerate(courses, start=1):
                print(f"Course {index}:")
                for key, value in course.items():
                    print(f"  {key}: {value}")
                print()  # Print a blank line for readability
        else:
            print("  No courses found.")
        print("-" * 40)  # Print a separator for clarity

# Define URLs for undergraduate and postgraduate courses
undergraduate_url = "https://www.kalindicollege.in/undergraduate/"
postgraduate_url = "https://www.kalindicollege.in/postgraduate/"

# Scrape course information from both URLs
undergraduate_courses = scrape_courses(undergraduate_url)
postgraduate_courses = scrape_courses(postgraduate_url)

# Prepare a dictionary with data for each category
data = {
    "Undergraduate Courses": undergraduate_courses,
    "Postgraduate Courses": postgraduate_courses
}

# Print the scraped data in a structured format
print_data_structured(data)

# Specify the file path where the Excel file will be saved
output_path = "E:\\perl\\codes\\Kalindi_College_Courses.xlsx"

# Save the scraped data to the Excel file
save_to_excel(data, output_path)
