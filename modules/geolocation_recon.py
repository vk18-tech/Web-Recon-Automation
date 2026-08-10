import requests
import logging


logger = logging.getLogger(__name__)


def get_ip_geolocation(ip_addresses):
    """
    Collect basic geolocation information for a list of IP addresses.

    Returns:
        Dictionary containing geolocation information for each IP.
    """

    results = {}

    if not ip_addresses:
        logger.info(
            "No IP addresses available for geolocation"
        )
        return results

    for ip in ip_addresses:

        try:

            response = requests.get(
                f"https://ipwho.is/{ip}",
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if not data.get("success", False):

                results[ip] = {
                    "Country": "Not available",
                    "Region": "Not available",
                    "City": "Not available",
                    "Postal Code": "Not available",
                    "Latitude": "Not available",
                    "Longitude": "Not available",
                    "ISP": "Not available",
                    "Organization": "Not available",
                    "ASN": "Not available"
                }

                continue

            connection = data.get(
                "connection",
                {}
            )

            results[ip] = {
                "Country": data.get(
                    "country",
                    "Not available"
                ),

                "Region": data.get(
                    "region",
                    "Not available"
                ),

                "City": data.get(
                    "city",
                    "Not available"
                ),

                "Postal Code": data.get(
                    "postal",
                    "Not available"
                ),

                "Latitude": data.get(
                    "latitude",
                    "Not available"
                ),

                "Longitude": data.get(
                    "longitude",
                    "Not available"
                ),

                "ISP": connection.get(
                    "isp",
                    "Not available"
                ),

                "Organization": connection.get(
                    "org",
                    "Not available"
                ),

                "ASN": connection.get(
                    "asn",
                    "Not available"
                )
            }

            logger.info(
                f"Geolocation collected for {ip}"
            )

        except requests.RequestException as error:

            logger.warning(
                f"Geolocation request failed for "
                f"{ip}: {error}"
            )

            results[ip] = {
                "Country": "Not available",
                "Region": "Not available",
                "City": "Not available",
                "Postal Code": "Not available",
                "Latitude": "Not available",
                "Longitude": "Not available",
                "ISP": "Not available",
                "Organization": "Not available",
                "ASN": "Not available",
                "Error": str(error)
            }

        except Exception as error:

            logger.exception(
                f"Unexpected geolocation error "
                f"for {ip}: {error}"
            )

            results[ip] = {
                "Country": "Not available",
                "Region": "Not available",
                "City": "Not available",
                "Postal Code": "Not available",
                "Latitude": "Not available",
                "Longitude": "Not available",
                "ISP": "Not available",
                "Organization": "Not available",
                "ASN": "Not available",
                "Error": str(error)
            }

    return results