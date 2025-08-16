#!/usr/bin/env python3
import time
from datetime import datetime

try:
    timestamp = time.time()
    print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
    now = datetime.now()
    print(now.strftime("%b %d %Y"))
except Exception as e:
    print(f"Unexpected error: {e}")
