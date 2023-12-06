# Internet Speed Test Utility v8.0
from speedtest import Speedtest

def run_speed_test():
    st = Speedtest()

    print("Running speed test...")

    # Perform the speed test
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping  # Latency in milliseconds
    server_info = st.results.server  # Server information

    # Display speed test results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

    # Display server information without the word "Server"
    print(f"Host: {server_info['host']}")
    print(f"Country: {server_info['country']}")
    print(f"Sponsor: {server_info['sponsor']}")

    print("Speed test complete.")

if __name__ == "__main__":
   run_speed_test()