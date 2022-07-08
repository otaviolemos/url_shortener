from urlshortener import to_base62, generate_id
from urlredirector import from_base62

def test_simple_conversion():
  assert to_base62(10) == "a"

def test_more_complex_conversion():
  assert to_base62(11157) == "2TX"

def test_larger_id_conversion():
  assert to_base62(2009215674938) == "zn9edcu"

def test_uuid_generator():
  assert isinstance(generate_id(), int)

def test_from_base62():
  assert from_base62("zn9edcu") == 2009215674938

def test_simple_conversion_from_base62():
  assert from_base62("a") == 10
