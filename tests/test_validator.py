from core.validator import validate_target


def test_valid_domain():
    result = validate_target("example.com")
    assert result == "example.com"


def test_valid_domain_with_subdomain():
    result = validate_target("www.example.com")
    assert result == "www.example.com"


def test_invalid_domain():
    try:
        validate_target("abc")
        assert False
    except ValueError:
        assert True