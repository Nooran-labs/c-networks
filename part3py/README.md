# Network Traffic Analysis Project

##  Overview
This project analyzes network traffic using **pcap files**, extracting key metrics such as:
- **Throughput (Bytes/sec)**
- **Packets per Second (PPS)**
- **Packet Inter-Arrival Time**
- **Flow Size and Volume**

The project consists of two parts:
1. **Sections 1, 2, and 3** (`part3_1.py`): Processes multiple network activities and visualizes traffic metrics.
2. **Section 4** (`part3_2.py`): Provides an advanced comparative analysis.

---

##  **Project Structure**
```
NetworkProj/
│
├── README.md                # Project documentation (this file)
├── requirements.txt          # Dependencies for running the project
│
├── src/                      # Source code directory
│   ├── part3_1.py              # Sections 1, 2, and 3 analysis script
│   ├── part3_2.py      # Section 4 analysis script
│
├── res/                      # Results (CSV, figures)
│   ├── results.csv
│
└── data/                     # PCAP files directory (Not uploaded to GitHub)
    ├── chanNews.pcap
    ├── ynetcap.pcap
    ├── spotifycap1.pcap
    ├── streamcap.pcap
    ├── zoomcap.pcap
```

---

##  **Installation & Setup (Linux)**
###  **1. Install Python Dependencies**
Run the following command:
```bash
pip3 install -r requirements.txt
```

---

##  **Running the Project**
###  **1. Running Sections 1, 2, and 3 Analysis**
```bash
cd src/
python3 part3_1.py
```
When prompted, enter the correct `.pcap` file paths, for example:
```
Enter path for 'Browsing Session 1' pcap file: ../data/YourBrowsingSession.pcap
Enter path for 'Browsing Session 2' pcap file: ../data/YourSecondBrowsingSession.pcap
Enter path for 'Music Streaming' pcap file: ../data/YourMusicStreamingfile.pcap
Enter path for 'HD Video Streaming' pcap file: ../data/YourVideoStreaminfile.pcap
Enter path for 'Conference Call' pcap file: ../data/YourConferenceCallfile.pcap
```

###  **2. Running Section 4 Analysis**
```bash
cd src/
python3 part3_2.py
```
Similarly, enter file paths when prompted.

---

##  **Expected Output**
- The project will generate **comparative graphs** showing network traffic analysis.
- A results file `attack_analysis_results.csv` will be stored in the `res/` directory.

---

##  **Notes**
- **Do NOT upload `.pcap` files to GitHub.** If necessary, store them in a separate cloud storage and provide a link.
- **Ensure your project runs on Linux.**
- **If any issues occur, restart the terminal and check file paths explicitly.**

---

###  **Project Successfully Set Up!**
```
 Now you are ready to analyze network traffic!
```
