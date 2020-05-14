# däμbenscrypt

## Why?

Everyone is writing their own web languages, so why shouldn't I?

### YOU CANNOT JUST USE UNICODE IN THE NAME THAT'S GONNA CRASH XYZ

brrr....

### Philosophy

[>click <<here>><](https://www.destroyallsoftware.com/talks/wat)

## Installation

Prerequisite is that you have:

- [WebAssembly/wabt](https://github.com/webassembly/wabt); and
- Python

installed.


```bash
$ git clone git@github.com:TimDaub/<whatever this language is called by then>.git
$ cd <you'll figure it out>
$ chmod +x däμ
```

## Usage

Once you've completed the installation, you can use the compiler:

```bash
$ däμ specs/init.däμ
```

## References

- Docs:
  - [WebAssembly docs](https://developer.mozilla.org/en-US/docs/WebAssembly)
  - [YAML Spec](https://yaml.org/spec/)
  - [WebAssembly Specification](https://webassembly.github.io/spec/core/index.html)
- Tools:
  - [wabt](https://github.com/webassembly/wabt)
- Compilers:
  - [Building your own WASM compiler](https://blog.scottlogic.com/2019/05/17/webassembly-compiler.html)
    - [ColinEberhardt/chasm](https://github.com/ColinEberhardt/chasm)
