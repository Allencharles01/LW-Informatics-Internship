Linux Task 6: Commands Behind Ctrl+C and Ctrl+Z Interrupts

Title: Understanding Ctrl+C and Ctrl+Z in Linux Terminal

Objective:
Investigate the process control and signals triggered when pressing Ctrl+C and Ctrl+Z in a Linux terminal.

1. Ctrl+C – SIGINT (Interrupt Signal):

What It Does:
- Immediately terminates the running foreground process.

Signal Sent:
- SIGINT (Signal Interrupt)

Equivalent Command:
    kill -SIGINT <PID>
    or
    kill -2 <PID>

Example Use Case:
- Running "ping google.com" and pressing Ctrl+C stops it by sending SIGINT.

2. Ctrl+Z – SIGTSTP (Terminal Stop Signal):

What It Does:
- Suspends the running process and moves it to the background.

Signal Sent:
- SIGTSTP (Signal Terminal Stop)

Equivalent Command:
    kill -SIGTSTP <PID>
    or
    kill -20 <PID>

Resume Options:
    fg  # bring back to foreground
    bg  # run in background

Check Signal List:
Use the following command to see all available signals:
    kill -l

Summary Table:

| Shortcut | Signal Name | Signal Number | Action         | Equivalent Command         |
|----------|-------------|----------------|----------------|----------------------------|
| Ctrl+C   | SIGINT      | 2              | Interrupt/Kill | kill -2 <PID>              |
| Ctrl+Z   | SIGTSTP     | 20             | Suspend        | kill -20 <PID>             |

Conclusion:
Ctrl+C and Ctrl+Z are keyboard shortcuts that map to specific signals (SIGINT and SIGTSTP) sent to running processes. These signals can be simulated using the `kill` command with appropriate signal numbers or names.
