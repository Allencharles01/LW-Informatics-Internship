Linux Task 2: GUI Programs and Their Underlying Commands

Title: 5 GUI Programs in Linux & Their Underlying Commands

1. File Manager (Nautilus on GNOME)
GUI Use: Browsing files and folders.
Underlying Command:
    nautilus
Other Commands Used:
    - ls: listing directory contents
    - cp, mv, rm: for copying, moving, deleting files
    - xdg-open: open files with default apps

2. Terminal Emulator (GNOME Terminal / Konsole)
GUI Use: Access to command line in a graphical window.
Underlying Command:
    gnome-terminal
Other Commands Used:
    - bash, top, htop, ps, etc.

3. Software Center (Ubuntu Software)
GUI Use: Installing, removing, and updating software.
Underlying Commands:
    apt install <package-name>
    apt remove <package-name>
    apt update && apt upgrade

4. System Monitor (GNOME System Monitor / KSysGuard)
GUI Use: Monitor system resources and running processes.
Underlying Command:
    gnome-system-monitor
Other Commands Used:
    - top, ps aux, free, uptime, df -h

5. Gedit (Text Editor)
GUI Use: Editing plain text files.
Underlying Command:
    gedit
Other Commands Used:
    - File I/O like cat, echo, or direct file access

Summary Table:

| GUI Program         | Underlying Command(s)             |
|---------------------|-----------------------------------|
| Nautilus            | nautilus, ls, cp, rm              |
| GNOME Terminal      | gnome-terminal, bash              |
| Ubuntu Software     | apt install/remove/update         |
| GNOME System Monitor| gnome-system-monitor, top         |
| Gedit               | gedit, file I/O operations        |

Conclusion:
These GUI programs in Linux offer user-friendly interfaces but are powered by powerful underlying terminal commands. Knowing the commands gives better control and deeper understanding of system operations.
