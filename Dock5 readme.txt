**Task:** Run graphical software inside a Docker container
**Goal:** Display GUI applications (like `xclock`) from inside Docker on a Windows host

---

### 🛠️ Steps Performed:

1. **Launch Ubuntu Container**

   ```bash
   docker run -it --name ubuntu-gui ubuntu bash
   ```

2. **Update and Install GUI Tools**
   Inside the container:

   ```bash
   apt update  
   apt install x11-apps -y
   ```

3. **Enable Display Forwarding**
   From PowerShell (host terminal):

   ```powershell
   set-variable -name DISPLAY -value host.docker.internal:0.0
   ```

4. **Run GUI Application**
   Inside the container:

   ```bash
   xclock
   ```

---

### ✅ Outcome:

* `xclock` displayed a live analog clock window on your Windows machine.
* GUI applications now launch from Docker containers using X11 forwarding.

---

### 📝 Notes:

* Requires **X server running on Windows** (e.g., [VcXsrv](https://sourceforge.net/projects/vcxsrv/) or [Xming](https://sourceforge.net/projects/xming/)).
* Ensure firewall allows access to port `6000` (default X11 port).
* Environment variable `DISPLAY=host.docker.internal:0.0` bridges the Docker container to Windows X server.
