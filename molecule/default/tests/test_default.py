import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


base_packages = [
  "apt-transport-https",
  "ca-certificates",
  "curl",
  "git",
  "vim",
  "htop",
  "sudo",
  "gnupg2",
  "python-pip",
  "python3-pip",
  "gcc",
  "make",
  "autoconf",
  "autoconf-archive",
  "autogen",
  "automake",
  "pkg-config",
  "lm-sensors",
  "dstat",
  "sysstat",
  "snmp",
  "mtr",
  "ncdu",
  "tcpdump",
  "atop",
  "python-dev",
  "net-tools",
  "locate",
  "man-db",
  "bash-completion",
  "dnsutils",
  "iftop"
]


def test_package_installation(host):
    for package in base_packages:
        package_status = host.package(package)
        assert package_status.is_installed
