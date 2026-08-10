import socket


def get_ip_addresses(domain):
    results = {
        "IPv4": [],
        "IPv6": []
    }

    try:
        addresses = socket.getaddrinfo(
            domain,
            None,
            socket.AF_UNSPEC,
            socket.SOCK_STREAM
        )

        for address in addresses:
            ip_address = address[4][0]

            if ":" in ip_address:
                if ip_address not in results["IPv6"]:
                    results["IPv6"].append(ip_address)
            else:
                if ip_address not in results["IPv4"]:
                    results["IPv4"].append(ip_address)

    except socket.gaierror:
        pass

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_ip_addresses(domain)

    print("IPv4 Addresses:")

    for ip in results["IPv4"]:
        print(f"  {ip}")

    print("\nIPv6 Addresses:")

    for ip in results["IPv6"]:
        print(f"  {ip}")