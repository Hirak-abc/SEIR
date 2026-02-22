# Assignment 1: Web Page Similarity 

## Objective
The objective of this project is to compare two web pages and determine their similarity using SimHash, a technique widely used for near-duplicate document detection.

The project renders live web pages, extracts textual content, computes word frequencies, generates 64-bit SimHash fingerprints, and compares them using Hamming distance (bit-level similarity).

## Information Retrieval Concepts Used

| Concept                   | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| Web Crawling              | Fetching live web pages using a browser-based crawler            |
| HTML Parsing              | Extracting title, body text, and hyperlinks                      |
| Tokenization              | Manual alphanumeric word extraction                              |
| Term Frequency (TF)       | Counting occurrences of words                                    |
| Hashing                   | Polynomial rolling hash                                          |
| Document Fingerprinting   | SimHash                                                         |
| Similarity Measure        | Hamming Distance (via XOR)                                       |

## Technologies Used
- Python  
- Selenium  
- webdriver-manager  
- BeautifulSoup (bs4)  
- Standard Python libraries (re, time, urllib)  

## Working Methodology

### Fetch Web Pages
- Uses Selenium with headless Chrome  
- Automatically manages ChromeDriver version  
- Fully renders JavaScript-based pages  

### HTML Parsing
- Parses rendered HTML using BeautifulSoup  
- Extracts page title  
- Removes `<script>` and `<style>` tags  
- Extracts visible text from the document  
- Collects all outgoing hyperlinks  

### Tokenization
- Converts text to lowercase  
- Extracts alphanumeric tokens using regular expressions  

### Word Frequency Calculation
- Counts frequency of each token in the document  

### SimHash Generation
- Applies polynomial hashing to each word  
- Builds a weighted 64-bit vector  
- Generates a 64-bit SimHash fingerprint  

### Similarity Computation
- Uses XOR between two SimHashes  
- Counts differing bits  
- Computes number of common bits (64 − differing bits)  

## Output
- All extracted data and results are written to `output.txt`  
- Includes titles, body text, outgoing links, word frequencies, SimHashes, and no. of common bits  
