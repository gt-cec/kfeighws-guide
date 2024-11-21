# How to Use the `kfeighws` Machine

This year we got a fancy new computer! With a very fancy graphics card! The compute in that box will support pretty much everything our lab needs until the 2030's. At the time of writing, the ISYE department has named this computer `isye-kfeighws`.

Here is a reference guide for how to access and use this computer, assuming you know absolutely nothing.

## What is RHEL? What is Linux?

_TL;DR: RHEL is the Linux distribution that kfeighws runs, you should know some basic terminal commands._

RHEL is Red Hat Enterprise Linux. It is a Linux distribution based on Debian (you can look that up) and maintained by a company called Red Hat. Red Hat makes money by licensing RHEL to companies and giving support to help them set up and maintain their compute infrastructure, and as such RHEL is widely used by companies for servers. Georgia Tech is no exception.

The main way you will access `kfeighws` is through a terminal. A terminal is just a text-based file explorer. You can navigate through directories, open files, run commands, and do whatever you would normally do. In fact, most Linux desktop features are tightly coupled to the terminal -- the UIs just run terminal commands behind the scenes when you click buttons. I know a terminal looks scary, but it's nothing to be afraid of. Linux was made by generations of college students who have placed a lot of guardrails to make sure they (and you) do not mess up your computer, and that using Linux is very easy for you.

If you have used the terminal on Ubuntu or Mac, RHEL will be the exact same. Ubuntu is also Debian-based, and MacOS is built on BSD (BSD and Linux are both derivatives of UNIX). Windows is based on the entirely-different NT kernal, so there are relatively few transferrable terminal commands (although in recent years Powershell has added some equivalents).

