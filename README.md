# ddns-firewall

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
