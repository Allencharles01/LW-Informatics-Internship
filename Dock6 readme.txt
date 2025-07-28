Docker Task 6: Audio Output in Docker on Windows

---

#### ✅ **Objective**

Enable audio playback from a Linux-based Docker container on a Windows host using PulseAudio.

---

### 🧰 **Requirements**

* Windows 10/11 (Host)
* Docker Desktop (Installed ✅)
* PulseAudio for Windows (v5 - Installed ✅)
* Any test audio-capable app (`ffplay`, `aplay`, etc.)

---

### 🔧 **Step-by-Step Instructions**

---

#### 🟩 1. **Install PulseAudio for Windows**

* Download the **full installer** from:
  [https://github.com/pgaskin/pulseaudio-win32/releases](https://github.com/pgaskin/pulseaudio-win32/releases)

* Install with all options enabled:

  * [x] PulseAudio
  * [x] System service
  * [x] Uninstaller

---

#### 🛠️ 2. **Edit PulseAudio Config**

**File path:**

```
C:\Program Files (x86)\PulseAudio\etc\pulse\default.pa
```

**Modify this section:**

```bash
# Disable the UNIX socket module (not supported on Windows)
# load-module module-native-protocol-unix

# Enable TCP support so Docker can talk to it
load-module module-native-protocol-tcp auth-anonymous=1
```

**At the bottom of the file**, also add:

```bash
exit-idle-time = -1
```

💾 Save and close.

---

#### 🔄 3. **Start PulseAudio**

Via PowerShell:

```powershell
& "C:\Program Files (x86)\PulseAudio\bin\pulseaudio.exe"
```

---

#### 🔍 4. **Verify PulseAudio is Listening**

Run:

```powershell
netstat -an | findstr 4713
```

Expected output:

```
TCP    0.0.0.0:4713           LISTENING
```

---

#### 🐳 5. **Run Docker Container with Audio Enabled**

Replace `192.168.0.201` with your actual local IP from `ipconfig`.

```powershell
docker run -it --rm `
  -e PULSE_SERVER=tcp:192.168.0.201 `
  ubuntu bash
```

---

#### 🎧 6. **Install Audio Tools in Container**

Inside the container:

```bash
apt update
apt install pulseaudio alsa-utils ffmpeg -y
```

---

#### 🔊 7. **Test Audio**

```bash
ffplay -f lavfi -i "sine=frequency=1000:duration=5"
```

or

```bash
aplay /usr/share/sounds/alsa/Front_Center.wav
```

---

### ✅ Task Complete!

You now have audio working inside Docker using PulseAudio over TCP. Combine this with VcXsrv for full GUI + audio support.