If you have no experience with using the terminal, I would start by looking up a basic "How to use a terminal" tutorial, [like this one](https://www.freecodecamp.org/news/command-line-for-beginners/).

You will most likely use:
* `ssh` (access the machine from your computer)
* `cd` (change directory)
* `ls` (list files in a folder)
* `rm` (remove file/folder)
* `cp` (copy file/folder)
* `mv` (move file/folder)
* `pwd` (current folder)
* `cat` (output file contents)
* `git` (you better be using git by now!)
* `chmod` (making your shell scripts runnable)
* `nano` (or `vim`, for quickly editing files)
* `tmux` (making your terminal persistent, will cover this later)
* `curl` (downloading files from online)

The linked tutorial covers most of these programs. If you have no terminal experience, remember that `Ctrl-c` will exit programs, the up/down arrows let you navigate through your previous commands, `[tab]` will autocomplete, and `~` is an alias for your home directory `/home/jkolb`.

## How do I access `kfeighws`?

_TL;DR: SSH to `isye-kfeighws` if you are on the ISYE network (lab workstations), otherwise SSH to `castle.isye.gatech.edu` and then `isye-kfeighws`. For coding on `kfeighws`, Jack recommends remote access with VS Code._

The reason we are using Linux on this computer instead of Windows is so we can:

1. Have multiple projects running in parallel (like hosting two user study websites, or having two people training their RL models at once).
2. Host projects that are persistent (like running an LLM server for everyone to use, or a lab demo linked to the lab website).
3. Allow multiple people to use the graphics card at a time (instead of waiting for whoever is using it to log out).

Each of the above requires that multiple people are able to access the computer from their own workstations/devices. That's where SSH comes in.

SSH (Secure Shell) is a way to access a remote computer through your terminal. Virtually every computer comes with an SSH client. If you have used VNC or other remote desktop tools, SSH is the terminal equivalent. I will include the basic commands you will use to access `kfeighws`, however you can look up tutorials on how to use SSH further.

### Accessing the ISYE network through the jump server

The ISYE network uses a _jump server_ (named `castle`) to gatekeep the rest of the network. That means computers within the ISYE network can access each other, and everything outside the ISYE network must first access `castle`, and then the rest of the network. This process is very similar to using a VPN.

```
|Your computer| -- SSH --> |ISYE network (via castle.isye.gatech.edu or an ISYE workstation)| -- SSH --> |isye-kfeighws|
```

If you are using a lab workstation (ISYE computer), that computer is already on the ISYE network, so you can SSH into `isye-kfeighws` directly.

To access `castle` from a non-ISYE computer (your laptop), open a terminal and run:

`ssh YOUR_GT_USER@castle.isye.gatech.edu`

Easy right? You will be asked your GT password and do a two-factor authentication, and will now be in your user directory on `castle`. There's probably nothing there (try `ls`). If you want to, you can use the ISYE network for file storage -- everyone gets 5.5T of space.

### Accessing `kfeighws` from the ISYE network

Once you are on the ISYE network, you can SSH into `kfeighws`:

`ssh jkolb@isye-kfeighws`

Your username defaults to your current computer's username, so in most cases you can just do:

`ssh isye-kfeighws`

If you are already on the ISYE network you will not have to do two-factor authentication again.

Congratulations, you are now on the `kfeighws` machine! Practice all your terminal commands, make files, clone your `git` repositories, do whatever. Don't worry about messing anything up.

If you run out of storage space, send an email to `helpdesk@isye.gatech.edu` asking them to add you to the user group for `isye-kfeighws`.

When you are done, close the SSH session by running `exit`.

### Jack's Wisdom: Set up your hosts file

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

In VS Code, open a remote window (blue `><` button in the bottom left). Select `Connect Current Window to Host...`, then `+ Add New SSH Host...`. Enter your SSH command (`ssh isye-kfeighws` or the one-liner from the previous section). You will then be prompted to select where to save the new host configuration, I typically choose one that doesn't look like it requires administrator rights (so, in your user directory). VS Code will open that file and you can change the host name from VS Code's default if you want to (`isye-kfeighws`).

If you are extra and edited your hosts/config file, or once you have done the above once, simply select `Connect Current Window to Host...` and then select `kf` (or `isye-kfeighws` if you had VS Code create the host).

You can now use VS Code like normal. Personally, I find VS Code to be a really convenient way to access Git, move files/folders, copy files to the remote server, and do other general development. You can also open terminal instances within VS Code. Pretty much everyone at GT uses VS Code connected to remote compute.

### How do I display UI windows?

You may want to use UIs despite being remote (e.g., PyGame windows or showing OpenCV images). This is possible and done through "X-Forwarding". In short, X-Forwarding sends the low-level rendering commands to your computer via SSH, which your computer then uses to render the window. Your interactions with that window are sent back to the remote machine.

If you are on Windows or Mac, you need to run what's called an X11 server, which converts forwarded X instructions to instructions usable by your OS. The most popular X11 server for Windows is XMing, which I believe is in the GT software center. For Mac, install XQuartz. Some Linux distributions (like Ubuntu) are switching from X11 to Wayland, and may require a X11 server as well.

Once the X11 server is running, you can use the `-X` flag in your SSH command to enable X-Forwarding. On PuTTY, there is a checkbox: `Connection -> SSH -> X11 -> Enable X11 Forwarding`.

From the terminal you would connect with:

`ssh -X kf`

Note that some windows will not work, but most basic applications should be fine.

## How do I run a persistent process?

_TL;DR: Use tmux._

If you have a user study server, RL/DL model training, or some other big task, you probably do not want to have to keep your SSH session alive the whole time. Wouldn't it be nice if there was a way to keep your session alive even after your terminal disconnected?

Meet [tmux](https://github.com/tmux/tmux/wiki/Getting-Started) and [screen](https://astrobiomike.github.io/unix/screen-intro)!

`tmux` and `screen` are two widely-used programs for running terminal instances that are detached from an SSH session. This lets you SSH into `kfeighws`, start running something, close your terminal, and come back to it later. Perfect!

The two programs do effectively the same thing, and are both present on `kfeighws` (and virtually all Linux systems). The main difference is tmux has more features and is generally more intuitive to use, while screen is the original and is considered a complete program. I recommend tmux, but it's entirely your choice.

Here is a quick cheat sheet for tmux. You can SSH into `kfeighws` and try them step-by-step to create a new session, detach from it, re-attach to it, and end it.

* Create a new session:
`tmux new -s user-study-server`

* (from tmux session) Detach your terminal from a session:
`Ctrl-b d`

* List all sessions:
`tmux ls`

* Attach your terminal to a session (resume it):
`tmux attach -t user-study-server`

* (from tmux session) End/kill your current session:
`exit`

* (from base SSH session) End/kill a session:
`tmux kill-session -t user-study-server`

The detached terminals will last until the machine is turned off (literally years). Tmux and screen use a negligible amount of system resources, so feel free to have as many sessions active as you'd like. **While we try not to turn off `kfeighws`, do not assume that it will never be turned off**! Record checkpoints in your model training, log your server data, pipe terminal outputs to a file if you are reliant on them, and so on.

### Jack's Wisdom: Use tmux

Tmux might seem complex, but trust me, it is well worth the 3 minutes it takes to learn how to use it. Just follow the cheat sheet step-by-step and you will have the hang of it. Enjoy eternal peace. If you want to get fancy, you can split a tmux session into multiple terminals. Up to you, I usually only use the commands written in the cheat sheet.

## How do I make my webserver publicly-accessible?

_TL;DR: If you are the only one hosting, host on port 8080. Otherwise, have someone run the `server-relay.py` script to send your webservers traffic based on the traffic's route (e.g., `/onr-isr/log` traffic goes to the `onr-isr` server's `/log` route). Use the machine's IP address as the URL, traffic to the `https` port is converted to `http` by ISYE and forwarded to port `8080`._

The ISYE IT folks set up `kfeighws` to have a public https port forwarded to port `8080`. This is really cool! It allows us to run a public facing webserver (and any number of internal ones), so you can host your project on `kfeighws` and access it by visiting the machine's IP address.

To get the IP address, SSH into `kfeighws` and run `ifconfig`:

```
[jkolb@isye-kfeighws ~]$ ifconfig
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 190.201.92.80  netmask 255.255.255.0  broadcast 948.392.402.412
        inet6 fe80:91c:02dd:cea2:e394  prefixlen 64  scopeid 0x20<link>
        ether 09:3d:54:03:e4:94  txqueuelen 1000  (Ethernet)
        RX packets 83166  bytes 330840 (3.7 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 61248  bytes 554340 (5.6 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 19  memory 0x492810000-494282110
...
```

The `inet` property of the `eno1` interface is the public IP address, in this case, `190.201.92.80`. If you have a webserver listening on port `8080`, visiting `https://190.201.92.80` in your browser will access that webserver.

To test this out, you can use the super simple built-in netcat server:

`echo "Hiiii!!" | nc -l 8080`

When you visit `https://190.201.92.80`, you will see `Hiiii!!`. Netcat will then exit. You can run the command again if you want. If you are interested in running a webserver for your project, I once hosted an _Intro to Python Webservers_ workshop and the slides are [here](https://kolb.dev/flask).

To have multiple webservers running, either ask ISYE IT to open another http port (like 8081), or set up a main webserver to reroute requests by the page the user accesses (e.g., have `/onr-isr` route to one webserver listening on port 5000, and `/tmm-mas` route to another listening on port 5001). I recommend the later so there are fewer exceptions made to ISYE's firewall. Use [this Python script](https://github.com/gt-cec/kfeighws-tutorial/server-relay.py) to handle this forwarding, just have one person running it via tmux and edit/re-run the script as needed to add more servers. As a test example, if you run the script and visit `https://IP_ADDRESS/cec` you should see the CEC homepage.

## I don't have sudo access, how do I install things? I can't even use pip!

_TL;DR: Use Mamba (replacement to Conda) environments. I have yet to run into any issues with not having sudo while using Mamba._

Back in the day we used Docker (hard to use, bloated, slow), then we used Conda (easy to use, less bloated, slow), now we use Mamba (easy to use, thin, fast).

Mamba is a package manager that is the spiritual successor to Conda. It allows you to install packages locally so you don't need sudo access, and manages versions so you don't need to worry about conflicting packages. My most common need we have for Mamba is to use a more recent version of Python, as RHEL uses the (outdated) Python 3.9 as of this writing, and to install Python packages through `pip` (which usually requires sudo access). Virtually everything else you would want to install is available from the package repository `conda-forge`, which is entirely compatible with Mamba.

Install Micromamba from [here](https://mamba.readthedocs.io), it's a simple copy/paste terminal command that will not require sudo. For the work we do, we don't need the full Mamba. You may need to run `source ~/.bashrc` to start Mamba, you will see `(base)` at the start of your terminal when it is running.

You can look at the Mamba documentation for how to use Mamba, here is a quick cheat sheet:

* Create a new environment:
`micromamba create -n new_env -c conda-forge`
* Activate the new environment:
`micromamba activate new_env`
* Install some packages in new_env:
`micromamba install python=3.12`
* Install some Python libraries in new_env:
`pip install matplotlib numpy flask`
* Deactivate the current environment
`micromamba deactivate`

Just like that, you are able to install whatever you would like without worrying about version conflicts with other projects. Each environment is independent, however the packages are linked, so if you install the same `matplotlib` version in two environments it will only install it once on your system.

## Conclusion

That's all! Please update this guide as things change, and reach out if you have any questions about anything covered in the guide. We dropped a lot of money on this computer, so make the most of it :)
