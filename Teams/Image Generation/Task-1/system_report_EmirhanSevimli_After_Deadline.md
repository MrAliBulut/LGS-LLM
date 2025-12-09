# System Information Report
--
**File**: system_report_EmirhanSevimli.md
--

## Meta
- Author: Emirhan Sevimli
- Date: 29-11-2025 14:06 GMT+3
- Report Deadline: 28-11-2025 21:59 GMT+3

---

## Summary (Optional)
This is a MacBook Air equipped with the Apple M4 chip. The operating system is a developer build (26.0.1), and the system has 16GB of Unified Memory. The device is used for development, indicated by the presence of multiple CoreSimulator volumes.

---

## Hardware Information
- CPU: **Apple M4** Chip (8-Core CPU) — [Clock Speed Unknown]
- RAM: **16GB** LPDDR5X (Unified Memory)
- GPU: Apple Integrated **8-core GPU** (VRAM: 16GB shared Unified Memory)
- Disk: NVMe SSD (Internal, Physical disk0), **251.0 GB** Total Capacity, ~15 GB free space (based on df output)
- Network: Built-in Wi-Fi 6E (IP Address: **ANONYMIZED**)
- Motherboard: MacBook Air (M4) - Model Identifier: **[To be filled by the user if available, otherwise assume standard M4 Air]**

---

## Operating System & Software
- Operating System: macOS (Product Name: macOS)
- Kernel / Build: BuildVersion: **25A362** / Kernel Version: **25.0.0**
- Python versions & environments: Python environments not explicitly listed/installed.
- Docker / Container support: **Yes, Docker is installed** (Based on user input).
- ML/LLM libraries installed: PyTorch, TensorFlow, Apple MLX, etc., are **not installed**.
- CUDA Version: N/A (Apple Silicon)
- NVIDIA driver: N/A (Apple Silicon)

---

## Observations & Notes
- Known issues / warnings: The reported OS version, **ProductVersion: 26.0.1**, suggests a non-public/beta/developer release (likely macOS 15+). The command `zsh: command not found: free` indicates the `free` command is not available, which is normal for standard macOS installations; `df -h` provides disk usage, but memory usage typically requires `top` or `sysctl`.

---

## Command Outputs

> **Privacy & Clean-up Note:** The raw outputs below have been summarized and sanitized.

### macOS (bash) Summarized Output

* **OS Info (`sw_vers`)**: ProductName: macOS, ProductVersion: 26.0.1, BuildVersion: 25A362
* **Kernel Info (`uname -r`)**: 25.0.0
* **CPU Info (`sysctl -n machdep.cpu.brand_string`)**: Apple M4
* **RAM Info (`sysctl -n hw.memsize | awk ...`)**: 16 GB (Unified Memory)
* **GPU Info (`system_profiler SPDisplaysDataType`)**: Apple M4 Chipset, 8 Total Number of Cores, Metal Support: Metal 4, Display: Built-in Liquid Retina Display (2560 x 1664).
* **Disk Info (`diskutil list`)**: Internal Physical Disk (`disk0`) is **251.0 GB** in size. Main APFS Container (`disk3`) is 245.1 GB. Multiple APFS volumes for simulators are present (`disk5`, `disk7`, `disk9`).
* **Filesystem Free Space (`df -h`)**: Root volume (/) and Data volume (/System/Volumes/Data) have approximately **15 Gi** (Gigabytes) available.
```bash
# sw_vers & uname -r
ProductName:        macOS
ProductVersion:        26.0.1
BuildVersion:        25A362
25.0.0

# sysctl -n machdep.cpu.brand_string & sysctl -n hw.memsize
Apple M4
16 GB

# system_profiler SPDisplaysDataType (Summarized)
Graphics/Displays:
    Apple M4:
      Chipset Model: Apple M4
      Type: GPU
      Total Number of Cores: 8
      Metal Support: Metal 4
      Displays: Color LCD: Built-in Liquid Retina Display (2560 x 1664)

# diskutil list (Summarized - Internal Physical Disk)
/dev/disk0 (internal, physical):
   #:                     TYPE NAME                       SIZE          IDENTIFIER
   0:      GUID_partition_scheme                        *251.0 GB      disk0
   2:                Apple_APFS Container disk3           245.1 GB      disk0s2

# df -h (Relevant Volumes)
Filesystem     Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1  228Gi   16Gi    15Gi   51%    447k  158M   0%   /
/dev/disk3s5    228Gi  178Gi    15Gi   93%    2.3M  158M   1%   /System/Volumes/Data
