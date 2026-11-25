"""Write the funniest out-of-office auto-reply (one line, <=140 chars).

The joke is recursion: the auto-reply forwards your email to another
auto-reply, which is also out of office — nobody is ever coming back.
"""

import os

TEXT = "Out of office until Monday. Your email has been forwarded to my out-of-office reply, which is also out of office."

# Entry rule: exactly one line, at most 140 characters (bounty cap).
assert "\n" not in TEXT and len(TEXT) <= 140, f"entry violates rules: {len(TEXT)} chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")

print(TEXT)
