
## 2024-04-21 - [Prevent Local IP Leakage on Proxy Failure]
**Vulnerability:** If a malformed proxy is provided to the script, `get_proxy_dict` would either throw `ValueError` due to split unpacking issues or return an invalid structure. If handled improperly, subsequent requests to external APIs could proceed without a proxy, silently exposing the local host IP.
**Learning:** Network request routines must halt gracefully if explicit proxy configurations are malformed or missing when a proxy is strictly expected.
**Prevention:** Always validate proxy string formats thoroughly before building proxy configuration dictionaries. On failure, return `None` and enforce early exit from the network operation.
