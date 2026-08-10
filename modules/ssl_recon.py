import socket
import ssl
from datetime import datetime, timezone


def get_ssl_info(domain):
    results = {
        "TLS Version": None,
        "Subject": None,
        "Issuer": None,
        "Valid From": None,
        "Valid Until": None,
        "Days Remaining": None,
        "Error": None
    }

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_socket:

                certificate = secure_socket.getpeercert()

                results["TLS Version"] = secure_socket.version()

                subject = certificate.get("subject", [])
                issuer = certificate.get("issuer", [])

                results["Subject"] = subject
                results["Issuer"] = issuer

                valid_from = certificate.get("notBefore")
                valid_until = certificate.get("notAfter")

                if valid_from:
                    valid_from_date = datetime.strptime(
                        valid_from,
                        "%b %d %H:%M:%S %Y %Z"
                    )

                    results["Valid From"] = valid_from_date.isoformat()

                if valid_until:
                    valid_until_date = datetime.strptime(
                        valid_until,
                        "%b %d %H:%M:%S %Y %Z"
                    )

                    results["Valid Until"] = valid_until_date.isoformat()

                    now = datetime.now(timezone.utc).replace(tzinfo=None)

                    days_remaining = (
                        valid_until_date - now
                    ).days

                    results["Days Remaining"] = days_remaining

    except (socket.timeout, socket.gaierror, ssl.SSLError, OSError) as error:
        results["Error"] = str(error)

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_ssl_info(domain)

    print("\nSSL/TLS Information")

    for key, value in results.items():
        print(f"\n{key}:")

        if value:
            print(f"  {value}")
        else:
            print("  Not available")