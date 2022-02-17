import hashlib
from pathlib import Path
from urllib.parse import urlparse

def write(filename: str, data: str):
    with open(filename, mode='w+', encoding='utf-8') as f:
        f.write(data)

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def hashit(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def is_file_present(f: str) -> bool:
    p = Path(f)
    return p.is_file()

