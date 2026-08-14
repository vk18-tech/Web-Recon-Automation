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
    geolocation_results,
    output_path=None
):

    # ========================================
    # Report Path
    # ========================================

    if output_path:
        report_path = Path(output_path)
        report_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    else:
        reports_dir = Path("reports")
        reports_dir.mkdir(
            parents=True,
            exist_ok=True
        )

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

            if key in ["HSTS", "CSP"]:
                severity = "Medium"
            else:
                severity = "Low"

            findings.append({
                "Finding": f"{key} Missing",
                "Status": "Missing",
                "Severity": severity,
                "Observation": (
                    f"{key} security header "
                    f"is not present in the HTTP response."
                )
            })
    # ========================================
    # Scan Summary
    # ========================================

    ipv4_addresses = ip_results.get("IPv4 Addresses", [])
    ipv6_addresses = ip_results.get("IPv6 Addresses", [])

    finding_severities = [
        finding["Severity"]
        for finding in findings
    ]

    severity_order = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    highest_severity = "None"

    if finding_severities:
        highest_severity = max(
            finding_severities,
            key=lambda severity: severity_order.get(
                severity,
                0
            )
        )

    generated_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    summary_html = f"""        <table>
            <tr>
                <th>Target</th>
                <td>{escape(target)}</td>
            </tr>

            <tr>
                <th>Scan Time</th>
                <td>{escape(generated_time)}</td>
            </tr>

            <tr>
                <th>IPv4 Addresses</th>
                <td>{len(ipv4_addresses)}</td>
            </tr>

            <tr>
                <th>IPv6 Addresses</th>
                <td>{len(ipv6_addresses)}</td>
            </tr>

            <tr>
                <th>Security Findings</th>
                <td>{len(findings)}</td>
            </tr>

            <tr>
                <th>Highest Severity</th>
                <td>{escape(highest_severity)}</td>
            </tr>
        </table>
    </section>
    """


    # ========================================
    # DNS Records
    # ========================================

    dns_html = ""

    for record_type, records in dns_results.items():

        dns_html += f"""
        <h3>{escape(record_type)} Records</h3>
        <ul>
            {list_items(records)}
        </ul>
        """

    # ========================================
    # IP Addresses
    # ========================================

    ipv4 = ip_results.get("IPv4", [])
    ipv6 = ip_results.get("IPv6", [])

    ip_html = f"""
    <h3>IPv4 Addresses</h3>
    <ul>
        {list_items(ipv4)}
    </ul>

    <h3>IPv6 Addresses</h3>
    <ul>
        {list_items(ipv6)}
    </ul>
    """

    # ========================================
    # Geolocation
    # ========================================

    geo_html = ""

    if geolocation_results:

        for ip_address, data in geolocation_results.items():

            geo_html += f"""
            <div class="card">
                <h3>{escape(ip_address)}</h3>

                <p><strong>Country:</strong>
                {escape(data.get("Country", "Not available"))}</p>

                <p><strong>Region:</strong>
                {escape(data.get("Region", "Not available"))}</p>

                <p><strong>City:</strong>
                {escape(data.get("City", "Not available"))}</p>

                <p><strong>Postal Code:</strong>
                {escape(data.get("Postal Code", "Not available"))}</p>

                <p><strong>Latitude:</strong>
                {escape(data.get("Latitude", "Not available"))}</p>

                <p><strong>Longitude:</strong>
                {escape(data.get("Longitude", "Not available"))}</p>

                <p><strong>ISP:</strong>
                {escape(data.get("ISP", "Not available"))}</p>

                <p><strong>Organization:</strong>
                {escape(data.get("Organization", "Not available"))}</p>

                <p><strong>ASN:</strong>
                {escape(data.get("ASN", "Not available"))}</p>
            </div>
            """

    else:
        geo_html = "<p>No geolocation information available.</p>"

    # ========================================
    # WHOIS
    # ========================================

    whois_html = ""

    for key, value in whois_results.items():

        whois_html += f"""
        <tr>
            <th>{escape(key)}</th>
            <td>{escape(value)}</td>
        </tr>
        """

    # ========================================
    # HTTP Reconnaissance
    # ========================================

    http_html = ""

    for key, value in http_results.items():

        if key == "Headers":
            continue

        http_html += f"""
        <tr>
            <th>{escape(key)}</th>
            <td>{escape(value)}</td>
        </tr>
        """

    headers_html = ""

    headers = http_results.get("Headers", {})

    if headers:

        for key, value in headers.items():

            headers_html += f"""
            <tr>
                <th>{escape(key)}</th>
                <td>{escape(value)}</td>
            </tr>
            """

    else:

        headers_html = """
        <tr>
            <td colspan="2">No HTTP headers available.</td>
        </tr>
        """

    # ========================================
    # SSL/TLS
    # ========================================

    ssl_html = ""

    for key, value in ssl_results.items():

        ssl_html += f"""
        <tr>
            <th>{escape(key)}</th>
            <td>{escape(value)}</td>
        </tr>
        """

    # ========================================
    # Web Files
    # ========================================

    web_files_html = ""

    for filename, data in web_files_results.items():

        web_files_html += f"""
        <div class="card">

            <h3>{escape(filename)}</h3>

            <p>
                <strong>URL:</strong>
                {escape(data.get("URL", "Not available"))}
            </p>

            <p>
                <strong>Status Code:</strong>
                {escape(data.get("Status Code", "Not available"))}
            </p>

            <p>
                <strong>Error:</strong>
                {escape(data.get("Error", "Not available"))}
            </p>
        """

        content = data.get("Content")

        if content:

            web_files_html += f"""
            <details>
                <summary>View Content</summary>
                <pre>{escape(content[:5000])}</pre>
            </details>
            """

        else:

            web_files_html += """
            <p>Content not available.</p>
            """

        web_files_html += "</div>"

    # ========================================
    # Security Header Results
    # ========================================

    security_html = ""

    for key, value in security_results.items():

        status = value.get("Status", "Not available")
        header_value = value.get("Value")

        security_html += f"""
        <tr>
            <th>{escape(key)}</th>
            <td>{escape(status)}</td>
            <td>{escape(
                header_value if header_value else "Not available"
            )}</td>
        </tr>
        """

    # ========================================
    # Security Findings HTML
    # ========================================

    findings_html = ""

    if findings:

        for finding in findings:

            findings_html += f"""
            <tr>
                <td>{escape(finding["Finding"])}</td>
                <td>{escape(finding["Status"])}</td>
                <td>{escape(finding["Severity"])}</td>
                <td>{escape(finding["Observation"])}</td>
            </tr>
            """

    else:

        findings_html = """
        <tr>
            <td colspan="4">
                No security observations were identified.
            </td>
        </tr>
        """

    # ========================================
    # Generate HTML
    # ========================================

    generated_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

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
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: #f4f6f8;
    color: #222;
}}

