# How to Use the `kfeighws` Machine

This year we got a fancy new computer! With a very fancy graphics card! The compute in that box will support pretty much everything our lab needs until the 2030's. At the time of writing, the ISYE department has named this computer `isye-kfeighws`.

Here is a quick reference for how to access and use this computer, assuming you know absolutely nothing.

## What is RHEL? What is Linux?

_TL;DR: RHEL is the Linux distribution that kfeighws runs, you should know some basic terminal commands._

RHEL is Red Hat Enterprise Linux. It is a Linux distribution based on Debian (you can look that up) and developed by a company called Red Hat. Red Hat makes money by licensing RHEL to companies and giving support to help them set up and maintain their compute infrastructure, and as such RHEL is widely used by companies for servers. Georgia Tech is no exception.

The main way you will access `kfeighws` is through a terminal. A terminal is just a text-based file explorer. You can navigate through directories, open files, run commands, and do whatever you would normally do. In fact, most Linux desktop features are tightly coupled to the terminal -- they just run terminal commands behind the scenes when you click buttons. Terminal looks scary but it's nothing to be afraid of. Linux (and most terminal things) was made by college students who placed a lot of guardrails to make sure they (and you) do not mess up your computer.

If you have used the terminal on Ubuntu or Mac, RHEL will be the exact same. Ubuntu is also Debian-based, and MacOS is built on BSD (BSD and Linux are both derivatives of UNIX). Windows is based on the entirely-different NT kernal, so there are relatively few transferrable terminal commands (although in recent years Powershell has added some equivalents).

