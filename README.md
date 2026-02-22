# Assignment 1: Web Page Similarity

## Objective
The aim of this assignment is to check how similar two web pages are by looking at their actual content instead of just their URLs. To do this, the project uses **SimHash**.

The program loads two web pages, reads the visible text from them, counts how often words appear, creates a compact 64-bit fingerprint for each page, and then compares these fingerprints to estimate how similar the pages are.

## Information Retrieval Concepts Used

| Concept                 | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| Web Crawling            | Loading live web pages using an automated browser                |
| HTML Parsing            | Extracting title, text content, and hyperlinks from HTML         |
| Tokenization            | Breaking text into individual alphanumeric words                 |
| Term Frequency (TF)     | Counting how many times each word appears                        |
| Hashing                 | Converting words into numeric values using polynomial hashing    |
| Document Fingerprinting | Representing a document using SimHash                            |
| Similarity Measure      | Measuring similarity using Hamming Distance (via XOR)           |

## Technologies Used
- Python  
- Selenium  
- webdriver-manager  
- BeautifulSoup (bs4)  
- Standard Python libraries such as `re`, `time`, and `urllib`  

## Working Methodology

### Fetch Web Pages
The program uses Selenium with headless Chrome to open each webpage. This approach ensures that pages relying on JavaScript are fully loaded before any data is extracted. ChromeDriver is managed automatically so browser updates do not break the program.

### HTML Parsing
Once the page is loaded, BeautifulSoup is used to parse the HTML.  
The program:
- Extracts the page title  
- Removes unnecessary `<script>` and `<style>` tags  
- Collects all visible text  
- Gathers all outgoing hyperlinks present on the page  

### Tokenization
The extracted text is converted to lowercase and split into words containing only letters and numbers. This keeps the comparison simple and consistent.

### Word Frequency Calculation
Each word is counted to determine how important it is within the page. Words that appear more frequently have a greater impact on the final fingerprint.

### SimHash Generation
Each word is hashed using a polynomial rolling hash. These hashes are combined into a weighted 64-bit vector based on word frequencies, which is then converted into a single 64-bit SimHash value representing the page.

### Similarity Computation
The two SimHash values are compared using the XOR operation.  
The number of matching bits is calculated to measure similarity. More matching bits indicate more similar content.

## Output
All results are written to `output.txt` to avoid terminal overflow. The file contains:
- Page titles  
- Extracted body text  
- Outgoing links  
- Word frequency lists  
- SimHash values (integer and binary form)  
- The number of common bits between the two pages  
