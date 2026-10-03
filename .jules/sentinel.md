## 2024-05-24 - Exposed Credentials in Python Requests Proxy Exceptions
**Vulnerability:** Proxy credentials (username/password) embedded in proxy URLs are leaked in plaintext through `requests` exceptions when network connection fails, and printed directly to console output.
**Learning:** The `requests` library automatically percent-encodes credentials in URLs. When exceptions are raised (like connection timeouts), the raw error message string preserves this full URL, exposing sensitive credentials. Normal application logging doesn't catch these auto-generated exception strings.
**Prevention:**
1. Always parse/split proxy strings to mask passwords before logging.
2. Explicitly percent-encode user/pass using `urllib.parse.quote` for proxy dicts.
3. Use a regex pattern like `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))` to sanitize any exception object strings containing proxy URLs before printing/logging them.
