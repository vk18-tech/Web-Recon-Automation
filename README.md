# Web Recon Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Tests](https://img.shields.io/badge/Tests-11%20passed-brightgreen)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-red)

A modular Python-based reconnaissance framework that automates the collection of publicly available information about an authorized web target and generates a structured HTML reconnaissance report.

The project demonstrates practical cybersecurity automation, modular Python development, reconnaissance techniques, error handling, logging, testing, and security reporting.

---

## Project Objective

During a penetration test or security assessment, reconnaissance often requires repeatedly using multiple tools to collect information about a target.

This project automates the initial reconnaissance process through a single command-line interface.

The framework accepts a domain or URL and collects:

* DNS records
* IPv4 and IPv6 addresses
* IP geolocation
* WHOIS information
* HTTP response information
* HTTP security headers
* SSL/TLS certificate information
* `robots.txt`
* `sitemap.xml`
* Basic security observations

The collected information is compiled into a structured HTML report.

---

## Project Highlights

* Automated DNS reconnaissance
* IPv4 and IPv6 discovery
* IP geolocation with ISP, organization, and ASN information
* WHOIS domain information gathering
* HTTP response analysis
* SSL/TLS certificate analysis
* Security header analysis
* `robots.txt` and `sitemap.xml` discovery
* Automated HTML reconnaissance report generation
* Modular Python architecture
* Input validation
* Logging and verbose output
* Automated unit testing with pytest
* Custom report output path
* Cross-platform setup instructions

---

## Architecture

The framework follows a modular architecture where each reconnaissance task is handled by a separate module.

```text
                    Target Domain / URL
                           |
                           v
                  +-------------------+
                  | Target Validator  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Reconnaissance    |
                  |     Modules       |
                  +---------+---------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
    DNS / IP             WHOIS             HTTP / SSL
        |                   |                   |
        +-------------------+-------------------+
                            |
                            v
                  +-------------------+
                  | Web Files Analysis|
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Security Headers  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Data Aggregation  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | HTML Report       |
                  |    Generator      |
                  +---------+---------+
                            |
                            v
                  Reconnaissance Report
```

---

## Module Structure

| Module                         | Responsibility                           |
| ------------------------------ | ---------------------------------------- |
| `core/validator.py`            | Validates and normalizes the target      |
| `modules/dns_recon.py`         | Collects DNS records                     |
| `modules/ip_recon.py`          | Discovers IPv4/IPv6 addresses            |
| `modules/geolocation_recon.py` | Retrieves IP geolocation information     |
| `modules/whois_recon.py`       | Collects WHOIS information               |
| `modules/http_recon.py`        | Analyzes HTTP responses and headers      |
| `modules/ssl_recon.py`         | Collects SSL/TLS certificate information |
| `modules/web_files_recon.py`   | Checks `robots.txt` and `sitemap.xml`    |
| `modules/security_headers.py`  | Checks important security headers        |
| `modules/report_generator.py`  | Generates the final HTML report          |

---

## Implementation & Engineering Details

The project uses established Python libraries for individual reconnaissance tasks while implementing the overall automation workflow, validation, analysis, error handling, logging, testing, and report generation within the framework.

### Target Validation

The framework validates the supplied domain or URL before reconnaissance begins.

The validator:

* Checks whether the target format is valid
* Normalizes the target
* Prevents invalid targets from reaching reconnaissance modules
* Provides clear validation errors

### Reconnaissance Orchestration

The main application coordinates the individual reconnaissance modules.

The workflow is:

```text
Input Target
     |
     v
Validation
     |
     v
DNS Reconnaissance
     |
     v
IP Discovery
     |
     v
IP Geolocation
     |
     v
WHOIS Reconnaissance
     |
     v
HTTP Reconnaissance
     |
     v
SSL/TLS Reconnaissance
     |
     v
Web Files Analysis
     |
     v
Security Header Analysis
     |
     v
Report Generation
```

---

## Installation

### Prerequisites

Make sure Python 3.x and Git are installed.

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/vk18-tech/Web-Recon-Automation.git
cd Web-Recon-Automation
```

### 2. Create a Virtual Environment

#### Windows PowerShell

```powershell
python -m venv venv
```

#### Windows Command Prompt

```cmd
python -m venv venv
```

#### Linux / macOS

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

After activation, your terminal should display:

```text
(venv)
```

### 4. Install Dependencies

The project dependencies are defined in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

## Usage

The framework requires an authorized domain or URL.

Basic usage:

```bash
python main.py example.com
```

The framework performs:

```text
DNS reconnaissance
        |
        v
