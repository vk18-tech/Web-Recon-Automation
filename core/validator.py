import re
from urllib.parse import urlparse


def validate_target(target):
    """
    Validate and normalize a domain or URL.

    Accepted examples:
        example.com
        www.example.com
        https://example.com
        http://example.com

    Returns:
        normalized domain name as a string

    Raises:
        ValueError for invalid targets
    """

    if not target:
        raise ValueError("Target cannot be empty.")

    target = target.strip()

    # Add a scheme temporarily so urlparse can process domains correctly
    parse_target = target

    if not parse_target.startswith(("http://", "https://")):
        parse_target = "https://" + parse_target

    parsed = urlparse(parse_target)

    hostname = parsed.hostname

    if not hostname:
        raise ValueError("Invalid domain or URL.")

    # Remove trailing dot if present
    hostname = hostname.rstrip(".")

    # Basic hostname validation
    if len(hostname) > 253:
        raise ValueError("Domain name is too long.")

    # Reject localhost / IP addresses for this project
    if hostname.lower() in ["localhost", "127.0.0.1", "::1"]:
        raise ValueError("IP/localhost targets are not accepted.")

    # Domain should contain at least one dot
    if "." not in hostname:
        raise ValueError(
            "Invalid domain. Please provide a domain such as example.com."
        )

    # Validate domain labels
    domain_pattern = re.compile(
        r"^(?=.{1,253}$)"
        r"(?:[a-zA-Z0-9]"
        r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,63}$"
    )

    if not domain_pattern.match(hostname):
        raise ValueError("Invalid domain format.")

    return hostname.lower()