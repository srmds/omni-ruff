import sys
import shutil
import subprocess
from pathlib import Path

def main():
    repo_root = Path(subprocess.run("REPO_ROOT=$(git rev-parse --show-toplevel) && echo $REPO_ROOT",shell=True, capture_output=True).stdout.decode('utf-8').rstrip())
    hook_root = Path(Path.cwd())
    source_conf = hook_root / "hooks" / "ruff.toml"
    dest_conf = repo_root / "ruff.toml"
    
    print(f"REPO ROOT: {repo_root}")
    print(f"HOOK ROOT: {source_conf}")

    # copy the contents of the demo.py file to  a new file called demo1.py
    shutil.copyfile(str(source_conf), str(dest_conf))


if __name__ == '__main__':
    try:
         main()
    except Exception as e:
        print(e)
        sys.exit(1)
        
    sys.exit(0)
