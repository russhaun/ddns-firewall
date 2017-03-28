# About ddns-firewall

Need to create firewall rules for hosts which do not have static IP addresses? This program allows you to do so if you're able to assign DDNSes to each of those hosts. This is how the program operates:
- At each time interval defined by you (e.g. 1 hourly), it will:
    1. Read your list of whitelisted hosts and ports
    2. Resolve those whitelisted hostnames to IP addresses
    3. Add those whitelisted IP addresses and ports to Windows Firewall
    4. Remove the outdated rules
    
That's it! It's a bit hack-ish but unfortunately I could not find anything better for free at this moment.

## Build

1. Make sure you have Python 2.7 and [py2exe](http://www.py2exe.org/) installed.
2. In the project root folder, execute `python setup.py`.
3. Distribute `dist\main.exe`.

## Usage

1. Make sure you have the necessary [runtime DDLs](https://www.microsoft.com/en-us/download/details.aspx?id=29).
2. Create `whitelist.txt` containing a list of whitelisted hosts/IP addresses and ports. For example:
    ```
    google.com 9999
    192.168.1.1 3000
    ```
3. Run `main.exe` as Administrator.
4. Add `main.exe` to startup, if necessary.
5. Enable Windows Firewall.
