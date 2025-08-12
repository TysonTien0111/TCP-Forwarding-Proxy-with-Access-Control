# TCP Forwarding Proxy with Access Control

A three-component network application (client, proxy, server) built from scratch in Python to demonstrate a deep understanding of low-level TCP/IP socket programming, network security, and protocol implementation. This project was completed as part of the Computer Networks curriculum at UC Davis.

## Key Features

*   **Mediated Communication:** All client-server traffic is routed through a central proxy, creating a single point of control and inspection.
*   **Stateful Security Policy:** The proxy parses JSON-serialized client data to enforce a network blocklist, rejecting connection attempts to predefined IP addresses.
*   **Reliable Data Transport:** Manages distinct, persistent TCP connections to ensure reliable, in-order message forwarding and response routing.
*   **Built from Scratch:** Implemented using only Python's standard `socket` and `json` libraries, without any high-level networking or packet construction APIs, to ensure a fundamental understanding of the underlying protocols.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/TysonTien0111/TCP-Forwarding-Proxy-with-Access-Control.git
    cd TCP-Forwarding-Proxy-with-Access-Control
    ```

2.  **Start the Server:**
    Open a terminal and run the server, which will listen for connections.
    ```bash
    python server.py
    ```

3.  **Start the Proxy:**
    Open a second terminal and run the proxy.
    ```bash
    python proxy.py
    ```

4.  **Run the Client:**
    Open a third terminal to run the client, which will send a request through the proxy to the server.
    ```bash
    python client.py
    ```

## Technologies Used

*   **Language:** Python
*   **Libraries:** `socket`, `json`
*   **Protocols:** TCP/IP
