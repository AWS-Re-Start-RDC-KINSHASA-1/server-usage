# Server Monitoring API

This project is a RESTful API built with FastAPI that provides server monitoring capabilities. It allows users to retrieve real-time information about the CPU usage, disk usage, and memory usage of a server.

## Features

- Get CPU usage percentage
- Get disk usage information (total space, used space, free space, and percentage used)
- Get memory usage percentage

## Technologies Used

- Python
- FastAPI
- psutil (Python system and process utilities)

## Getting Started

### Prerequisites

- Python 3.10.11
- pip package manager

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/AWS-Re-Start-RDC-KINSHASA-1/server-usage.git
   
2. Install the dependencies:
   ```shell
   pip install -r requirements.txt
### Usage

1. Start the server:

   ```shell
   python3 main.py

2. Access the API at http://localhost:8000/monitoring to retrieve the server monitoring information.

### Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
