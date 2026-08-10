import dns.resolver


def get_dns_records(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)

            records = []

            for answer in answers:
                records.append(str(answer))

            results[record_type] = records

        except Exception:
            results[record_type] = []

    return results
if __name__ == "__main__":
    domain = "example.com"

    results = get_dns_records(domain)

    for record_type, records in results.items():
        print(f"\n{record_type} Records:")

        if records:
            for record in records:
                print(f"  {record}")
        else:
            print("  No records found")