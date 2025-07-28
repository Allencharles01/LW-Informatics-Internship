Task: Run Docker **inside a Docker container** using the official `docker:dind` image.

---

### 🧰 **Requirements**

| Item                                | Status                       |
| ----------------------------------- | ---------------------------- |
| Docker Desktop                      | ✅ Installed and running     |
| Windows Terminal / PowerShell / CMD | ✅ Available                 |
| VS Code Terminal (PowerShell)       | ✅ Preferred for ease of use |

---

### 🟢 **Step-by-Step Instructions**

---

#### ✅ Step 1: Make sure Docker Desktop is running

> Look for the whale 🐳 icon in the system tray — it should say “Docker is running”.

---

#### ✅ Step 2: (Optional Clean-up) Remove any previous container

**Where:** PowerShell or CMD

```bash
docker rm dind-test
```

---

#### ✅ Step 3: Run the Docker-in-Docker container

**Where:** PowerShell or CMD

```bash
docker run --privileged --name dind-test -d docker:dind
```

> This starts the DIND container in the background.

---

#### ✅ Step 4: Enter the container shell

**Where:** PowerShell or CMD

```bash
docker exec -it dind-test sh
```

> Prompt will change to something like:
> `/ #` — now you're *inside the container*

---

#### ✅ Step 5: Run Docker inside Docker

**Where:** Inside the container (`/#` prompt)

```bash
docker version
docker info
docker run hello-world
```

> These confirm that Docker is running **inside** the container.

---

#### ✅ Step 6: Exit the container

**Where:** Inside the container

```bash
exit
```

---

### 📌 Notes

* `--privileged` is required to allow nested Docker daemon usage.
* Use `docker ps -a` to list containers if needed.
* If you get a name conflict, remove old container using:
  `docker rm dind-test`
* If the container exists but isn't running, start it:
  `docker start dind-test`

---

✅ **Task Complete!** You now have Docker running inside Docker.