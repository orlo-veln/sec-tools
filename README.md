# Listen up, citizens. 
  Sec-tools is my first collection of foundational tools written to understand technical security.
  These tools were written with the assistance of Claude Opus 4.8. Anyone in my position (A damn relative novice at this) who says they aren't using some kind of LLM is probably lying to you.
  It is not my intention to be a 'vibe-coder' which is why I typed every line of this code by hand and went to extreme measures to ensure that I understood every aspect of every script. Ask me anything!!
  While learning the various aspects of networking and other aspects of security, I described and planned the tools, recieved instructions on the code and studied each aspect. In that way I managed the building of these tools, while inputting and understanding.

## The Infrastructure
I wanted to understand these tools in a real environment so I built a home security lab from scratch. I purchased a desktop server and a managed switch. On the server I installed a Type-1 Hypervisor with 3 x VMs. VM1: Linux Kali attack machine. VM2: Metasploitable. VM3: A 3B LLM to practice AI attack techniques. I isolated the Metasploitable and Kali machines on VLAN. Don't tell anyone.

## The Tools
### Lumos.py
I've always heard the word Python floating around. I've even joked about it in the comedy fiction books I've produced in the past. So, I wanted to learn to read and understand Python. After messing around with some crude beginner scripts, I wanted to create a tool that took a logfile and measured the current threat level based on the number of failed login attempts. I called this number 'The number of zombies knocking on the windows.' Claude helped me create this script which was absolutely exhilarating. While this is very basic, it was my first real Python script and hence I have a soft spot for it.
### Netcheck.sh
As a natural progression from lumos, I wanted a tool that checked the network in real time rather than relying on a log tool. It was almost like Lumos check last nights log files for zombies in the night while Netcheck.sh checks the local network for hosts and open ports.

### Sravnit.py
I'd been learning how to alter a log file directly to cover tracks. Being ruthlessly committed to defence, I wanted to create a script where we could compare two log files to check for deleted logs.

### Test Tools
test data and scripts that can be used to test the above tools.
