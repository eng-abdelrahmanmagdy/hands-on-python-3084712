import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

intrupution = f"{current_env} environment"
if current_env == DEVELOPMENT:
    print(intrupution)
elif current_env == PRODUCTION:
    print(intrupution)
elif current_env == STAGING:
    print(intrupution)
elif current_env in [CODE_SPACE, LOCAL]:
    print(intrupution)
else:
    print(intrupution)
