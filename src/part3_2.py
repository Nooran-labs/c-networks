from scapy.all import rdpcap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np


# Load packet data from pcap
def load_pcap(file_path):
    packets = rdpcap(file_path)
    data = []
    for packet in packets:
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            src_port = packet.sport if packet.haslayer('TCP') or packet.haslayer('UDP') else 0
            dst_port = packet.dport if packet.haslayer('TCP') or packet.haslayer('UDP') else 0
            flow_id = hash((src_ip, dst_ip, src_port, dst_port))
            data.append({
                'Time': packet.time,
                'Size': len(packet),
                'Flow_ID': flow_id
            })
    return pd.DataFrame(data)


# Analyze packet flows
def analyze_flows(pcap_data, app_name):
    unique_flows = pcap_data['Flow_ID'].nunique()
    total_packets = len(pcap_data)
    total_bytes = pcap_data['Size'].sum()
    return {'App': app_name, 'Unique_Flows': unique_flows, 'Total_Packets': total_packets, 'Total_Bytes': total_bytes}


# Corrected combined plot according to instructions
def final_combined_plot(metrics_data, app_names, flow_metrics):
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))

    for data, app in zip(metrics_data, app_names):
        inter_arrival = data['Time'].diff().dropna()

        # Filter inter-arrival times to keep values only <= 0.1 seconds
        inter_arrival = inter_arrival[inter_arrival <= 0.1]

        sns.histplot(inter_arrival, bins=50, binrange=(0, 0.5), alpha=0.6, label=app, ax=axs[0, 0])

    axs[0, 0].set_title('Inter-Arrival Time Distribution (Limited to 0.5s)')
    axs[0, 0].set_xlabel('Inter-arrival Time (sec)')
    axs[0, 0].set_ylabel('Frequency')
    axs[0, 0].set_xlim(0, 0.1)  # Ensure x-axis only goes up to 0.1
    axs[0, 0].legend()

    # Packet Size Distribution (0-5000 bytes)
    for data, app in zip(metrics_data, app_names):
        sns.histplot(data['Size'], bins=50, binrange=(0, 5000), alpha=0.6, label=app, ax=axs[0, 1])
    axs[0, 1].set_title('Packet Size Distribution (0-5000 bytes)')
    axs[0, 1].set_xlabel('Packet Size (Bytes)')
    axs[0, 1].set_ylabel('Frequency')
    axs[0, 1].legend()

    # Flow Metrics (Bar plot for Flows, Packets, Bytes)
    x = np.arange(len(app_names))
    width = 0.25

    axs[1, 0].bar(x - width, [f['Unique_Flows'] for f in flow_metrics], width, label='Unique Flows')
    axs[1, 0].bar(x, [f['Total_Packets'] for f in flow_metrics], width, label='Total Packets')
    axs[1, 0].bar(x + width, [f['Total_Bytes'] for f in flow_metrics], width, label='Total Bytes')

    axs[1, 0].set_xticks(x)
    axs[1, 0].set_xticklabels(app_names)
    axs[1, 0].set_title('Flow Metrics Comparison')
    axs[1, 0].set_xlabel('Activity')
    axs[1, 0].set_ylabel('Count / Bytes')
    axs[1, 0].legend()

    fig.delaxes(axs[1, 1])  # Remove unused subplot
    plt.tight_layout()
    plt.show()


# User input and main execution
pcap_files = {}
for app in ['Web-surfing 1', 'Web-surfing 2', 'Audio streaming', 'Video streaming', 'Video conferencing']:
    path = input(f"Enter pcap path for {app}: ")
    pcap_files[app] = path

metrics_data = []
app_names = []
flow_metrics = []

for app, file_path in pcap_files.items():
    if os.path.exists(file_path):
        data = load_pcap(file_path)
        metrics_data.append(data)
        app_names.append(app)
        flow_metrics.append(analyze_flows(data, app))
    else:
        print(f"File {file_path} not found.")

# Display final combined plot correctly according to instructions
final_combined_plot(metrics_data, app_names, flow_metrics)

# Save results explicitly as required
results_df = pd.DataFrame(flow_metrics)
results_df.to_csv("results.csv", index = False)
print(results_df)
