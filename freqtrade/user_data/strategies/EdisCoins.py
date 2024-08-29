
import sys
import os
import platform

# Add the parent directory of 'strategies' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Determine the correct runtime to import
system = platform.system().lower()
machine = platform.machine().lower()
if system == 'darwin' and machine == 'arm64':
    runtime_arch = 'darwin_aarch64'
else:
    runtime_arch = f'{system}_{machine}'

# Import the Pyarmor runtime
pyarmor_runtime_path = os.path.join(os.path.dirname(__file__), 'pyarmor_runtime_006349', runtime_arch)
sys.path.insert(0, pyarmor_runtime_path)

# Import the obfuscated strategy
from strategies import EdisCoins_obf

class EdisCoins(EdisCoins_obf.EdisCoins):
    def __init__(self, config: dict):
        super().__init__(config)
