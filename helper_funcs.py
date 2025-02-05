import platform
import config
def check_os():
    """ Check OS type.

    Args: None

    Returns:
        str: Windows, macOS, or Linux.
    """
    os_name = platform.system()
    if os_name == 'Darwin':
        os_name = 'macOS'
    return os_name

def main_selector():
    try:
        if check_os() == 'Windows':
            return config.main_loc_windows
        elif check_os() == 'macOS':
            return config.main_loc_mac
    except:
        "OS type either Linux or not found"