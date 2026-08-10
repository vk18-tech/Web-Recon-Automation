import requests


def get_web_files(domain):
    results = {
        "robots.txt": {
            "URL": f"https://{domain}/robots.txt",
            "Status Code": None,
            "Content": None,
            "Error": None
        },
        "sitemap.xml": {
            "URL": f"https://{domain}/sitemap.xml",
            "Status Code": None,
            "Content": None,
            "Error": None
        }
    }

    for filename in results:
        url = results[filename]["URL"]

        try:
            response = requests.get(
                url,
                timeout=10
            )

            results[filename]["Status Code"] = response.status_code

            if response.ok:
                results[filename]["Content"] = response.text
            else:
                results[filename]["Content"] = None

        except requests.RequestException as error:
            results[filename]["Error"] = str(error)

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_web_files(domain)

    for filename, data in results.items():
        print(f"\n{'=' * 40}")
        print(filename)
        print(f"{'=' * 40}")

        print(f"URL: {data['URL']}")
        print(f"Status Code: {data['Status Code']}")

        if data["Content"]:
            print("\nContent:")
            print(data["Content"][:2000])
        else:
            print("\nContent: Not available")

        if data["Error"]:
            print(f"\nError: {data['Error']}")