IP reconnaissance
        |
        v
IP geolocation
        |
        v
WHOIS reconnaissance
        |
        v
HTTP reconnaissance
        |
        v
SSL/TLS reconnaissance
        |
        v
Web files reconnaissance
        |
        v
Security header analysis
        |
        v
HTML report generation
```

---

## Command-Line Options

### Display Help

```bash
python main.py --help
```

Available options include:

```text
usage: main.py [-h] [--verbose] [--output OUTPUT] target

Automated web reconnaissance and HTML reporting framework.

positional arguments:
  target           Target domain or URL

options:
  -h, --help       show this help message and exit
  --verbose        Display detailed logging information during reconnaissance
  --output OUTPUT  Custom path for the generated HTML report
```

### Custom Report Output

The framework also supports a custom output path:

```bash
python main.py example.com --output reports/custom_report.html
```

### Verbose Logging

Detailed logging can be enabled with:

```bash
python main.py example.com --verbose
```

---

## Technology Stack

* **Language:** Python 3
* **DNS & Network Recon:** `dnspython`
* **WHOIS:** `python-whois`
* **HTTP Analysis:** `requests`
* **SSL/TLS:** Python `ssl` module
* **IP Geolocation:** IP geolocation API
* **Report Generation:** Python / HTML
* **Logging:** Python `logging`
* **Testing:** `pytest`
* **Version Control:** Git & GitHub

---

## Testing

The project includes automated tests for core functionality.

Run the test suite:

```bash
pytest
```

Current test result:

```text
11 passed in 0.09s
```

Test coverage currently includes:

* DNS reconnaissance
* Security header analysis
* Target validation

---

## Project Structure

```text
Web-Recon-Automation/
|
+-- core/
|   +-- __init__.py
|   +-- logger.py
|   +-- validator.py
|
+-- modules/
|   +-- __init__.py
|   +-- dns_recon.py
|   +-- ip_recon.py
|   +-- geolocation_recon.py
|   +-- whois_recon.py
|   +-- http_recon.py
|   +-- ssl_recon.py
|   +-- web_files_recon.py
|   +-- security_headers.py
|   +-- report_generator.py
|
+-- tests/
|   +-- test_dns_recon.py
|   +-- test_security_headers.py
|   +-- test_validator.py
|
+-- reports/
|   +-- recon_report_example.com.html
|
+-- screenshots/
|   +-- 01_framework_execution.png
|   +-- 02_html_report.png
|   +-- 03_security_headers.png
|
+-- logs/
|   +-- recon.log
|
+-- main.py
+-- requirements.txt
+-- pytest.ini
+-- README.md
+-- LICENSE
+-- .gitignore
```

---

## Screenshots

### Framework Execution

![Framework Execution](screenshots/01_framework_execution.png)

### Generated HTML Report

![HTML Report](screenshots/02_html_report.png)

### Security Header Analysis

![Security Header Analysis](screenshots/03_security_headers.png)

---

## Security Considerations

This framework is intended for authorized security assessment and reconnaissance activities.

Only use it against:

* Systems you own
* Systems where you have explicit authorization
* Intentionally vulnerable training environments

The framework performs passive/basic reconnaissance and does not perform exploitation or intrusive vulnerability scanning.

---

## Limitations

* Results depend on DNS, WHOIS, geolocation, and target-server availability.
* Some WHOIS servers may restrict automated queries.
* IP geolocation provides approximate information and should not be treated as an exact physical location.
* Security header findings indicate missing or exposed headers; they do not by themselves confirm a vulnerability.
* `robots.txt` and `sitemap.xml` may not exist on every website.
* Some HTTP or SSL/TLS information may be unavailable when a target is unreachable.
* The framework depends on third-party services and libraries for some reconnaissance functions.
* The framework performs basic reconnaissance and is not a replacement for a full penetration-testing methodology.

---

## Future Improvements

Potential future improvements include:

* Additional DNS record types
* Subdomain enumeration
* Port and service discovery integration
* More comprehensive security header scoring
* Additional report formats such as PDF and JSON
* Expanded automated test coverage
* Threat intelligence API integration
* CVE and vulnerability intelligence integration
* Configurable reconnaissance modules
* CI/CD integration for automated testing

---

## Author

**Shrishti Pandey**

B.Tech Computer Science Student | Cybersecurity Enthusiast | SOC Analyst Aspirant

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
