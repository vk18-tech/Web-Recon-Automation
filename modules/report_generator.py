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