If you have no experience with using the terminal, I would start by looking up a basic "How to use a terminal" tutorial, [like this one](https://www.freecodecamp.org/news/command-line-for-beginners/).

You will most likely use: `ssh` (access the machine from your computer), `cd` (change directory), `ls` (list files in a folder), `rm` (remove file/folder), `cp` (copy file/folder), `mv` (move file/folder), `pwd` (current folder), `cat` (output file contents), `git` (you better know this), `chmod` (making your shell scripts runnable), and `nano` (or `vim`, for quickly editing files). The linked tutorial covers most all of these commands.

## How do I access `kfeighws`?

_TL;DR: SSH to `isye-kfeighws` if you are on the ISYE network (lab workstations), otherwise SSH to `castle.isye.gatech.edu` and then `isye-kfeighws. Jack highly recommends remote access with VS Code.`_

The reason we are using Linux on this computer instead of Windows is so we can:

1. Have multiple projects running in parallel (like hosting two user study websites, or having two people training their RL models at once).
2. Host projects that are persistent (like running an LLM server for everyone to use, or a lab demo linked to the lab website).
3. Allow multiple people to use the graphics card at a time (instead of waiting for whoever is using it to log out).

Each of the above requires that multiple people are able to access the computer from their own workstations/devices. That's where SSH comes in.

SSH (Secure Shell) is a way to access a remote computer through your terminal. Pretty much every PC comes with an SSH client. If you have used VNC or other remote desktop tools, SSH is the terminal equivalent. I will include the basic commands you will use to access `kfeighws`, however you can look up tutorials on how to use SSH further.

### Accessing the ISYE network through the jump server

The ISYE network uses a _jump server_ (`castle`) to gatekeep the rest of the network. That means everything within the ISYE network can access each other, and everything outside the ISYE network must first access `castle`, and then the rest of the network. This process is very similar to using a VPN.

If you are using a lab workstation (ISYE computer), that computer is already on the ISYE network, so you can skip this step.

To access `castle` from your own machine, open a terminal and run:

`ssh YOUR_GT_USER@castle.isye.gatech.edu`

Easy right? You will be asked your GT password and do a two-factor authentication, and will now be in your user directory on `castle`. There's probably nothing there (try `ls`). If you want to, you can use the ISYE network for file storage -- everyone gets 5.5T of space.

### Accessing `kfeighws` from the ISYE network

Once you are on the ISYE network, you can SSH into `kfeighws`:

`ssh jkolb@isye-kfeighws`

Your username defaults to your current computer's username, so in most cases you can just do:

`ssh isye-kfeighws`

If you are already on the ISYE network you will not have to do two-factor authentication again.

Congratulations, you are now on the `kfeighws` machine! Practice all your terminal commands, make files, do whatever, I would be very surprised if it was possible for you to mess anything up here.

If you run out of storage space, send an email to `helpdesk@isye.gatech.edu` asking them to add you to the user group for `isye-kfeighws`. 

### Jack's Wisdom

If you are using a lab workstation, install PuTTY through the software center and add a configuration for `isye-kfeighws`. It's the easiest way to SSH into the machine through Windows.

If you are using your own Windows computer (at home or laptop), `ssh` is available via Command Prompt.

Jump servers are standard practice, and accessing them is integrated into SSH. Instead of SSHing into the jump server and then SSHing into `kfeighws`, You can access `kfeighws` through one command:

`ssh -J jkolb6@castle.isye.gatech.edu jkolb6@isye-kfeighws`

If you want to be extra (always be extra), you can add a host alias to make it super easy to access `kfeighws`:

On Windows open `C:\Windows\System32\drivers\etc\hosts`, or on Linux/Mac open `~/.ssh/config`.

Add the following to the bottom, replacing my GT username with yours.
```
Host kf
    HostName isye-kfeighws
    User jkolb
    ProxyJump jkolb@castle.isye.gatech.edu
```

This adds an alias from `kf` to `isye-kfeighws`, specifies the username, and notes that `kf` requires jumping through `castle.isye.gatech.edu` first. Change the `kf` name if you would like.

After saving the hosts file, you can access `kfeigh-ws` using:

`ssh kf`

Beautiful.

### Accessing `kfeighws` through VS Code, PyCharm, or other editors

Most of us work through a text editor, and most text editors support remote access. VS Code is probably what you use (or, at least, _should_ use). VS Code uses the hosts file, if you did not edit that file (see Jack's Wisdom) then VS Code will do it automatically.

In VS Code, open a remote window (blue `><` button in the bottom left). Select `Connect Current Window to Host...`, then `+ Add New SSH Host...`. Enter your SSH command (`ssh isye-kfeighws` or the one-liner in Jack's Wisdom). You will then be prompted to select where to save the new host configuration, I typically choose one that doesn't look like it requires administrator rights (so, in your user directory). VS Code will open that file and you can change the host name from VS Code's default if you want to (`isye-kfeighws`).

If you are extra and edited your hosts/config file, or once you have done the above once, simply select `Connect Current Window to Host...` and then select `kf` (or `isye-kfeighws` if you had VS Code create the host).

You can then use VS Code like normal. Personally, I find VS Code to be a really convenient way to access Git, move files/folders, copy files to the remote server, and other generic commands. You can also open terminal instances within VS Code. Pretty much everyone at GT uses VS Code connected to remote compute.

### How do I display UI windows?

You may want to use UIs despite being remote (e.g., PyGame windows). This is possible (although it works so-so) and done through "X-Forwarding". In short, X-Forwarding sends the low-level render commands to your computer via SSH, which your computer then uses to render the window. Your interactions with that window are sent back to the remote machine, processed, and this cycle repeats.

If you are on Windows or Mac, you need to run what's called an X11 server, which converts forwarded X instructions to instructions usable by Windows. The most popular X11 server for Windows is XMing, which I believe is in the software center. For Mac, install XQuartz. Some Linux distributions (like Ubuntu) are switching from X11 to Wayland, and may require a X11 server as well.

Once the X11 server is running, you can use the `-X` flag in your SSH command to enable X-Forwarding. On PuTTY, there is a checkbox: `Connection -> SSH -> X11 -> Enable X11 Forwarding`.

`ssh -X kf`

Note that some windows will not work, but most should be fine.

## How do I run a persistent process?

