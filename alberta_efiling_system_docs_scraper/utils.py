import os
from pathlib import Path

from aws_cdk import aws_lambda as _lambda


def get_python_version():
    python_version_file = Path(__file__).parent.parent / ".python-version"
    with open(python_version_file, "r") as file:
        return file.read().strip()


def get_lambda_runtime():
    default_version = _lambda.Runtime.PYTHON_3_12

    version = get_python_version()
    major_version = version.split(".")[0]

    if major_version == "3" and len(version.split(".")) >= 2:
        minor_version = version.split(".")[1]
        return getattr(
            _lambda.Runtime,
            f"PYTHON_{major_version}_{minor_version}",
            default_version,
        )

    return default_version


def get_excluded_files(all_lambda_handlers, exclude_handlers):
    return list(set(all_lambda_handlers) - set(exclude_handlers))


def get_all_lambda_handlers(entry="lambda"):
    lambda_handlers_path = Path(__file__).parent.parent / entry
    return [f for f in os.listdir(lambda_handlers_path) if f.endswith(".py")]
