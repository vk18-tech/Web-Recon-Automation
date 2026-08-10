import requests
import time


def get_http_info(domain):
    url = f"https://{domain}"

    results = {
        "URL": url,
        "Status Code": None,
        "Response Time": None,
        "Server": None,
        "Content-Type": None,
        "Headers": {},
        "Error": None
    }

    try:
        start_time = time.perf_counter()

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        end_time = time.perf_counter()

        results["URL"] = response.url
        results["Status Code"] = response.status_code
        results["Response Time"] = round(end_time - start_time, 3)
        results["Server"] = response.headers.get("Server")
        results["Content-Type"] = response.headers.get("Content-Type")
        results["Headers"] = dict(response.headers)

    except requests.RequestException as error:
        results["Error"] = str(error)

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_http_info(domain)

    print(f"\nURL: {results['URL']}")
    print(f"Status Code: {results['Status Code']}")
    print(f"Response Time: {results['Response Time']} seconds")
    print(f"Server: {results['Server']}")
    print(f"Content-Type: {results['Content-Type']}")

    print("\nHTTP Headers:")

    for key, value in results["Headers"].items():
        print(f"{key}: {value}")

    if results["Error"]:
        print(f"\nError: {results['Error']}")