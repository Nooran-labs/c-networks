from scapy.all import rdpcap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Activities and data structure
activities = ['Browsing Session 1', 'Browsing Session 2', 'Music Streaming', 'HD Video Streaming', 'Conference Call']
dataframes = []


# Load PCAP data with enhanced structure
def extract_pcap_data(file_path, label):
    packets = rdpcap(file_path)
    extracted_data = [{
        'Timestamp': pkt.time,
        'PacketLength': len(pkt)
    } for pkt in packets if pkt.haslayer('IP')]

    df = pd.DataFrame(extracted_data)
    df['Timestamp'] -= df['Timestamp'].min()
    df['Activity'] = label
    return df


# Compute enhanced packet analysis metrics
def packet_analysis(df, label):
    throughput = df.groupby(df['Timestamp'].astype(int))['PacketLength'].sum()
    packet_rate = df.groupby(df['Timestamp'].astype(int)).size()
    inter_arrival = df['Timestamp'].diff().dropna()

    return {
        'Activity': label,
        'Throughput': throughput,
        'PacketRate': packet_rate,
        'InterArrival': inter_arrival,
        'FlowPackets': len(df),
        'FlowBytes': df['PacketLength'].sum()
    }


# Visualize clearly and distinctly from original code
def enhanced_visualizations(metrics):
    fig, axs = plt.subplots(3, 2, figsize=(16, 18))

    # Throughput Analysis
    for m in metrics:
        axs[0, 0].plot(m['Throughput'].index, m['Throughput'].values, label = m['Activity'])
    axs[0, 0].set_title('Throughput (Bytes/sec)')
    axs[0, 0].set_xlabel('Time (sec)')
    axs[0, 0].set_ylabel('Bytes')
    axs[0, 0].legend()

    # Packet Rate Analysis
    for m in metrics:
        axs[0, 1].plot(m['PacketRate'].index, m['PacketRate'].values, label = m['Activity'])
    axs[0, 1].set_title('Packet Rate (Packets/sec)')
    axs[0, 1].set_xlabel('Time (sec)')
    axs[0, 1].set_ylabel('Packets/sec')
    axs[0, 1].legend()

    # Inter-Arrival Times Comparison (line plot approach)
    for m in metrics:
        axs[1, 0].plot(m['InterArrival'].values, label = m['Activity'])
    axs[1, 0].set_title('Packet Inter-arrival Times Comparison')
    axs[1, 0].set_xlabel('Packets')
    axs[1, 0].set_ylabel('Inter-arrival Time (seconds)')
    axs[1, 0].legend()

    # Flow Packets Comparison
    flow_packets = [m['FlowPackets'] for m in metrics]
    activities_labels = [m['Activity'] for m in metrics]
    sns.barplot(x = activities_labels, y = flow_packets, ax = axs[1, 1])
    axs[1, 1].set_title('Flow Size Comparison')
    axs[1, 1].set_ylabel('Packets')

    # Flow Volume Comparison
    flow_bytes = [m['FlowBytes'] for m in metrics]
    sns.barplot(x = activities_labels, y = flow_bytes, ax = axs[2, 0])
    axs[2, 0].set_title('Flow Volume Comparison (Bytes)')
    axs[2, 0].set_ylabel('Bytes')

    fig.delaxes(axs[2, 1])  # Removing empty subplot
    plt.tight_layout()
    plt.show()


# Main execution logic
activity_metrics = []

for activity in activities:
    path = input(f"Enter path for '{activity}' pcap file: ")
    if os.path.isfile(path):
        df = extract_pcap_data(path, activity)
        dataframes.append(df)
        metrics = packet_analysis(df, activity)
        activity_metrics.append(metrics)
    else:
        print(f"File not found: {path}")

# Display all enhanced visualizations
if activity_metrics:
    enhanced_visualizations(activity_metrics)
else:
    print("No valid data available for analysis.")
