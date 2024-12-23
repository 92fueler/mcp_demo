from typing import Any

import httpx

from config import USER_AGENT

async def make_nws_request(client: httpx.AsyncClient, url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }

    try:
        response = await client.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a concise string."""
    props = feature["properties"]
    return (
        f"Event: {props.get('event', 'Unknown')}\n"
        f"Area: {props.get('areaDesc', 'Unknown')}\n"
        f"Severity: {props.get('severity', 'Unknown')}\n"
        f"Status: {props.get('status', 'Unknown')}\n"
        f"Headline: {props.get('headline', 'No headline')}\n"
        "---"
    )
