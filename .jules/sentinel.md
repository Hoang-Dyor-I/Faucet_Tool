## 2024-07-18 - Exposed Proxy Credentials
**Vulnerability:** Proxy passwords containing sensitive credentials were inadvertently exposed in cleartext within stdout logs (e.g., `print(f"\n🌐 Đang dùng proxy: {proxy}")`) and raw Exception objects thrown by the `requests` library when proxy connections failed.
**Learning:** Python's `requests` library incorporates fully reconstructed proxy connection URLs—including credentials—into error messages on connection failure. Direct string casting or printing of raw Exception objects (`print(e)`) will passively leak these credentials.
**Prevention:** Always parse and mask sensitive configuration values prior to logging, and utilize regex replacements (e.g., `re.sub(r'(://[^:]+:).*?(@)', r'\1***\2', str(e))`) to sanitize raw library exceptions before they reach console or file outputs.

## 2024-07-18 - Arbitrary Input in Connection Strings
**Vulnerability:** User-provided proxy credentials containing special characters (like `%`, `@`, or `/`) were directly interpolated into URL connection strings without URL-encoding.
**Learning:** Failing to URL-encode password fields breaks proxy URL parsing. More critically, unencoded input fed into structured URL strings can lead to injection vectors where malicious strings modify the host, port, or schema portions of the connection logic.
**Prevention:** Always use `urllib.parse.quote(..., safe='')` to percent-encode arbitrary user input (like usernames and passwords) before injecting it into structured URIs.
