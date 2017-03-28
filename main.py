from time import sleep
from socket import gethostbyname
from subprocess import check_output

LOG_FILE = 'logs.txt'
WHITELIST_FILE = 'whitelist.txt' # a list of whitelisted IP_ADDR/DDNS PORT - separated by whitespace on each line
UPDATE_INTERVAL = 12 * 60 * 60 # 12 HRLY
RULE_NAME_TEMPLATE = 'CUSTOM RULE 9834 %d-%d'

def get_rule_name(major_index, minor_index):
    return RULE_NAME_TEMPLATE % (major_index, minor_index)

def log(cmd, output):
    entry = "[LOG]: Command '%s' was executed with output '%s'\n\n" % (cmd, output)
    with open(LOG_FILE, 'a+') as f:
        f.write(entry)

def exec_cmd(cmd, should_log):
    output = check_output(cmd, shell=True)
    if should_log:
        log(cmd, output)
    return output

def exception_exists(major_index, minor_index):
    cmd = 'netsh advfirewall firewall show rule name="%s"' % get_rule_name(major_index, minor_index)
    output = exec_cmd(cmd, False)
    return 'No rules match the specified criteria.' not in output

def get_current_major_index():
    if exception_exists(0, 0):
        return 0
    return 1

def delete_exception(major_index, minor_index):
    cmd = 'netsh advfirewall firewall delete rule name="%s"' % get_rule_name(major_index, minor_index)
    exec_cmd(cmd, True)

def add_exception(exception, major_index, minor_index):
    ip_addr, port = exception
    rule_name = get_rule_name(major_index, minor_index)
    cmd = 'netsh advfirewall firewall add rule name="%s" dir=in action=allow remoteip=%s localport=%s' % (get_rule_name(major_index, minor_index), ip_addr, port)
    exec_cmd(cmd, True)

def clear_old_rules(major_index):
    for minor_index in range(5000):
        if exception_exists(major_index, minor_index):
            delete_exception(major_index, minor_index)
        else:
            return

def get_whitelist():
    with open(WHITELIST_FILE, 'r+') as f:
        return map(lambda line: line.split(), f.readlines())

def get_resolved_list(raw_exceptions):
        return map(lambda exception: (gethostbyname(exception[0]), exception[1]), raw_exceptions)

while True:
    # toggle between 0 and 1
    old_major_index = get_current_major_index()
    new_major_index = 1 - old_major_index

    # get and add updated exceptions
    raw_exceptions = get_whitelist()
    resolved_exceptions = get_resolved_list(raw_exceptions)
    for minor_index in range(len(resolved_exceptions)):
        add_exception(resolved_exceptions[i], new_major_index, minor_index)

    # clear outdated exceptions
    clear_old_rules(old_major_index)
    sleep(UPDATE_INTERVAL)
