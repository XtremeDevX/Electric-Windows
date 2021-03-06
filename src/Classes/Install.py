######################################################################
#                               INSTALL                              #
######################################################################
from Classes.Metadata import Metadata


class Install:
    """
    Stores data about an installation for usage
    """

    def __init__(self, json_name: str, display_name: str, path: str, install_switches, download_type: str, directory: str, custom_install_switch, install_exit_codes, uninstall_exit_codes, metadata: Metadata, version):
        self.display_name = display_name
        self.json_name = json_name
        self.path = path
        self.install_switches = install_switches
        self.download_type = download_type
        self.directory = directory
        self.custom_install_switch = custom_install_switch
        self.metadata = metadata
        self.install_exit_codes = install_exit_codes
        self.uninstall_exit_codes = uninstall_exit_codes
        self.version = version
