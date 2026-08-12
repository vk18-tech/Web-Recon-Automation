
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-red)

# Web Recon Automation Framework

A modular Python-based reconnaissance framework that automates the collection of publicly available information about an authorized web target and generates a structured HTML reconnaissance report.

The project demonstrates practical cybersecurity automation, modular Python development, reconnaissance techniques, error handling, logging, and security reporting.

---

## 🎯 Project Objective

During a penetration testing or security assessment, reconnaissance can involve repeatedly using multiple tools to collect information about a target.

This project automates that initial reconnaissance process through a single command-line interface.

The framework accepts a domain or URL and collects:

- DNS records
- IPv4 and IPv6 addresses
- IP geolocation
- WHOIS information
- HTTP response information
- HTTP security headers
- SSL/TLS certificate information
- `robots.txt`
- `sitemap.xml`
- Basic security observations

The collected information is then compiled into a professional HTML report.

---

## ✨ Project Highlights

- 🔍 Automated DNS reconnaissance
- 🌐 IPv4 and IPv6 address discovery
- 📍 IP geolocation with ISP, organization, and ASN details
- 🏷️ WHOIS domain information gathering
- 🌐 HTTP response and header analysis
- 🔐 SSL/TLS certificate and protocol analysis
- 🤖 `robots.txt` and `sitemap.xml` discovery
- 🛡️ Security header analysis
- 📊 Automated HTML reconnaissance report generation
- 📝 Structured logging for reconnaissance activities
- ⚙️ Modular Python-based architecture
- ❌ Graceful handling of invalid or unreachable targets

---

## 🏗️ Architecture

The framework follows a modular architecture where each reconnaissance task is handled by a separate module.

```text
                    Target Domain
                         │
                         ▼
                 ┌───────────────┐
                 │ Target        │
                 │ Validator     │
                 └───────┬───────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Reconnaissance     │
              │      Modules         │
              └──────────┬───────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
     DNS/IP            WHOIS          HTTP/SSL
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                         ▼
                Web Files Analysis
                         │
                         ▼
              Security Header Analysis
                         │
                         ▼
                Data Aggregation
                         │
                         ▼
               HTML Report Generator
                         │
                         ▼
                 Reconnaissance Report
```

### Module Structure

| Module | Responsibility |
|---|---|
| `core/validator.py` | Validates and normalizes the target |
| `modules/dns_recon.py` | Collects DNS records |
| `modules/ip_recon.py` | Discovers IPv4/IPv6 addresses |
| `modules/geolocation_recon.py` | Retrieves IP geolocation information |
| `modules/whois_recon.py` | Collects WHOIS information |
| `modules/http_recon.py` | Analyzes HTTP responses and headers |
| `modules/ssl_recon.py` | Collects SSL/TLS certificate information |
| `modules/web_files_recon.py` | Checks `robots.txt` and `sitemap.xml` |
| `modules/security_headers.py` | Checks important security headers |
| `modules/report_generator.py` | Generates the final HTML report |

---

## 🔎 Features

### DNS Reconnaissance

Collects:

- A records
- AAAA records
- MX records
- NS records
- TXT records
- CNAME records

### IP Reconnaissance

Identifies:

- IPv4 addresses
- IPv6 addresses

### IP Geolocation

Collects basic publicly available information associated with discovered IP addresses:

- Country
- Region
- City
- Postal code
- Latitude
- Longitude
- ISP
- Organization
- ASN

### WHOIS Reconnaissance

Collects available domain registration information such as:

- Registrar
- Creation date
- Expiration date
- Updated date
- Name servers
- Domain status

### HTTP Reconnaissance

Collects:

- HTTP status code
- Response time
- Server information
- Content type
- HTTP response headers

### SSL/TLS Reconnaissance

Collects:

- TLS version
- Certificate subject
- Certificate issuer
- Certificate validity period
- Days remaining

### Web Files Reconnaissance

Checks for:

- `robots.txt`
- `sitemap.xml`

The framework records whether these resources are available and captures their content when accessible.

### Security Header Analysis

