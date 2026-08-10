# Web Recon Automation Framework

A modular Python-based reconnaissance framework that automates the collection of publicly available information about an authorized web target and generates a structured HTML reconnaissance report.

The project is designed to demonstrate practical cybersecurity automation, modular Python development, reconnaissance techniques, error handling, logging, and security reporting.

---

## Project Objective

During a penetration testing or security assessment, reconnaissance can involve repeatedly using multiple tools to collect information about a target.

This project automates that initial reconnaissance process by providing a single command-line interface.

The framework accepts a domain or URL and collects:

- DNS records
- IPv4 and IPv6 addresses
- IP geolocation
- WHOIS information
- HTTP response information
- HTTP security headers
- SSL/TLS certificate information
- robots.txt
- sitemap.xml
- Basic security observations

The collected information is then compiled into a professional HTML report.

---

## Features

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

- robots.txt
- sitemap.xml

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