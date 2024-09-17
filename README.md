# Remote Network Bandwidth Monitor

Welcome to the **Network Bandwidth Monitor**! This application allows you to monitor real-time network bandwidth usage on a remote machine via SSH, using a beautiful graphical interface powered by Tkinter and Matplotlib.

## Features

- **Real-time Bandwidth Monitoring**: Tracks both incoming and outgoing network bandwidth in real-time.
- **Visual Graph**: Displays bandwidth data dynamically using Matplotlib for clear visualization.
- **Data Rate Calculations**: Automatically calculates the bandwidth rate in bits per second.
- **Remote SSH Monitoring**: Connects to any remote machine via SSH to retrieve network statistics (compatible with Windows).
- **Responsive UI**: Utilizes Tkinter for a sleek and responsive graphical user interface.
- **Live Updates**: The graph updates every 500 milliseconds to ensure live data representation.
  
## Technologies Used

- **Python**: Core programming language.
- **Paramiko**: For establishing SSH connections to remote machines.
- **Tkinter**: For creating the graphical user interface.
- **Matplotlib**: For dynamic graph plotting and real-time data visualization.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Paramiko (`pip install paramiko`)
- Matplotlib (`pip install matplotlib`)
- Tkinter (usually included with Python installations)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/itsadhil/Remote-bandwidth-monitor-with-Paramiko.git
   cd Remote-bandwidth-monitor-with-Paramiko

2. **Install the required Python dependencies:**
   ```bash
   pip install paramiko matplotlib

3. **For Linux Users**
   ```bash
   sudo apt-get install python3-tk

4. **If you're running on Windows, make sure to install the following additional dependencies:**
   ```bash
   pip install pywin32

## SSH Setup

If you are monitoring a Windows machine, follow these steps to install OpenSSH Server:

1. **Open PowerShell as Administrator and run the following command to install the OpenSSH Server:**
   ```bash
   Add-WindowsCapability -Online -Name OpenSSH.Server

2. **Start the OpenSSH Server:**
   ```bash
   Start-Service sshd

3. **Ensure the SSH service starts automatically on boot:**
   ```bash
   Set-Service -Name sshd -StartupType 'Automatic'

  For Linux or macOS, OpenSSH Server is usually pre-installed. If not, use the following command to install it:

1. **Ubuntu/Debian:**
    ```bash
    sudo apt update
    sudo apt install openssh-server

2. **CentOS/RedHat:**
   ```bash
   sudo yum install openssh-server

## Test SSH Connection

Before running the Network Bandwidth Monitor, ensure the remote machine has OpenSSH Server installed, and verify SSH connection works properly.

- Open a terminal (Linux/macOS) or PowerShell (Windows) on the local machine.
- Run the following command to initiate a test SSH connection to the remote machine:
  ```bash
  ssh username@remote_host
Replace username with your SSH username and remote_host with the IP address or hostname of the remote machine.
- On first connection, you will be prompted to accept the SSH fingerprint. Type yes to continue.
- Enter the password when prompted, and verify that the SSH connection is successful.
  Once the connection is successful and the fingerprint is stored, the Network Bandwidth Monitor will be able to connect without further fingerprint prompts.

## Usage
- Run the Python script:
- Enter the IP address, username, and password for the remote machine.
- The real-time bandwidth graph will be displayed in the Tkinter window, showing both incoming and outgoing bandwidth rates.
- The bandwidth rates will refresh every 500 milliseconds.

## Troubleshooting
- Authentication failed: Double-check the SSH username and password for the remote machine. Ensure OpenSSH Server is running on the remote machine.
- SSHException: This could be due to a network issue or improper SSH setup. Test your SSH connection with ssh username@remote_host and resolve any errors.
- No data displayed: Ensure the remote machine supports the Get-NetAdapterStatistics PowerShell command.
- Make sure you're on a Local Account rather than a Microsoft Account on your windows for SSH to work

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.
Contact me on discord through @hayayaquazi



