import argparse
import logging

from core.validator import validate_target

from modules.dns_recon import get_dns_records
from modules.ip_recon import get_ip_addresses
from modules.geolocation_recon import get_ip_geolocation
from modules.whois_recon import get_whois_info
from modules.http_recon import get_http_info
from modules.ssl_recon import get_ssl_info
from modules.web_files_recon import get_web_files
from modules.security_headers import analyze_security_headers
from modules.report_generator import generate_report


# ========================================
# Logging Configuration
# ========================================

logging.basicConfig(
    filename="logs/recon.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ========================================
# Main Function
# ========================================

def main():

    print("\n# Web Recon Automation Framework")
    print("========================================")

    # ========================================
    # Command Line Arguments
    # ========================================

    parser = argparse.ArgumentParser(
        description="Automated web reconnaissance and HTML reporting framework."
    )

    parser.add_argument(
        "target",
        help="Target domain or URL, for example: example.com"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Display detailed logging information during reconnaissance"
    )

    parser.add_argument(
    "--version",
    action="version",
    version="Web Recon Automation Framework 1.0.0"

   )

    parser.add_argument(
        "--output",
        help="Custom path for the generated HTML report"
    )

    args = parser.parse_args()

    raw_target = args.target
    verbose = args.verbose
    output_path = args.output

    if verbose:
        logger.setLevel(logging.DEBUG)

    # ========================================
    # Target Validation
    # ========================================

    try:

        validated_target = validate_target(raw_target)

    except ValueError as error:

        print(f"\n[!] Invalid target: {error}")

        logger.warning(
            f"Invalid target received: {raw_target} | {error}"
        )

        return

    logger.info(
        f"Target received: {validated_target}"
    )

    print(f"\nTarget: {validated_target}")

    # ========================================
    # DNS Reconnaissance
    # ========================================

    print("\n[+] Starting DNS reconnaissance...")

    logger.info(
        "Starting DNS reconnaissance"
    )

    dns_results = get_dns_records(
        validated_target
    )

    for record_type, records in dns_results.items():

        print(f"\n{record_type} Records:")

        if records:

            for record in records:
                print(record)

        else:

            print("No records found")

    logger.info(
        "DNS reconnaissance completed"
    )

    # ========================================
    # IP Reconnaissance
    # ========================================

    print("\n[+] Starting IP reconnaissance...")

    logger.info(
        "Starting IP reconnaissance"
    )

    ip_results = get_ip_addresses(
        validated_target
    )

    print("\nIPv4 Addresses:")

    ipv4_addresses = ip_results.get(
        "IPv4",
        []
    )

    if ipv4_addresses:

        for ip in ipv4_addresses:
            print(ip)

    else:

        print("No IPv4 addresses found")

    print("\nIPv6 Addresses:")

    ipv6_addresses = ip_results.get(
        "IPv6",
        []
    )

    if ipv6_addresses:

        for ip in ipv6_addresses:
            print(ip)

    else:

        print("No IPv6 addresses found")

    logger.info(
        "IP reconnaissance completed"
    )

    # ========================================
    # IP Geolocation
    # ========================================

    print("\n[+] Starting IP geolocation...")

    logger.info(
        "Starting IP geolocation"
    )

    all_ips = (
        ipv4_addresses +
        ipv6_addresses
    )

    if all_ips:

        geolocation_results = get_ip_geolocation(
            all_ips
        )

        for ip, location in geolocation_results.items():

            print(f"\nIP Address: {ip}")

            print(
                f"Country: "
                f"{location.get('Country', 'Not available')}"
            )

            print(
                f"Region: "
                f"{location.get('Region', 'Not available')}"
            )

            print(
                f"City: "
                f"{location.get('City', 'Not available')}"
            )

            print(
                f"Postal Code: "
                f"{location.get('Postal Code', 'Not available')}"
            )

            print(
                f"Latitude: "
                f"{location.get('Latitude', 'Not available')}"
            )

            print(
                f"Longitude: "
                f"{location.get('Longitude', 'Not available')}"
            )

            print(
                f"ISP: "
                f"{location.get('ISP', 'Not available')}"
            )

            print(
                f"Organization: "
                f"{location.get('Organization', 'Not available')}"
            )

            print(
                f"ASN: "
                f"{location.get('ASN', 'Not available')}"
            )

    else:

        geolocation_results = {}

        print(
            "No IP addresses available for geolocation"
        )

    logger.info(
        "IP geolocation completed"
    )

    # ========================================
    # WHOIS Reconnaissance
    # ========================================

    print("\n[+] Starting WHOIS reconnaissance...")

    logger.info(
        "Starting WHOIS reconnaissance"
    )

    whois_results = get_whois_info(
        validated_target
    )

    for key, value in whois_results.items():

        print(f"\n{key}:")

        if value:

            print(f"  {value}")

        else:

            print("  Not available")

    logger.info(
        "WHOIS reconnaissance completed"
    )

    # ========================================
    # HTTP Reconnaissance
    # ========================================

    print("\n[+] Starting HTTP reconnaissance...")

    logger.info(
        "Starting HTTP reconnaissance"
    )

    http_results = get_http_info(
        validated_target
    )

    for key, value in http_results.items():

        if key == "Headers":
            continue

        print(f"\n{key}:")

        if value:

            print(f"  {value}")

        else:

            print("  Not available")

    print("\nHTTP Headers:")

    headers = http_results.get(
        "Headers",
        {}
    )

    if headers:

        for key, value in headers.items():

            print(
                f"{key}: {value}"
            )

    else:

        print("No headers found")

    if http_results.get("Error"):

        print(
            f"\nHTTP Error:"
            f"\n{http_results['Error']}"
        )

    logger.info(
        "HTTP reconnaissance completed"
    )

    # ========================================
    # SSL/TLS Reconnaissance
    # ========================================

    print("\n[+] Starting SSL/TLS reconnaissance...")

    logger.info(
        "Starting SSL/TLS reconnaissance"
    )

    ssl_results = get_ssl_info(
        validated_target
    )

    for key, value in ssl_results.items():

        print(f"\n{key}:")

        if value:

            print(f"  {value}")

        else:

            print("  Not available")

    logger.info(
        "SSL/TLS reconnaissance completed"
    )

    # ========================================
    # Web Files Reconnaissance
    # ========================================

    print("\n[+] Starting web files reconnaissance...")

    logger.info(
        "Starting web files reconnaissance"
    )

    web_files_results = get_web_files(
        validated_target
    )

    for filename, data in web_files_results.items():

        print(f"\n{filename}:")

        print(
            f"URL: "
            f"{data.get('URL', 'Not available')}"
        )

        print(
            f"Status Code: "
            f"{data.get('Status Code', 'Not available')}"
        )

        if data.get("Content"):

            print(
                f"Content:\n"
                f"{data['Content']}"
            )

        else:

            print("Content not available")

        if data.get("Error"):

            print(
                f"Error: "
                f"{data['Error']}"
            )

    logger.info(
        "Web files reconnaissance completed"
    )

    # ========================================
    # Security Header Analysis
    # ========================================

    print("\n[+] Starting security header analysis...")

    logger.info(
        "Starting security header analysis"
    )

    security_results = analyze_security_headers(
        http_results.get(
            "Headers",
            {}
        )
    )

    print("\nSecurity Header Analysis")

    for key, value in security_results.items():

        print(f"\n{key}:")

        print(
            f"Status: "
            f"{value.get('Status', 'Not available')}"
        )

        if value.get("Value"):

            print(
                f"Value: "
                f"{value['Value']}"
            )

    logger.info(
        "Security header analysis completed"
    )

    # ========================================
    # HTML Report Generation
    # ========================================

    print(
        "\n[+] Generating HTML reconnaissance report..."
    )

    logger.info(
        "Starting HTML report generation"
    )

    report_path = generate_report(
        target=validated_target,
        dns_results=dns_results,
        ip_results=ip_results,
        whois_results=whois_results,
        http_results=http_results,
        ssl_results=ssl_results,
        web_files_results=web_files_results,
        security_results=security_results,
        geolocation_results=geolocation_results,
        output_path=output_path
    )

    print(
        "\n[+] Report generated successfully!"
    )

    print(
        f"[+] Report location: "
        f"{report_path}"
    )

    logger.info(
        f"Report generated successfully: "
        f"{report_path}"
    )


# ========================================
# Program Entry Point
# ========================================

if __name__ == "__main__":
    main()