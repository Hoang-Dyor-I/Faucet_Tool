import requests
import random
import time
import threading

FAUCET_URL = "https://api.devnet.solana.com"
MIN_THREADS = 20
MAX_THREADS = 25
REQUEST_INTERVAL = 10  # giây giữa các batch
DELAY_BETWEEN_REQUESTS = (1, 3)  # delay ngẫu nhiên mỗi request (giây)

def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

wallets = read_lines("wallets.txt")
proxies = read_lines("proxies.txt")

def get_proxy_dict(proxy_str):
    host, port, user, password = proxy_str.split(":")
    proxy_auth = f"{user}:{password}@{host}:{port}"
    return {
        "http": f"http://{proxy_auth}",
        "https": f"http://{proxy_auth}"
    }

def request_faucet(wallet, proxy_str):
    proxy = get_proxy_dict(proxy_str)
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
    except Exception:
        print(f"⚠️ Lỗi proxy hoặc kết nối cho {wallet}")
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
    while True:
        for proxy in proxies:
            proxy_parts = proxy.split(":")
            masked_proxy = f"{proxy_parts[0]}:{proxy_parts[1]}" if len(proxy_parts) >= 2 else proxy
            print(f"\n🌐 Đang dùng proxy: {masked_proxy}")
            wallet_index = 0
            while wallet_index < len(wallets):
                num_threads = random.randint(MIN_THREADS, MAX_THREADS)
                wallets_batch = wallets[wallet_index:wallet_index + num_threads]
                if not wallets_batch:
                    break
                run_batch(wallets_batch, proxy)
                wallet_index += num_threads
                print(f"⏳ Chờ {REQUEST_INTERVAL} giây trước batch tiếp theo...")
                time.sleep(REQUEST_INTERVAL)

if __name__ == "__main__":
    main()
