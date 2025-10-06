# WiFi Jammer LOL

check out the cli script to skip the lib installation ---> ![here](https://github.com/mtm-x/wifijammer-script.git)

## Requirements

- Python 3.x
- PySide6 (optional)
- `aircrack-ng` suite


## Installation

Download the bin from the releases and run it with sudo. or 


1. Clone the repository:
    ```sh
    git clone https://github.com/mtm-x/wifijammer.git
    cd wifijammer
    ```


2. Ensure you have `aircrack-ng` installed:
    ```sh
    sudo apt-get install aircrack-ng
    ```
    or
    ```sh
    sudo pacman -S aircrack-ng
    ```
## Usage

Best way is to download the binary from the release and run 

    ```
    sudo -E ./Jammer_v1.0_x64_Linux.bin
    ```
    or wihtout -E arugument
    
Run the application with root privileges: ( need to install the requirements )

    
1. Install the required Python packages: 
    ```sh
    pip install -r requirements.txt
    ```
2.
   /home/lotus/qt_venv/bin/python ( this is your virt env path where u installed the requirements and make sure to  give the full path as given below )
    ```sh
    sudo -E /home/lotus/qt_venv/bin/python Jammer.py 
    ```
    or

    ```
    sudo -E python jammer.py
    ```

 
   
## Screenshot

![Screenshot_20250117_144919](https://github.com/user-attachments/assets/a5684559-7260-49b6-a48b-6daaecff2c51)
