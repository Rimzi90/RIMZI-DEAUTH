import json
import subprocess
import time
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def install_requirements():
    print("🔍 Checking for required packages...")
    try:
        subprocess.run(['pkg', 'install', 'termux-api', '-y'], check=True)
        print("✅ termux-api installed successfully")
    except:
        print("⚠️ Could not install termux-api. Please install manually from F-Droid")
        print("Run: pkg install termux-api")

def scan_wifi():
    print("\n📡 Scanning for Wi-Fi networks...")
    try:
        result = subprocess.run(['termux-wifi-scaninfo'], 
                                capture_output=True, 
                                text=True,
                                timeout=30)
        
        if result.returncode != 0:
            print("❌ Error: Could not scan Wi-Fi networks")
            print("Make sure you have Termux:API installed from F-Droid")
            print("Enable Location Services and Wi-Fi on your device")
            return []
        
        networks = json.loads(result.stdout)
        return networks
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return []

def display_networks(networks):
    if not networks:
        print("No networks found. Try again in a different location.")
        return
    
    print("\n" + "="*60)
    print(f"📶 Found {len(networks)} Wi-Fi Networks".center(60))
    print("="*60)
    print("\n{:<30} {:<20} {:<8} {:<10}".format(
        "Network Name", "MAC Address", "Signal", "Channel"))
    print("-"*60)
    
    for network in networks:
        ssid = network.get('ssid', 'Hidden Network')[:28]
        bssid = network.get('bssid', 'Unknown')
        signal = network.get('rssi', 0)
        frequency = network.get('frequency', 0)
        
        # Convert frequency to channel
        channel = "2.4G" if frequency < 3000 else "5G"
        
        # Create signal strength indicator
        bars = "▮" * max(1, min(5, (signal + 100) // 20))
        
        print("{:<30} {:<20} {:<3}dBm {:<5} {}".format(
            ssid, 
            bssid, 
            signal,
            channel,
            bars))

def main():
    clear_screen()
    print("🔐 Wi-Fi Scanner for Non-Rooted Android")
    print("=======================================")
    print("⚠️ Note: This tool is for educational purposes only")
    print("      Requires Termux and Termux:API from F-Droid")
    print("      Enable Location Services for best results\n")
    
    # Check for termux-api
    if not os.path.exists('/data/data/com.termux/files/usr/bin/termux-wifi-scaninfo'):
        print("❌ termux-wifi-scaninfo not found!")
        install_requirements()
        return
    
    while True:
        networks = scan_wifi()
        display_networks(networks)
        
        print("\nOptions:")
        print("1. Rescan networks")
        print("2. Exit")
        
        choice = input("\nSelect option: ")
        if choice == '2':
            break
            
        clear_screen()

if __name__ == "__main__":
    main()
