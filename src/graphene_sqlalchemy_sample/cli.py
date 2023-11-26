from __future__ import annotations

import argparse
import importlib
import pathlib


def get_mains() -> list[str]:
    return [
        elm.stem[len("main_") :]
        for elm in pathlib.Path(__file__).parent.glob("main/*.py")
        if elm.stem != "__init__"
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", choices=get_mains(), required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    module = importlib.import_module(f".main.main_{args.main}", package=__package__)
    module.main()
