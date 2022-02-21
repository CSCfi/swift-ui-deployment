#!/usr/bin/env python3


import secrets


def main():
    """."""
    pwd_sharing = secrets.token_hex(32)
    pwd_request = secrets.token_hex(32)
    pwd_postgres = secrets.token_hex(32)
    api_tokens = [f"{secrets.token_hex(64)}," for _ in range(0, 3)]

    pwd_redis = secrets.token_hex(32)
    print("Generating environment variables...")
    with open("envs.sh", "w") as envs:
        envs.write(
f"""\
SHARING_PASSWORD={pwd_sharing}
REQUEST_PASSWORD={pwd_request}
POSTGRES_PASSWORD={pwd_postgres}
SHARING_DB_HOST=database
SHARING_DB_PASSWORD={pwd_sharing}
REQUEST_DB_HOST=database
REQUEST_DB_PASSWORD={pwd_request}
OS_AUTH_URL="https://pouta.csc.fi:5001/v3"
BROWSER_START_SHARING_ENDPOINT_URL=http://192.168.200.22:9090
BROWSER_START_SHARING_INT_ENDPOINT_URL=http://sharing:9090
BROWSER_START_REQUEST_ENDPOINT_URL=http://192.168.200.22:9091
BROWSER_START_REQUEST_INT_ENDPOINT_URL=http://request:9091
BROWSER_START_RUNNER_ENDPOINT=http://download:9092
BROWSER_START_RUNNER_EXT_ENDPOINT=http://192.168.200.22:9092
SWIFT_UI_API_AUTH_TOKENS={"".join(api_tokens).rstrip(",")}
SWIFT_UI_SHARING_REQUEST_TOKEN={api_tokens[0].rstrip(",")}
SWIFT_UI_REDIS_HOST=dbredis
SWIFT_UI_REDIS_USER="swiftui"
SWIFT_UI_REDIS_PASSWORD={pwd_redis}
UPLOAD_RUNNER_LOG_LEVEL=10
LOG_LEVEL=DEBUG
BROWSER_DEBUG=1
""",
        )
    print("Generating redis configuration...")
    with open("redis.conf", "w") as redisconf:
        redisconf.write(
f"""\
user default off
user swiftui on +@all ~* &* >{pwd_redis}
""",
        )


if __name__ == "__main__":
    main()
