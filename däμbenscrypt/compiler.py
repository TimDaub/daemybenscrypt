import re
import itertools

keywords = ["say"]
matchers = [
  (r"^(?P<keyword>{})".format("|".join(keywords)), "keyword"),
  (r"(?P<string>\".*\")", "string")
]

def setup():
  head = [0x00, 0x61, 0x73, 0x6d]
  version = [0x01, 0x00, 0x00, 0x00]
  return bytes(head + version)

def run(path):
  emission = to_wasm(path)
  name = "{}.wasm".format(path.stem)
  write(name, emission)

def to_wasm(path):
  source = read(path)
  tokens = tokenizer(source)
  emission = emitter()
  return emission

def read(path):
  with open(path, 'r') as f:
    return f.read()

def tokenizer(source):
  tokens = list(itertools.chain(*[tinder(source, matcher)
            for matcher in matchers]))
  return tokens

def tinder(source, matcher):
  (pattern, token_type) = matcher
  res = re.compile(pattern, re.MULTILINE)
  return [
      {"type": token_type, "value": match.group(0), "span": match.span()}
    for match in re.finditer(res, source)
  ]

def emitter():
  # TODO: https://webassembly.github.io/spec/core/text/lexical.html#comments
  scrypt = setup()
  return scrypt

def write(name, scrypt):
  with open(name, 'wb') as out:
    print("Compiling successful")
