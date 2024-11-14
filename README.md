# TopoGuard (TopoG) - Real-Time Network Mapper and Alert Generator

**TopoGuard (TopoG)** is a real-time network mapping and alerting tool designed to visualize and monitor network topology changes in real time. By connecting to a designated node within a network, TopoG provides a graphical representation of the network's structure. It detects any device removals instantly and updates with new device additions within 3 minutes.

## Table of Contents
- [Key Features](#key-features)
- [How It Works](#how-it-works)
  - [Example](#example)
- [Installation](#installation)
- [Usage](#usage)
- [Performance](#performance)
- [Limitations](#limitations)
- [License](#license)

## Key Features
- **Real-Time Mapping**: Generates a real-time, graphical map of network topology using vertices (network devices) and edges (point-to-point connections).
- **Automated Network Discovery**: Uses Telnet/SSH to connect to devices and leverage CDP (Cisco Discovery Protocol) for neighbor discovery.
- **Efficient Exploration**: Implements a Breadth-First Search (BFS) approach to traverse and map the network.
- **Change Detection and Alerts**: Monitors and alerts on changes in the network, such as device removals (instant detection) and additions (detected within ~3 minutes).
- **Minimal Network Traffic**: Limits traffic by only establishing Telnet connections as required, keeping network load minimal.
- **Scalable Complexity**: Optimized for efficient traversal with an exploration complexity of \( O(n+v) \).

## How It Works
1. **Initial Connection**: Connect to the default gateway of the endpoint in the network.
2. **Neighbor Discovery**: Executes `show cdp neighbor` to gather details on neighboring devices.
3. **IP Retrieval**: Pings neighboring devices to retrieve IP addresses for connected interfaces.
4. **Recursive Mapping**: Connects to each router in turn, retrieves loopback addresses, and repeats the neighbor discovery process.
5. **Topology Visualization**: Builds a network topology graph with:
    - **Vertices** representing network devices (routers, switches).
    - **Edges** representing point-to-point connections between devices.

### Example
Consider two routers with the following configurations:
- **Router A**
  - Interface IP: 10.1.1.1/24
  - Loopback Address: 1.1.1.1
- **Router B**
  - Interface IP: 10.1.1.2/24
  - Loopback Address: 2.2.2.2

If connected to Router A (1.1.1.1), TopoG:
- Runs `show cdp neighbor`, identifying Router B (10.1.1.2).
- SSHs to Router B and confirms the link from 10.1.1.1 to 10.1.1.2.
- Extracts Router B's loopback address, 2.2.2.2.
- Continues the discovery process recursively to map additional devices.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/username/topoguard.git
    cd topoguard
    ```

2. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```
   
   TopoG primarily uses the following libraries:
   - `networkx` for graph processing
   - `matplotlib` for visualization
   - `Telnetlib` for Telnet connections

3. **Configure Network Access**:
   Ensure Telnet/SSH access to network devices and that CDP is enabled on all devices to be mapped.

## Usage

1. **Run TopoG**:
    ```bash
    python topoguard.py
    ```

2. **Visualize Topology**:
   The tool will output a graphical network map showing all devices and their interconnections.

3. **Monitor for Alerts**:
   TopoG continuously scans the network, providing alerts for any changes:
   - **Device Removal**: Detected immediately.
   - **Device Addition**: Detected within 3 minutes (CDP update interval).

## Performance

- **Complexity**: The BFS traversal for the network topology has a complexity of \( O(n+v) \), where \( n \) is the number of devices and \( v \) is the number of edges.
- **Network Load**: Generates minimal traffic by using Telnet only as necessary for device discovery.

## Limitations

- **CDP Dependency**: Limited to networks with CDP-enabled devices.
- **Device Addition Detection Delay**: New devices are detected based on the CDP update interval (~180 seconds).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
