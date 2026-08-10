## 2024-05-30 - Fix Proxy Credential Leak and Parsing in Sol_Devnet.py
**Vulnerability:** Proxy passwords containing colons were incorrectly truncated, passwords were leaked in console logs, and requests library exceptions could leak unmasked proxy URLs. Proxy credentials were not URL-encoded.
**Learning:** Hardcoded proxy strings sent directly to logs or unencoded in dicts can lead to credential leakage. `requests` objects leak the entire constructed URL on exceptions. Special characters break the `.split` logic if `maxsplit` is not used.
**Prevention:** Always use `.split(":", maxsplit)` for structured credentials. Pre-encode special characters using `urllib.parse.quote`. Scrub logs for URLs matching credential patterns using regex before printing exception text.
