# Top 100 Movies Scraper

A Python-based web scraping tool that extracts the Top 100 Movies of All Time from an archived Empire Online list and exports the results into a structured text file.

---

## Overview

This project scrapes movie titles from a Wayback Machine snapshot of an Empire Online article and processes them into a clean, ordered list.

---

## Features

- Extracts movie data from an archived web page
- Parses HTML using BeautifulSoup
- Reorders results into correct ranking (1–100)
- Outputs results to a structured text file
- Handles encoding issues during data extraction

---

## How It Works

### Data Source
The script retrieves HTML content from a saved snapshot of the Empire Online “Top 100 Movies” list via the Internet Archive.

### Parsing Logic
- Locates all `<h3 class="title">` elements
- Extracts and cleans movie titles

### Data Processing
- Stores titles in a list
- Reverses the list to match original ranking order

### Output
- Writes formatted results to `Top 100 Movies.txt`

---

## Project Structure

main.py  

---

## Usage

Run the script:

python main.py  

After execution, the output file will be generated:

Top 100 Movies.txt  

---

## Example Output

1) The Godfather
2) The Empire Strikes BAck
3) The Dark Knight  
...

---

## Technologies Used

- requests
- BeautifulSoup4

---

## Notes

- The dataset is static due to archived source material
- Minor encoding issues are handled during parsing
- No external API keys are required
