import subprocess
import time

def start_emulator(avd_name):
    subprocess.Popen(["emulator", "-avd", avd_name])
    time.sleep(30)  # wait for boot; better use a device-ready check

def install_apk(apk_path):
    subprocess.run(["adb", "install", apk_path])
