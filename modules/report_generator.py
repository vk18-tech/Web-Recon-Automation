from pathlib import Path
from datetime import datetime
import html


def generate_report(
    target,
    dns_results,
    ip_results,
    whois_results,
    http_results,
    ssl_results,
    web_files_results,
    security_results,
    geolocation_results
):

    # ========================================
    # Report Directory
    # ========================================

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    safe_target = (
        target
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    report_path = (
        reports_dir /
        f"recon_report_{safe_target}.html"
    )

    # ========================================
    # Helper Functions
    # ========================================

    def escape(value):
        return html.escape(str(value))

    def list_items(values):

        if not values:
            return "<li>No records found</li>"

        return "".join(
            f"<li>{escape(value)}</li>"
            for value in values
        )

    # ========================================
    # Security Findings
    # ========================================

    findings = []

    for key, value in security_results.items():

        status = value.get("Status", "")
        header_value = value.get("Value", "")

        if key == "Server Banner" and status == "Exposed":

            findings.append({
                "Finding": "Server Banner Exposed",
                "Status": "Exposed",
                "Severity": "Low",
                "Observation": (
                    f"Server information is exposed: "
                    f"{header_value}"
                )
            })

        elif status == "Missing":

            if key in ["HSTS", "CSP", "X-Frame-Options"]:
                severity = "Medium"
            else:
                severity = "Low"

            findings.append({
                "Finding": f"{key} Missing",
                "Status": "Missing",
                "Severity": severity,
                "Observation": (
                    f"{key} security header "
                    f"was not observed in the HTTP response."
                )
            })

    # ========================================
    # Module Status
    # ========================================

    module_status = {
        "DNS Reconnaissance": "Completed",
        "IP Reconnaissance": "Completed",
        "IP Geolocation": (
            "Completed"
            if geolocation_results
            else "No data"
        ),
        "WHOIS Reconnaissance": "Completed",
        "HTTP Reconnaissance": "Completed",
        "SSL/TLS Reconnaissance": "Completed",
        "Web Files Reconnaissance": "Completed",
        "Security Header Analysis": "Completed"
    }

    # ========================================
    # Summary Counts
    # ========================================

    high_count = sum(
        1 for finding in findings
        if finding["Severity"] == "High"
    )

    medium_count = sum(
        1 for finding in findings
        if finding["Severity"] == "Medium"
    )

    low_count = sum(
        1 for finding in findings
        if finding["Severity"] == "Low"
    )

    info_count = sum(
        1 for finding in findings
        if finding["Severity"] == "Informational"
    )

    # ========================================
    # HTML Start
    # ========================================

    html_content = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>
Web Reconnaissance Report - {escape(target)}
</title>

<style>

body {{
    font-family:
        Arial,
        Helvetica,
        sans-serif;

    margin: 0;

    background: #f4f6f8;

    color: #222;
}}

header {{
    background: #17202a;

    color: white;

    padding: 35px;
}}

header h1 {{
    margin: 0 0 10px 0;
}}

.container {{
    width: 92%;

    max-width: 1250px;

    margin: 30px auto;
}}

section {{
    background: white;

    padding: 25px;

    margin-bottom: 25px;

    border-radius: 8px;

    box-shadow:
        0 2px 8px rgba(0,0,0,0.08);
}}

h2 {{
    border-bottom:
        2px solid #ddd;

    padding-bottom: 10px;
}}

h3 {{
    margin-top: 25px;
}}

table {{
    width: 100%;

    border-collapse:
        collapse;

    margin-top: 15px;
}}

th,
td {{
    border:
        1px solid #ddd;

    padding: 10px;

    text-align: left;

    vertical-align: top;
}}

th {{
    background: #f0f2f4;
}}

ul {{
    line-height: 1.8;
}}

.summary-grid {{
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 15px;

    margin-top: 20px;
}}

.summary-card {{
    padding: 20px;

    border-radius: 8px;

    text-align: center;

    background: #f4f6f8;
}}

.summary-card h3 {{
    margin: 0;

    font-size: 28px;
}}

.summary-card p {{
    margin-bottom: 0;
}}

.high {{
    border-left:
        5px solid #c0392b;
}}

.medium {{
    border-left:
        5px solid #e67e22;
}}

.low {{
    border-left:
        5px solid #f1c40f;
}}

.info {{
    border-left:
        5px solid #3498db;
}}

.status-completed {{
    font-weight: bold;
}}

.finding-note {{
    background: #f8f9fa;

    padding: 15px;

    border-left:
        4px solid #3498db;

    margin-top: 15px;
}}

pre {{
    white-space:
        pre-wrap;

    word-wrap:
        break-word;
}}

footer {{
    text-align: center;

    padding: 25px;

    color: #666;
}}

</style>

</head>

<body>

<header>

<h1>Web Reconnaissance Report</h1>

<p>
<strong>Target:</strong>
{escape(target)}
</p>

<p>
<strong>Generated:</strong>
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
</p>

<p>
<strong>Assessment Type:</strong>
Passive / Basic Web Reconnaissance
</p>

</header>

<div class="container">

<!-- ======================================== -->
<!-- EXECUTIVE SUMMARY -->
<!-- ======================================== -->

<section>

<h2>1. Executive Summary</h2>

<p>
This report summarizes publicly observable reconnaissance
information collected for the specified target using the
Web Recon Automation Framework.
</p>

<p>
The framework collected DNS, IP addressing, IP geolocation,
WHOIS, HTTP, SSL/TLS, web-file and security-header information.
</p>

<div class="summary-grid">

<div class="summary-card high">

<h3>{high_count}</h3>

<p>High Findings</p>

</div>

<div class="summary-card medium">

<h3>{medium_count}</h3>

<p>Medium Findings</p>

</div>

<div class="summary-card low">

<h3>{low_count}</h3>

<p>Low Findings</p>

</div>

<div class="summary-card info">

<h3>{info_count}</h3>

<p>Informational</p>

</div>

</div>

<div class="finding-note">

<strong>Important:</strong>

Security header observations are indicators of potential
security hardening opportunities. They do not by themselves
prove that the target is vulnerable.

</div>

</section>

<!-- ======================================== -->
<!-- MODULE STATUS -->
<!-- ======================================== -->

<section>

<h2>2. Reconnaissance Module Status</h2>

<table>

<tr>

<th>Module</th>

<th>Status</th>

</tr>
"""

    for module, status in module_status.items():

        html_content += f"""
<tr>

<td>{escape(module)}</td>

<td class="status-completed">
{escape(status)}
</td>

</tr>
"""

    html_content += """

</table>

</section>

<!-- ======================================== -->
<!-- SECURITY FINDINGS -->
<!-- ======================================== -->

<section>

<h2>3. Security Findings</h2>

<table>

<tr>

<th>Finding</th>

<th>Status</th>

<th>Severity</th>

<th>Observation</th>

</tr>
"""

    if findings:

        for finding in findings:

            severity_class = (
                finding["Severity"].lower()
            )

            html_content += f"""

<tr>

<td>{escape(finding["Finding"])}</td>

<td>{escape(finding["Status"])}</td>

<td class="{severity_class}">
<strong>
{escape(finding["Severity"])}
</strong>
</td>

<td>{escape(finding["Observation"])}</td>

</tr>

"""

    else:

        html_content += """

<tr>

<td colspan="4">
No security observations were identified.
</td>

</tr>

"""

    html_content += """

</table>

</section>

<!-- ======================================== -->
<!-- DNS -->
<!-- ======================================== -->

<section>

<h2>4. DNS Reconnaissance</h2>
"""

    for record_type, records in dns_results.items():

        html_content += f"""

<h3>{escape(record_type)} Records</h3>

<ul>

{list_items(records)}

</ul>

"""

    html_content += """

</section>

<!-- ======================================== -->
<!-- IP -->
<!-- ======================================== -->

<section>

<h2>5. IP Addresses</h2>

<h3>IPv4 Addresses</h3>

<ul>
"""

    html_content += list_items(
        ip_results.get("IPv4", [])
    )

    html_content += """

</ul>

<h3>IPv6 Addresses</h3>

<ul>
"""

    html_content += list_items(
        ip_results.get("IPv6", [])
    )

    html_content += """

</ul>

</section>

<!-- ======================================== -->
<!-- GEOLOCATION -->
<!-- ======================================== -->

<section>

<h2>6. IP Geolocation</h2>

<table>

<tr>

<th>IP Address</th>
<th>Country</th>
<th>Region</th>
<th>City</th>
<th>Postal Code</th>
<th>ISP</th>
<th>Organization</th>
<th>ASN</th>

</tr>
"""

    if geolocation_results:

        for ip, location in geolocation_results.items():

            html_content += f"""

<tr>

<td>{escape(ip)}</td>

<td>
{escape(location.get("Country", "Not available"))}
</td>

<td>
{escape(location.get("Region", "Not available"))}
</td>

<td>
{escape(location.get("City", "Not available"))}
</td>

<td>
{escape(location.get("Postal Code", "Not available"))}
</td>

<td>
{escape(location.get("ISP", "Not available"))}
</td>

<td>
{escape(location.get("Organization", "Not available"))}
</td>

<td>
{escape(location.get("ASN", "Not available"))}
</td>

</tr>

"""

    else:

        html_content += """

<tr>

<td colspan="8">
Geolocation information not available.
</td>

</tr>

"""

    html_content += """

</table>

<p>

<strong>Note:</strong>
IP geolocation is approximate and represents information
associated with the network/IP address. It should not be
interpreted as the physical location of a specific person
or device.

</p>

</section>

<!-- ======================================== -->
<!-- WHOIS -->
<!-- ======================================== -->

<section>

<h2>7. WHOIS Information</h2>

<table>
"""

    for key, value in whois_results.items():

        html_content += f"""

<tr>

<th>{escape(key)}</th>

<td>
{escape(value) if value else "Not available"}
</td>

</tr>

"""

    html_content += """

</table>

</section>

<!-- ======================================== -->
<!-- HTTP -->
<!-- ======================================== -->

<section>

<h2>8. HTTP Reconnaissance</h2>

<table>
"""

    for key, value in http_results.items():

        if key == "Headers":
            continue

        html_content += f"""

<tr>

<th>{escape(key)}</th>

<td>
{escape(value) if value else "Not available"}
</td>

</tr>

"""

    html_content += """

</table>

<h3>HTTP Headers</h3>

<table>

<tr>

<th>Header</th>

<th>Value</th>

</tr>
"""

    headers = http_results.get(
        "Headers",
        {}
    )

    if headers:

        for key, value in headers.items():

            html_content += f"""

<tr>

<td>{escape(key)}</td>

<td>{escape(value)}</td>

</tr>

"""

    else:

        html_content += """

<tr>

<td colspan="2">
No headers found
</td>

</tr>

"""

    html_content += """

</table>

</section>

<!-- ======================================== -->
<!-- SSL/TLS -->
<!-- ======================================== -->

<section>

<h2>9. SSL/TLS Information</h2>

<table>
"""

    for key, value in ssl_results.items():

        html_content += f"""

<tr>

<th>{escape(key)}</th>

<td>
{escape(value) if value else "Not available"}
</td>

</tr>

"""

    html_content += """

</table>

</section>

<!-- ======================================== -->
<!-- WEB FILES -->
<!-- ======================================== -->

<section>

<h2>10. Web Files</h2>
"""

    for filename, data in web_files_results.items():

        html_content += f"""

<h3>{escape(filename)}</h3>

<table>

<tr>

<th>URL</th>

<td>
{escape(data.get("URL", "Not available"))}
</td>

</tr>

<tr>

<th>Status Code</th>

<td>
{escape(data.get("Status Code", "Not available"))}
</td>

</tr>

<tr>

<th>Content</th>

<td>
"""

        if data.get("Content"):

            html_content += (
                "<pre>"
                + escape(data["Content"])
                + "</pre>"
            )

        else:

            html_content += "Not available"

        html_content += """

</td>

</tr>

</table>

"""

    html_content += """

</section>

<!-- ======================================== -->
<!-- SECURITY HEADERS -->
<!-- ======================================== -->

<section>

<h2>11. Detailed Security Header Analysis</h2>

<table>

<tr>

<th>Security Header</th>

<th>Status</th>

<th>Value</th>

</tr>
"""

    for key, value in security_results.items():

        status = value.get(
            "Status",
            "Not available"
        )

        header_value = value.get(
            "Value",
            ""
        )

        html_content += f"""

<tr>

<td>{escape(key)}</td>

<td>{escape(status)}</td>

<td>
{
    escape(header_value)
    if header_value
    else "—"
}
</td>

</tr>

"""

    html_content += """

</table>

</section>

</div>

<footer>

Web Recon Automation Framework<br>

Automated Reconnaissance Report

</footer>

</body>

</html>
"""

    # ========================================
    # Write Report
    # ========================================

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as report_file:

        report_file.write(html_content)

    return str(report_path)