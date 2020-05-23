import pytest
from pathlib import Path
from wasmer import Instance
from däμbenscrypt.compiler import emitter

ext = "däμ"

@pytest.mark.skip(reason="Currently emitter isn't taking any arguments")
def test_comments():
  wasm = emitter()
  instance = Instance(wasm)
  
