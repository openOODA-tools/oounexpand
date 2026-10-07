Name:           oounexpand
Version:        0.1.0
Release:        1%{?dist}
Summary:        Converts consecutive spaces into tabs to save storage and match standard conventions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oounexpand
Source0:        oounexpand-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oounexpand is a sovereign, capability-bounded SPACE COMPACTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oounexpand
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oounexpand-uninstall

%files
/usr/bin/oounexpand
/usr/bin/oounexpand-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
