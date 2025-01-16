# WiFi Jammer LOL

## Requirements

- Python 3.x
- PySide6
- `aircrack-ng` suite


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mtm-x/wifijammer.git
    cd wifijammer
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have `aircrack-ng` installed:
    ```sh
    sudo apt-get install aircrack-ng
    ```
    or
    ```sh
    sudo pacman -S aircrack-ng
    ```
## Usage

1. Run the application with root privileges:
    ```sh
    sudo python jammer.py
    ```
    or

    ```
    sudo -E python jammer.py
    ```

