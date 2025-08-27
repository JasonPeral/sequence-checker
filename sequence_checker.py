import requests
from urllib.parse import urljoin

def fetch_playlist(url):
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.text.splitlines()

def get_variants(master_url):
    lines = fetch_playlist(master_url)
    variants = []
    for line in lines:
        if line and not line.startswith("#"):  # only URLs
            full_url = urljoin(master_url, line)
            variants.append(full_url)
    return variants

def get_media_sequence(url):
    lines = fetch_playlist(url)
    for line in lines:
        if line.startswith("#EXT-X-MEDIA-SEQUENCE"):
            return line.split(":")[1].strip()
    return "N/A"

def main():
    master_url = input("Paste the master playlist URL: ").strip()
    if not master_url:
        print("No URL provided, exiting.")
        return

    print(f"\nMaster playlist: {master_url}")
    variants = get_variants(master_url)

    print("\nChecking variants...")
    for v in variants:
        seq = get_media_sequence(v)
        print(f"{v}  ->  MEDIA-SEQUENCE: {seq}")

if __name__ == "__main__":
    main()
