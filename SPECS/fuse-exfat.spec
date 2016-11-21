Name:           fuse-exfat
Summary:        Free exFAT file system implementation
Version:        1.2.4
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/fuse-exfat-%{version}.tar.gz
URL:            https://github.com/relan/exfat
BuildRequires:  fuse-devel

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT"
ln -s %{_mandir}/man8/mount.exfat-fuse.8.gz %{buildroot}%{_mandir}/man8/mount.exfat.8.gz

%files
%doc COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/*

%changelog
* Mon Sep 26 2016 Dario Cordova <dcordova@deskosproject.org> - 1.2.4-1
- Initial package for DeskOS.
