import whois


def get_whois_info(domain):
    results = {
        "Domain": None,
        "Registrar": None,
        "Creation Date": None,
        "Expiration Date": None,
        "Updated Date": None,
        "Name Servers": [],
        "Status": []
    }

    try:
        data = whois.whois(domain)

        results["Domain"] = data.domain_name
        results["Registrar"] = data.registrar
        results["Creation Date"] = data.creation_date
        results["Expiration Date"] = data.expiration_date
        results["Updated Date"] = data.updated_date

        if data.name_servers:
            if isinstance(data.name_servers, list):
                results["Name Servers"] = data.name_servers
            else:
                results["Name Servers"] = [data.name_servers]

        if data.status:
            if isinstance(data.status, list):
                results["Status"] = data.status
            else:
                results["Status"] = [data.status]

    except Exception as error:
        results["Error"] = str(error)

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_whois_info(domain)

    for key, value in results.items():
        print(f"\n{key}:")

        if value:
            print(f"  {value}")
        else:
            print("  Not available")