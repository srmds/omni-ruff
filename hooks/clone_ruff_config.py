import os
import subprocess
import shutil
import sys
from pathlib import Path
# import argparse
import tempfile
import platform

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
    
    branch = "feature/ruff-config" # "master"  # or the specific branch where the file is located
    repo_url = f"https://{pat}@{org}.visualstudio.com/{project}/_git/{repo}"
     
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

    temp_dir: Path = Path("/tmp") if platform.system() == "Darwin" else Path(tempfile.gettempdir())
    temp_clone_dir: Path = temp_dir / repo
            
    try:
        # Ensure PAT is available
        if not pat:
            raise ValueError("PAT environment variable is not set")

        if temp_clone_dir.exists():
            # Repo is already cloned, pull latest changes, if any
            print("Ruff global repo locally exists, check for updates...")
            subprocess.call(["git", "pull"], cwd=str(temp_clone_dir))

        else:
            # Clone the repository using the PAT
            print("Ruff global repo does not locally exist, clone repo...") 
                      
            try:
                subprocess.run([
                    "git", "clone", "--branch", branch, repo_url, str(temp_clone_dir)
                ], check=True)
            except Exception as e:
                print(e)
            
        # Copy the TOML file to the desired location
        shutil.copyfile(f"{temp_clone_dir}/{config}", str(destination_ruff_config_path))

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
