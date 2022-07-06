from uuid import uuid4

def to_base_62(num):
  base62chars = list(str(c) for c in range(10))
  base62chars = base62chars + list(chr(c) for c in range(97, 123))
  base62chars = base62chars + list(chr(c) for c in range(65, 91))
  converted = ""
  while num // 62 != 0:
    remainder = num % 62
    converted += base62chars[remainder]
    num = num // 62
  converted += base62chars[num % 62]
  return converted[::-1]

def generate_id():
  return uuid4().int>>104