HOMEPAGE = "https://meigenai.io"
DOCUMENTATION = "https://meigenai.io/docs"
PACKAGE = "meigenai-io"
REPOSITORY = "https://github.com/youram470-art/meigenai-io-python"
LOCAL_REPOSITORY = "/Users/mac/Documents/code/meigenai"
CONTENT_PATH = "content"
APP_PATH = "src/app"


def hello() -> str:
    return "hello from meigenai.io"


def get_site_info() -> dict:
    return {
        "name": "meigenai.io",
        "homepage": HOMEPAGE,
        "documentation": DOCUMENTATION,
        "package": PACKAGE,
        "repository": REPOSITORY,
        "local_repository": LOCAL_REPOSITORY,
        "content_path": CONTENT_PATH,
        "app_path": APP_PATH,
    }
