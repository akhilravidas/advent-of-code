#!/usr/bin/env python
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
yr = 2023 if len(sys.argv) < 3 else sys.argv[2]
day = sys.argv[1] if len(sys.argv) > 1 else int(input("Day: "))


# Define the URL and headers for the request
url = f"https://adventofcode.com/{yr}/day/{day}/input"
headers = {
    "Cookie": f"session={os.environ['SESSION']}",
    "User-Agent": "src: https://github.com/akhilravidas/advent-of-code/blob/master/2023/download.py, reach me @ ar@mod0.ai",
}

response = requests.get(url, headers=headers, timeout=10)
if response.status_code == 200:
    output = response.text
    with open(f"{day}.in", "w") as f:
        f.write(output)
    print("\n".join(output.split("\n")[:10]))
else:
    print(f"Error: Received status code {response.status_code}")
