import subprocess

def get_device_info():
    info = {}
    info["OS Version"] = subprocess.getoutput("adb shell getprop ro.build.version.release")
    info["Device Model"] = subprocess.getoutput("adb shell getprop ro.product.model")
    info["Available Memory"] = subprocess.getoutput("adb shell cat /proc/meminfo | grep MemAvailable")
    return info
