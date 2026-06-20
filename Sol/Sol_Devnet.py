import requests
import random
import time
import threading
import urllib.parse
import re

FAUCET_URL = "https://api.devnet.solana.com"
MIN_THREADS = 20
MAX_THREADS = 25
REQUEST_INTERVAL = 10  # giây giữa các batch
DELAY_BETWEEN_REQUESTS = (1, 3)  # delay ngẫu nhiên mỗi request (giây)

def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def get_proxy_dict(proxy_str):
    parts = proxy_str.split(":", 3)
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

def mask_proxy(proxy_str):
    parts = proxy_str.split(":", 3)
    if len(parts) == 4:
        host, port, user, password = parts
        return f"{host}:{port}:{user}:***"
    return proxy_str

def request_faucet(wallet, proxy):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "requestAirdrop",
        "params": [wallet, 1000000000]  # 1 SOL = 1,000,000,000 lamports
    }

    try:
        response = requests.post(FAUCET_URL, json=payload, headers=headers, proxies=proxy, timeout=15)
        if response.status_code == 200 and "result" in response.json():
            print(f"✅ Airdrop thành công cho {wallet}")
        else:
            print(f"❌ Airdrop thất bại cho {wallet} - {response.text}")
    except Exception as e:
        safe_error = re.sub(r'(://[^:]+:).*(@)', r'\1***\2', str(e))
        print(f"⚠️ Lỗi proxy hoặc kết nối cho {wallet} - {safe_error}")
    time.sleep(random.uniform(*DELAY_BETWEEN_REQUESTS))

def run_batch(wallets_batch, proxy):
    threads = []
    for wallet in wallets_batch:
        t = threading.Thread(target=request_faucet, args=(wallet, proxy))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def main():
    try:
        wallets = read_lines("wallets.txt")
        proxies = read_lines("proxies.txt")
    except FileNotFoundError:
        print("Missing wallets.txt or proxies.txt")
        return

    while True:
        for proxy_str in proxies:
            masked = mask_proxy(proxy_str)
            print(f"\n🌐 Đang dùng proxy: {masked}")

            proxy_dict = get_proxy_dict(proxy_str)
            if proxy_dict is None:
                time.sleep(REQUEST_INTERVAL)
                continue

            wallet_index = 0
            while wallet_index < len(wallets):
                num_threads = random.randint(MIN_THREADS, MAX_THREADS)
                wallets_batch = wallets[wallet_index:wallet_index + num_threads]
                if not wallets_batch:
                    break
                run_batch(wallets_batch, proxy_dict)
                wallet_index += num_threads
                print(f"⏳ Chờ {REQUEST_INTERVAL} giây trước batch tiếp theo...")
                time.sleep(REQUEST_INTERVAL)

if __name__ == "__main__":
    main()
