from pathlib import Path
from wasmer import Instance
from däμbenscrypt.compiler import emitter

ext = "däμ"

def test_comments():
  wasm = emitter(Path("abc"))
  instance = Instance(wasm)
  
