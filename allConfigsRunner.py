import time, random, constants, subprocess, os
from pathlib import Path


def main():
    configs_path = Path("configs")
    config_files = sorted(configs_path.glob('*_config.py'))

    for config_file in config_files:
        print(f"Starting LinkedIn application with configuration: {config_file.name}")
        # Copy the current config file to config.py

        # subprocess.run(["cp", "-f", str(config_file), "config.py"], check=True)
        # Check if the operating system is Windows
        if os.name == 'nt':  # 'nt' indicates a Windows environment
            # Use the 'copy' command in Windows
            subprocess.run(["copy", str(config_file), "config.py"], shell=True, check=True)
        else:
            # Use the 'cp' command for Unix/Linux
            subprocess.run(["cp", "-f", str(config_file), "config.py"], check=True)


        # Run the LinkedIn Easy Apply bot
        # subprocess.run(["python3", "runner.py"], check=True)
        # Check if the operating system is Windows
        if os.name == 'nt':  # 'nt' indicates a Windows environment
            # Use 'python' for Windows
            subprocess.run(["python", "runner.py"], check=True)
        else:
            # Use 'python3' for Unix/Linux
            subprocess.run(["python3", "runner.py"], check=True)

        # Wait for a specified number of seconds or implement a random wait time
        sleep_time = random.uniform(constants.botSleepInBetweenSearchesBottom, constants.botSleepInBetweenSearchesTop)
        print(f"Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
