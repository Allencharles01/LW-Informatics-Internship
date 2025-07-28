Linux Task 3: Changing the Icon of a Linux Application

Title: Changing the Icon of a Linux Application

Objective:
To change the icon or logo of any installed Linux application by editing its .desktop launcher file.

Steps:

1. Locate the .desktop file:
   System-wide: /usr/share/applications/
   User-specific: ~/.local/share/applications/

2. Find the application file:
   Example:
       sudo nano /usr/share/applications/gedit.desktop

3. Edit the Icon line:
   Find the line:
       Icon=gedit
   Replace it with your custom icon path:
       Icon=/home/yourname/Pictures/new-gedit-icon.png

4. Save and Exit:
   Press Ctrl + O to save and Ctrl + X to exit the editor.

5. Optional: Update the desktop database:
       sudo update-desktop-database

6. Restart your system or log out/in to see the changes.

Notes:
- Recommended icon format: .png or .svg (128x128 or 256x256 preferred)
- For user-specific changes, copy the .desktop file to ~/.local/share/applications/ and edit there.
- Some desktop environments may cache icons; a reboot helps to refresh changes.

Why Learn This?
- Personalize your Linux desktop environment
- Practice software branding and packaging
- Enhance usability with custom visuals

Conclusion:
Customizing app icons in Linux is easy and powerful. With just a few steps, you can give your desktop a personal touch or prepare branded software for deployment.