header {{
    background: #1f2937;
    color: white;
    padding: 30px;
}}

.container {{
    max-width: 1200px;
    margin: auto;
    padding: 25px;
}}

section {{
    background: white;
    padding: 20px;
    margin-bottom: 25px;
    border-radius: 8px;
}}

h1, h2, h3 {{
    margin-top: 0;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background: #f0f2f5;
}}

ul {{
    line-height: 1.8;
}}

.card {{
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 15px;
    margin-bottom: 15px;
}}

pre {{
    background: #f5f5f5;
    padding: 15px;
    overflow-x: auto;
    white-space: pre-wrap;
}}

footer {{
    text-align: center;
    color: #666;
    padding: 25px;
}}

</style>

</head>

<body>

<header>

<div class="container">

<h1>Web Reconnaissance Report</h1>

<p>
<strong>Target:</strong> {escape(target)}
</p>

<p>
<strong>Generated:</strong> {escape(generated_time)}
</p>

</div>

</header>

<div class="container">

{summary_html}

<section>

<h2>1. DNS Reconnaissance</h2>

{dns_html}

</section>

<section>

<h2>2. IP Reconnaissance</h2>

{ip_html}

</section>

<section>

<h2>3. IP Geolocation</h2>

{geo_html}

</section>

<section>

<h2>4. WHOIS Reconnaissance</h2>

<table>

{whois_html}

</table>

</section>

<section>

<h2>5. HTTP Reconnaissance</h2>

<table>

{http_html}

</table>

<h3>HTTP Headers</h3>

<table>

{headers_html}

</table>

</section>

<section>

<h2>6. SSL/TLS Reconnaissance</h2>

<table>

{ssl_html}

</table>

</section>

<section>

<h2>7. Web Files Reconnaissance</h2>

{web_files_html}

</section>

<section>

<h2>8. Security Header Analysis</h2>

<table>

<tr>
    <th>Header</th>
    <th>Status</th>
    <th>Value</th>
</tr>

{security_html}

</table>

</section>

<section>

<h2>9. Security Findings</h2>

<table>

<tr>
    <th>Finding</th>
    <th>Status</th>
    <th>Severity</th>
    <th>Observation</th>
</tr>

{findings_html}

</table>

</section>

</div>

<footer>

Web Recon Automation Framework

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
    ) as file:

        file.write(html_content)

    # ========================================
    # Return Report Path
    # ========================================

    return report_path