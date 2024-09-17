# USE LOCAL ACCOUNT ON WINDOWS:
# DO NOT USE MICROSOFT ACCOUNT

import paramiko
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_bandwidth(remote_host, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        ssh.close()

        if error:
            print(f"Error: {error}")
            return None

        return output

    except paramiko.AuthenticationException:
        print("Authentication failed.")
        return None
    except paramiko.SSHException as e:
        print(f"SSHException: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def parse_statistics(stats):
    lines = stats.splitlines()
    received_bytes = 0
    sent_bytes = 0
    
    for line in lines:
        if line.strip() and not line.startswith('Name'):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    received_bytes = float(parts[-2].replace(',', ''))
                    sent_bytes = float(parts[-1].replace(',', ''))
                    return received_bytes, sent_bytes
                except ValueError:
                    print("Error parsing line:", line)
                    continue
    
    print("No valid statistics found.")
    return None, None

def fetch_bandwidth_data():
    remote_host = ' '  # Replace with the IP address of the Windows machine
    username = ' '     # Replace with the SSH username
    password = ' '    # Replace with the SSH password
    command = 'powershell -Command "Get-NetAdapterStatistics -Name \'*\' | Format-Table ReceivedBytes, SentBytes -HideTableHeaders"'

    stats = get_bandwidth(remote_host, username, password, command)
    if stats is None:
        return None, None

    return parse_statistics(stats)

def update_plot(frame):
    curr_in, curr_out = fetch_bandwidth_data()
    if curr_in is None or curr_out is None:
        print("Failed to fetch or parse data.")
        return

    # Calculate rates in bits per second
    in_rate = (curr_in - prev_in[0]) * 8  # bits per second
    out_rate = (curr_out - prev_out[0]) * 8  # bits per second

    # Update previous values
    prev_in[0] = curr_in
    prev_out[0] = curr_out

    # Append data for plotting
    current_time = time.time()
    times.append(current_time)
    in_rates.append(in_rate)
    out_rates.append(out_rate)

    # Maintain a fixed number of data points
    if len(times) > max_len:
        times.pop(0)
        in_rates.pop(0)
        out_rates.pop(0)

    # Update plot
    ax1.clear()
    ax1.plot(times, in_rates, label='Incoming Bandwidth (bits/s)')
    ax1.plot(times, out_rates, label='Outgoing Bandwidth (bits/s)')
    ax1.legend(loc='upper right')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Bandwidth (bits/s)')
    ax1.set_title('Network Bandwidth Monitoring')
    ax1.set_ylim(0, max(max(in_rates, default=0), max(out_rates, default=0)) * 1.1)  # Adjust y-axis limits

    # Update text display
    in_label.config(text=f"Incoming Bandwidth: {in_rate:.0f} bits/s")
    out_label.config(text=f"Outgoing Bandwidth: {out_rate:.0f} bits/s")

if __name__ == "__main__":
    # Initialize data lists
    times = []
    in_rates = []
    out_rates = []
    prev_in = [0]
    prev_out = [0]
    max_len = 60  # Number of points to display on the graph

    # Set up Tkinter window
    root = tk.Tk()
    root.title("Network Bandwidth Monitor")

    # Set up matplotlib figure and axis
    fig, ax1 = plt.subplots()
    ani = FuncAnimation(fig, update_plot, interval=500, cache_frame_data=False)  # Refresh every 500 milliseconds

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Add labels for incoming and outgoing bandwidth
    frame = ttk.Frame(root)
    frame.pack(side=tk.RIGHT, fill=tk.Y)

    in_label = ttk.Label(frame, text="Incoming Bandwidth: 0 bits/s")
    in_label.pack(padx=10, pady=5)

    out_label = ttk.Label(frame, text="Outgoing Bandwidth: 0 bits/s")
    out_label.pack(padx=10, pady=5)

    root.mainloop()