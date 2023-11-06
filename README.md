# http_header_proxy

This acts like a proxy, but only returns the response header.
The body is NOT(!) returned.

If you are looking for a rust proxy implementation have a look at the hyper example:
[http_proxy.rs](https://github.com/hyperium/hyper/blob/master/examples/http_proxy.rs).

# Usage

```shell
export http_proxy=http://127.0.0.1:8100
curl -v https://www.github.com
```

# Build

Precondition:
rust is installed (recommended: [rustup](https://rustup.rs/))

```shell
cargo build
```

# Run

For the initial step you just can run it with

```shell
cargo run
```

# Installation 


