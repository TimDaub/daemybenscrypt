import os
from pathlib import Path
from wasmer import Instance
from däμbenscrypt.compiler import to_wasm, tokenizer

ext = "däμ"

def test_ingesting():
  path, _ = os.path.split(__file__)
  p = Path("{}/specs/say.{}".format(path, ext))
  wasm = to_wasm(p)
  instance = Instance(wasm)

def test_tokenizing():
  source =  """
say
say "hello"
say wisdom
say
say "hello world"
say "say"
popcorn
  """

  tokens = tokenizer(source)
  assert len(tokens) == 9
