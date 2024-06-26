import sys
import shutil
import subprocess
from pathlib import Path


def main():
    try:
        repo_root = Path(
            subprocess.run(
                "REPO_ROOT=$(git rev-parse --show-toplevel) && echo $REPO_ROOT",
                shell=True,
                capture_output=True,
            )
            .stdout.decode("utf-8")
            .rstrip()
        )
        source_conf = Path(__file__).resolve().parent / "ruff.toml"
        dest_conf = repo_root / "ruff.toml"

        print(f"SOURCE PATH: {source_conf}")
        print(f"DEST PATH: {dest_conf}")

        # copy the contents of the demo.py file to  a new file called demo1.py
        shutil.copyfile(str(source_conf), str(dest_conf))
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
