import subprocess
import re

def scan_wifi():
    """Educational Wi-Fi scanner for non-rooted devices"""
    print("EDUCATIONAL WI-FI SCANNER")
    print("==========================")
    print("This tool demonstrates Wi-Fi scanning capabilities")
    print("on non-rooted devices. Actual network disruption")
    print("is illegal without explicit permission.\n")
    
    try:
        # Get available Wi-Fi networks using system commands
        result = subprocess.check_output(
            ['cmd', '/c', 'netsh wlan show networks mode=bssid'],
            text=True,
            stderr=subprocess.STDOUT
        )
        
        # Parse network information
        networks = []
        current_ssid = None
        
        for line in result.split('\n'):
            if "SSID" in line and "BSSID" not in line:
                current_ssid = line.split(':')[1].strip()
            elif "BSSID" in line and current_ssid:
                bssid = line.split(':')[1].strip()
                networks.append((current_ssid, bssid))
        
        # Display results
        print("Detected Networks (Educational Purposes Only):")
        for ssid, bssid in networks:
            print(f"• Network: {ssid}")
            print(f"  MAC Address: {bssid}")
            
        print("\nEducational Note:")
        print("Actual deauthentication attacks require:")
        print("- Special hardware (monitor mode support)")
        print("- Root access on mobile devices")
        print("- Legal authorization for testing")
        
    except Exception as e:
        print("Error occurred:", str(e))
        print("This functionality may not be available")
        print("on your device or operating system")

if __name__ == "__main__":
    scan_wifi()
