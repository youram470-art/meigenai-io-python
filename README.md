# meigenai-io

Python metadata package for [meigenai.io](https://meigenai.io).

`meigenai-io` provides a small importable helper for scripts and automation that
need a stable reference to the Meigen AI website. It records the public site URL,
the local content path used by the website, and the Next.js app directory that
drives the page implementation.

## Installation

```bash
pip install meigenai-io
```

## Usage

```python
from meigenai_io import HOMEPAGE, get_site_info, hello

print(hello())
print(HOMEPAGE)
print(get_site_info())
```

## Site Metadata

- Website: https://meigenai.io
- Local repository: `/Users/mac/Documents/code/meigenai`
- Content path: `content`
- Next.js app path: `src/app`
- Source: https://github.com/youram470-art/meigenai-io-python

## License

MIT
