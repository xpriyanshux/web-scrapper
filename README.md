# Course Scraper for Indian Colleges

## Overview

This Python script scrapes course information from the course pages of Indian colleges. For the purpose of this assignment, the script is demonstrated using Kalindi College of Delhi University as an example. It retrieves a list of courses offered by the college, including course names and syllabus links.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`

## Installation

1. **Clone this repository** or download the script file.

2. **Install the required libraries** using pip:

   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

## Usage

1. **Download the script** (`course_scraper.py`) and ensure it is in your working directory.

2. **Modify the script**:
   - Update the URLs if needed or adjust the script to accept a college name (if required).

3. **Run the script**:

   ```bash
   python course_scraper.py
   ```

   By default, the script uses URLs for Kalindi College's undergraduate and postgraduate courses. You can change these URLs in the script if you want to scrape data from other colleges.

4. **Check the output**:
   - The script will print the scraped course data in a structured format to the terminal.
   - The data will be saved to an Excel file at the specified path.

## Example

For Kalindi College, the script scrapes data from:
- [Undergraduate Courses URL](https://www.kalindicollege.in/undergraduate/)
- [Postgraduate Courses URL](https://www.kalindicollege.in/postgraduate/)

## Output

- **Terminal Output**: Structured display of course data.
- **Excel File**: Saved as `Kalindi_College_Courses.xlsx` in the specified path.

## Limitations and Constraints

1. **Website Structure**: 
   - The script is tailored to scrape data from a specific website structure. If the website’s layout changes or if data is presented differently (e.g., in JavaScript-rendered content or via pagination), the script may not work correctly without modifications.

2. **Dynamic Content**:
   - The script does not handle dynamically loaded content (e.g., content loaded via JavaScript). Websites that load data asynchronously may require additional tools like Selenium or adjustments to handle such cases.

3. **Error Handling**:
   - While basic error handling is implemented, the script may not handle all edge cases. For example, if the table structure or HTML tags are different from what is expected, the script might not extract the data correctly.

4. **College Name Handling**:
   - The script currently works with predefined URLs. It does not support searching for a college’s URL based on its name, which means users must manually provide the correct URL.

5. **Scalability**:
   - The script does not include advanced features for scraping multiple pages or handling large datasets efficiently. Improvements may be needed for more extensive data collection tasks.

6. **Server Load**:
   - Ensure the script is run responsibly to avoid excessive requests to the server. Implementing delays between requests or using rate limiting can help mitigate any potential load on the server.

## LIMITATIONS

- Add functionality to handle college names and search for corresponding URLs.
- Enhance the script to handle dynamic content loading such as drop down menu options which might need use of selenium and respective web drivers.
- Include rate limiting and request throttling to reduce server load.
