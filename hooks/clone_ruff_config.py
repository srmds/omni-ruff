import os
import subprocess
import shutil
import sys
from pathlib import Path
import argparse

# $ export ORG=<VALUE> && \
# export PROJECT=<VALUE> && \
# export REPO=<VALUE> && \
# export PAT=<VALUE> 
def main(argv=None):
    
    try:
        # parser = argparse.ArgumentParser()
        # parser.add_argument("--config", type=str, default='pyproject.toml', help="The name of the global ruff config file, for example: ruff.toml")
        # args = parser.parse_args(argv)
        config = 'pyproject.toml' # args.config
        
        if config is None:
            raise Exception("Mandatory flag --config <path/to/ruff.toml> not set")
        
        print(f"config file: {config}")

    except Exception as e:
        print(e)
        sys.exit(1)
        
    try:
        pat = os.environ['PAT']
        org = os.environ["ORG"]
        project = os.environ["PROJECT"]
        repo = os.environ["REPO"]
    except KeyError as e:
        print(f"Mandatory environment variable: {e} is not set")
        sys.exit(1)
    
    branch = "master"  # or the specific branch where the file is located
    repo_url = f"https://{pat}@{org}.visualstudio.com/{project}/_git/{repo}"
    source_repo_path = Path(__file__).resolve().parent.parent / repo
    source_ruff_config_path = source_repo_path / config
     
    repo_root = Path(
            subprocess.run(
                "REPO_ROOT=$(git rev-parse --show-toplevel) && echo $REPO_ROOT",
                shell=True,
                capture_output=True,
            )
            .stdout.decode("utf-8")
            .rstrip()
        )
    destination_ruff_config_path = repo_root / "ruff.toml"

    try:
        # Ensure PAT is available
        if not pat:
            raise ValueError("PAT environment variable is not set")

        if source_repo_path.exists():
            # Repo is already cloned, pull latest changes, if any
            print("Ruff global repo locally exists, check for updates...")
            subprocess.call(["git", "pull"], cwd=str(source_repo_path))

        else:
            # Clone the repository using the PAT
            print("Ruff global repo does not locally exist, clone repo...")
            
            import tempfile
            import platform

            temp_dir = Path(f"/tmp/{repo}" if platform.system() == "Darwin" else tempfile.gettempdir())
            if Path(temp_dir).exists():
                Path(temp_dir).rmdir()
                
            Path(temp_dir).mkdir(exist_ok=True)
            
            try:
                res = subprocess.run([
                    "git", "clone", "--branch", branch, repo_url, f"{temp_dir}/{repo}"
                ], 
                    check=True,
                    shell=True,
                    capture_output=True
                ).stdout.decode("utf-8").rstrip()
            except Exception as e:
                print(e)
            
        
        # Copy the TOML file to the desired location
        shutil.copyfile(f"{temp_dir}/{config}", str(destination_ruff_config_path))

        # Clean up the temporary clone directory
        # shutil.rmtree(repo)
        print(f"Config file downloaded/updated successfully to {destination_ruff_config_path}")

    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error downloading config file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(e)
        sys.exit(1)
