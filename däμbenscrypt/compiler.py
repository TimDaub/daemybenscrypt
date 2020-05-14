def setup():
  head = [0x00, 0x61, 0x73, 0x6d]
  version = [0x01, 0x00, 0x00, 0x00]
  return bytes(head + version)

def run(path):
  emission = emitter()
  name = "{}.wasm".format(path.stem)
  write(name, emission)

def emitter(path):
  # TODO: https://webassembly.github.io/spec/core/text/lexical.html#comments
  scrypt = setup()
  return scrypt

def write(name, scrypt):
  with open(name, 'wb') as out:
    print("Compiling successful")
