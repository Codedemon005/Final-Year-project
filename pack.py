import subprocess

required_packages = ['pandas', 'matplotlib']

for package in required_packages:
    try:
        # Check if package is already installed
        __import__(package)
        print(f'{package} is already installed.')
    except ImportError:
        print("Required packages Installing...")
        try:
            # Use pip to install the package
            subprocess.check_call(['pip', 'install', package])
            print(f'{package} installation successful.')
        except subprocess.CalledProcessError:
            print(f'Failed to install {package}.')