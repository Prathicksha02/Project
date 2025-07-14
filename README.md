# Web Application Vulnerability Scanner

A lightweight Python-based tool that scans websites for common web application vulnerabilities such as **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)**. This project was built as part of a cybersecurity internship to demonstrate the basics of automated vulnerability detection.

---

## Project Objective

To develop a command-line vulnerability scanner that:
- Crawls a target web page
- Finds all HTML forms
- Injects test payloads
- Detects reflected input or SQL error messages in the response

---

## Features

-  Extracts forms using `BeautifulSoup`
-  Injects XSS and SQLi test payloads into input fields
-  Analyzes response content for reflected payloads and SQL error messages
-  Logs detection results in the terminal (optionally to a file)
-  Optional: Flask-based web interface for easier scanning

---

## Tools & Technologies

- **Language**: Python 3
- **Libraries**: `requests`, `beautifulsoup4`, `flask` (optional)
- **Testing Site**: [http://testphp.vulnweb.com](http://testphp.vulnweb.com) (legal test site)

---

## Install Dependencies

**pip install requests beautifulsoup4 flask**

3. Run the Scanner
python scanner.py

4. Enter a Target URL
Example:
http://testphp.vulnweb.com

The scanner will:

Search for input forms on the page

Inject test payloads (XSS & SQLi)

Analyze the response

Display results in the terminal

## Example Output

Scanning form: http://testphp.vulnweb.com/search.php?test=query
Payload sent: {'searchFor': "<script>alert('XSS')</script>' OR '1'='1"}
❗ XSS Vulnerability Detected!

## Conclusion
This project successfully demonstrates how basic web application vulnerabilities like Cross-Site Scripting (XSS) and SQL Injection (SQLi) can be detected using automated tools. By building this scanner from scratch using Python, I gained hands-on experience in:

Crawling web forms

Payload injection techniques

Analyzing server responses for vulnerability detection

It also deepened my understanding of the OWASP Top 10 and the importance of secure input handling in web applications.
This tool serves as a foundational step towards learning more advanced security testing techniques and tools like Burp Suite, OWASP ZAP, and sqlmap.
