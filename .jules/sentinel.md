## 2024-09-03 - Plaintext Credential Exposure in Exception Logs
**Vulnerability:** The script previously printed raw exception objects during proxy request failures. This exposed plaintext proxy passwords, including those with special characters, in the console logs.
**Learning:** The `requests` library incorporates proxy URLs within its exception messages. If unhandled, printing exceptions directly leaks credentials.
**Prevention:** Always sanitize exception messages containing sensitive URLs using regex (e.g., `re.sub(r'(://[^:]+:).*?(@[^@/]+(?:/|$))', r'\1***\2', str(e))`) to mask credentials before logging.
