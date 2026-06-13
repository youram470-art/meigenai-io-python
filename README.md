# meigenai-io

Python metadata and integration helper package for [meigenai.io](https://meigenai.io).

`meigenai-io` provides a small, importable Python layer for Meigen AI publishing, website metadata, and local content automation workflows. The
package is intentionally lightweight, but the published metadata is complete:
it exposes the production website URL, documentation URL, source repository,
local repository path, content path, and Next.js app path used by the site.

This package is useful as a stable integration point for scripts that generate
content, inspect website structure, publish MDX files, or attach site metadata
to automation output. It follows the same package-page pattern used by broader
SDK-style placeholder packages: clear installation instructions, concrete usage
examples, package metadata, and direct links back to the target website.

## Installation

Install from PyPI:

```bash
pip install meigenai-io
```

Upgrade to the latest published version:

```bash
pip install --upgrade meigenai-io
```

## Quick Start

```python
from meigenai_io import HOMEPAGE, hello, get_site_info

print(hello())
print(HOMEPAGE)
print(get_site_info())
```

Expected output includes the public website URL:

```text
https://meigenai.io
```

## Metadata API

The package exposes simple constants for direct imports:

```python
from meigenai_io import (
    HOMEPAGE,
    DOCUMENTATION,
    PACKAGE,
    REPOSITORY,
    LOCAL_REPOSITORY,
    CONTENT_PATH,
    APP_PATH,
)
```

You can also retrieve everything at once:

```python
from meigenai_io import get_site_info

site = get_site_info()

print(site["name"])
print(site["homepage"])
print(site["content_path"])
print(site["app_path"])
```

Returned metadata:

```python
{
    "name": "meigenai.io",
    "homepage": "https://meigenai.io",
    "documentation": "https://meigenai.io/docs",
    "package": "meigenai-io",
    "repository": "https://github.com/youram470-art/meigenai-io-python",
    "local_repository": "/Users/mac/Documents/code/meigenai",
    "content_path": "content",
    "app_path": "src/app",
}
```

## Automation Example

The metadata can be used in release scripts, blog generators, indexing tools, or
site maintenance commands:

```python
from pathlib import Path
from meigenai_io import get_site_info

site = get_site_info()
content_dir = Path(site["local_repository"]) / site["content_path"]
app_dir = Path(site["local_repository"]) / site["app_path"]

print(f"Website: {site['homepage']}")
print(f"Content directory: {content_dir}")
print(f"Next.js app directory: {app_dir}")
```

## Use Cases

- Keep a Python package name reserved for Meigen AI related tooling.
- Provide a clean PyPI page that points back to https://meigenai.io.
- Share website metadata across scripts without duplicating hard-coded paths.
- Support Meigen AI website automation, content indexing, and package metadata reuse.
- Help publishing tools locate `content` and `src/app` consistently.

## Project Layout

The related website project is organized around local content and Next.js app
routes:

```text
Local repository: /Users/mac/Documents/code/meigenai
Content path:     content
Next.js app path: src/app
```

Use it when a Python script needs to know where the Meigen AI content lives, which public URL should be attached to generated output, or which repository owns the package metadata.

## Links

- Website: https://meigenai.io
- Documentation: https://meigenai.io/docs
- Source: https://github.com/youram470-art/meigenai-io-python
- PyPI: https://pypi.org/project/meigenai-io/

## License

MIT
