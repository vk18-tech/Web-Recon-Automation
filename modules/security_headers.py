SECURITY_HEADERS = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Frame-Options": "X-Frame-Options",
    "X-Content-Type-Options": "X-Content-Type-Options",
    "Referrer-Policy": "Referrer-Policy",
    "Permissions-Policy": "Permissions-Policy"
}


def analyze_security_headers(headers):
    results = {}

    normalized_headers = {
        key.lower(): value
        for key, value in headers.items()
    }

    for header, display_name in SECURITY_HEADERS.items():
        if header.lower() in normalized_headers:
            results[display_name] = {
                "Status": "Present",
                "Value": normalized_headers[header.lower()]
            }
        else:
            results[display_name] = {
                "Status": "Missing",
                "Value": None
            }

    # Server banner observation
    server = normalized_headers.get("server")

    if server:
        results["Server Banner"] = {
            "Status": "Exposed",
            "Value": server
        }
    else:
        results["Server Banner"] = {
            "Status": "Not Exposed",
            "Value": None
        }

    return results
if __name__ == "__main__":

    test_headers = {
        "Server": "cloudflare",
        "Content-Type": "text/html",
        "Strict-Transport-Security": "max-age=31536000"
    }

    results = analyze_security_headers(test_headers)

    print("\nSecurity Header Analysis")

    for key, value in results.items():
        print(f"\n{key}:")
        print(f"  Status: {value['Status']}")

        if value["Value"]:
            print(f"  Value: {value['Value']}")