Checks for commonly used security headers:

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

It also checks whether the HTTP Server banner is exposed.

### Logging

The framework records important events and errors in:

```text
logs/recon.log
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vk18-tech/Web-Recon-Automation.git
cd Web-Recon-Automation
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the framework by providing an authorized domain:

```powershell
python main.py example.com
```

Example output:

```text
# Web Recon Automation Framework

Target: example.com

[+] Starting DNS reconnaissance...
[+] Starting IP reconnaissance...
[+] Starting IP geolocation...
[+] Starting WHOIS reconnaissance...
[+] Starting HTTP reconnaissance...
[+] Starting SSL/TLS reconnaissance...
[+] Starting web files reconnaissance...
[+] Starting security header analysis...
[+] Generating HTML reconnaissance report...

[+] Report generated successfully!
```

The generated report is saved in:

```text
reports/recon_report_example.com.html
```

---

## 📄 Sample Report

A sample reconnaissance report generated by the framework is included in the repository.

**Target:** `example.com`

The report contains:

- DNS records
- IPv4 and IPv6 addresses
- IP geolocation
- WHOIS information
- HTTP response details
- HTTP security headers
- SSL/TLS certificate information
- `robots.txt` and `sitemap.xml` results
- Security observations

👉 [View the Sample HTML Report](reports/recon_report_example.com.html)

---

## 🛠️ Technology Stack

- **Language:** Python 3
- **DNS & Network Recon:** `dnspython`
- **WHOIS:** WHOIS lookup functionality
- **HTTP Analysis:** `requests`
- **SSL/TLS:** Python `ssl` module
- **IP Geolocation:** IP geolocation API
- **Report Generation:** HTML / Python
- **Logging:** Python `logging`
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
Web-Recon-Automation/
│
├── core/
│   └── validator.py
│
├── modules/
│   ├── dns_recon.py
│   ├── ip_recon.py
│   ├── geolocation_recon.py
│   ├── whois_recon.py
│   ├── http_recon.py
│   ├── ssl_recon.py
│   ├── web_files_recon.py
│   ├── security_headers.py
│   └── report_generator.py
│
├── reports/
│   └── recon_report_example.com.html
│
├── screenshots/
│   ├── 01_framework_execution.png
│   ├── 02_html_report.png
│   └── 03_security_headers.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📸 Screenshots

### Framework Execution

![Framework Execution](screenshots/01_framework_execution.png)

### Generated HTML Report

![HTML Report](screenshots/02_html_report.png)

### Security Header Analysis

![Security Header Analysis](screenshots/03_security_headers.png)

---

## ⚠️ Limitations

- Results depend on DNS, WHOIS, geolocation, and target-server availability.
- Some WHOIS servers may restrict automated queries.
- IP geolocation provides approximate information and should not be treated as an exact physical location.
- Security header findings indicate missing or exposed headers; they do not by themselves confirm a vulnerability.
- `robots.txt` and `sitemap.xml` may not exist on every website.
- Some HTTP or SSL/TLS information may be unavailable when a target is unreachable.
- The framework performs passive/basic reconnaissance and does not perform exploitation or intrusive vulnerability scanning.

---

## 🔐 Responsible Use

This framework is intended for authorized security testing, learning, and reconnaissance.

Only run the tool against domains and systems that you own or have explicit permission to assess.

The project does not perform exploitation or unauthorized access.

---

## 📚 Learning Outcomes

Through this project, I learned how to:

- Design a modular Python security tool
- Automate common reconnaissance tasks
- Work with DNS and domain information
- Process HTTP and SSL/TLS information
- Perform basic security-header analysis
- Handle network failures gracefully
- Implement structured application logging
- Generate automated security reports
- Organize a cybersecurity project for GitHub
- Document technical limitations and responsible use

---

## 👩‍💻 Author

**Shrishti Pandey**

B.Tech Computer Science Student | Cybersecurity Enthusiast | SOC Analyst Aspirant

---

## ⭐ Project Status

**Status:** Completed

The framework is functional and can be extended with additional reconnaissance modules and security analysis capabilities.