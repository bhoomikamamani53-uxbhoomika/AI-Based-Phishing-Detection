
from urllib.parse import urlparse
import re

def extract_features(url):

    features = {}

    parsed_url = urlparse(url)

    features["url_length"] = len(url)

    # Detect IP address
    features["has_ip"] = 1 if re.search(
        r'(\d{1,3}\.){3}\d{1,3}', parsed_url.netloc
    ) else 0

    features["has_https"] = 1 if parsed_url.scheme == "https" else 0

    features["dot_count"] = url.count(".")

    features["hyphen_count"] = url.count("-")

    features["at_symbol"] = 1 if "@" in url else 0

    features["double_slash"] = 1 if url.count("//") > 1 else 0

    features["subdomain_count"] = max(
        0, len(parsed_url.hostname.split(".")) - 2
    ) if parsed_url.hostname else 0

    features["has_suspicious_word"] = 1 if any(
        word in url.lower()
        for word in ["login", "verify", "secure", "update", "account"]
    ) else 0

    features["question_mark"] = url.count("?")

    features["equal_count"] = url.count("=")

    features["ampersand_count"] = url.count("&")

    features["slash_count"] = url.count("/")

    features["digit_count"] = sum(c.isdigit() for c in url)

    features["shortening_service"] = 1 if any(
        service in parsed_url.netloc.lower()
        for service in ["bit.ly", "tinyurl.com", "t.co"]
    ) else 0
    return features
