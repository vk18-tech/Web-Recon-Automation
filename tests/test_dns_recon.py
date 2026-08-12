from modules.dns_recon import get_dns_records


def test_dns_records_success(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    def fake_resolve(domain, record_type):
        fake_records = {
            "A": [FakeAnswer("93.184.216.34")],
            "AAAA": [FakeAnswer("2606:2800:220:1:248:1893:25c8:1946")],
            "MX": [FakeAnswer("10 mail.example.com.")],
            "NS": [FakeAnswer("ns1.example.com.")],
            "TXT": [FakeAnswer("v=spf1 -all")],
            "CNAME": [FakeAnswer("www.example.com.")]
        }

        return fake_records[record_type]

    monkeypatch.setattr(
        "dns.resolver.resolve",
        fake_resolve
    )

    results = get_dns_records("example.com")

    assert results["A"] == ["93.184.216.34"]
    assert results["AAAA"] == [
        "2606:2800:220:1:248:1893:25c8:1946"
    ]
    assert results["MX"] == ["10 mail.example.com."]
    assert results["NS"] == ["ns1.example.com."]
    assert results["TXT"] == ["v=spf1 -all"]
    assert results["CNAME"] == ["www.example.com."]


def test_dns_records_empty(monkeypatch):
    def fake_resolve(domain, record_type):
        raise Exception("DNS record not found")

    monkeypatch.setattr(
        "dns.resolver.resolve",
        fake_resolve
    )

    results = get_dns_records("nonexistent.example")

    assert results["A"] == []
    assert results["AAAA"] == []
    assert results["MX"] == []
    assert results["NS"] == []
    assert results["TXT"] == []
    assert results["CNAME"] == []


def test_dns_record_types():
    expected_types = {
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME"
    }

    def fake_resolve(domain, record_type):
        return []

    import dns.resolver

    original_resolve = dns.resolver.resolve

    try:
        dns.resolver.resolve = fake_resolve

        results = get_dns_records("example.com")

        assert set(results.keys()) == expected_types

    finally:
        dns.resolver.resolve = original_resolve