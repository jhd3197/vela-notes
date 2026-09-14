"""Build the app ZIP and SHA-256 file in dist/."""
import runpy
import sys
from pathlib import Path
sys.argv = [sys.argv[0], 'build']
runpy.run_path(str(Path(__file__).resolve().parent / 'scripts/automation.py'), run_name='__main__')
