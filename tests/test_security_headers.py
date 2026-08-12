from modules.security_headers import analyze_security_headers


def test_security_headers_present():
    headers = {
        "Strict-Transport-Security": "max-age=31536000",
        "Content-Security-Policy": "default-src 'self'",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "geolocation=()",
    }

    results = analyze_security_headers(headers)

    assert results["HSTS"]["Status"] == "Present"
    assert results["CSP"]["Status"] == "Present"
    assert results["X-Frame-Options"]["Status"] == "Present"
    assert results["X-Content-Type-Options"]["Status"] == "Present"
    assert results["Referrer-Policy"]["Status"] == "Present"
    assert results["Permissions-Policy"]["Status"] == "Present"


def test_missing_security_headers():
    headers = {}

    results = analyze_security_headers(headers)

    assert results["HSTS"]["Status"] == "Missing"
    assert results["CSP"]["Status"] == "Missing"
    assert results["X-Frame-Options"]["Status"] == "Missing"
    assert results["X-Content-Type-Options"]["Status"] == "Missing"
    assert results["Referrer-Policy"]["Status"] == "Missing"
    assert results["Permissions-Policy"]["Status"] == "Missing"


def test_server_banner_exposed():
    headers = {
        "Server": "cloudflare"
    }

    results = analyze_security_headers(headers)

    assert results["Server Banner"]["Status"] == "Exposed"
    assert results["Server Banner"]["Value"] == "cloudflare"


def test_server_banner_not_exposed():
    headers = {}

    results = analyze_security_headers(headers)

    assert results["Server Banner"]["Status"] == "Not Exposed"
    assert results["Server Banner"]["Value"] is None


def test_case_insensitive_headers():
    headers = {
        "strict-transport-security": "max-age=31536000",
        "CONTENT-SECURITY-POLICY": "default-src 'self'",
        "server": "cloudflare"
    }

    results = analyze_security_headers(headers)

    assert results["HSTS"]["Status"] == "Present"
    assert results["CSP"]["Status"] == "Present"
    assert results["Server Banner"]["Status"] == "Exposed"