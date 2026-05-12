import urllib.parse

def mask_proxy(proxy_str):
    parts = proxy_str.split(":")
    if len(parts) == 4:
        return f"{parts[0]}:{parts[1]}:{parts[2]}:***"
    elif len(parts) == 2:
        return proxy_str
    return "***"

def get_proxy_dict(proxy_str):
    parts = proxy_str.split(":")
    if len(parts) != 4:
        return None

    host, port, user, password = parts
    user_enc = urllib.parse.quote(user, safe='')
    pass_enc = urllib.parse.quote(password, safe='')
    proxy_auth = f"{user_enc}:{pass_enc}@{host}:{port}"
    return {
        "http": f"http://{proxy_auth}",
        "https": f"http://{proxy_auth}"
    }

print(mask_proxy("1.2.3.4:8080:user:pass"))
print(get_proxy_dict("1.2.3.4:8080:user:pa@ss"))
