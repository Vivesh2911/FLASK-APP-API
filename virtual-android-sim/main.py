from utils.emulator_manager import start_emulator, install_apk
from utils.system_info import get_device_info

if __name__ == "__main__":
    avd_name = "Pixel_3a_API_30"  # Replace with your emulator name
    start_emulator(avd_name)

    print("Waiting for device to be ready...")
    install_apk("sample-app.apk")

    info = get_device_info()
    print("System Info:")
    print(info)
