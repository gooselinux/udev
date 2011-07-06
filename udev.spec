%define debug true
%define udev_scriptdir /lib/udev
%define firmwaredir /lib/firmware

Summary: A userspace implementation of devfs
Name: udev
Version: 147
Release: 2.29%{?dist}
License: GPLv2
Group: System Environment/Base
Provides: udev-persistent = %{version}-%{release}
Obsoletes: udev-persistent < 0:030-5
Obsoletes: udev-extras < 20090618
Provides: udev-extras = 20090618-1
Source: ftp://ftp.kernel.org/pub/linux/utils/kernel/hotplug/%{name}-%{version}.tar.bz2

Patch1: 0001-cdrom_id-Still-check-profiles-even-if-there-is-no-me.patch
Patch2: 0002-cdrom_id-remove-deprecated-device-matches.patch
Patch3: 0003-cdrom_id-open-non-mounted-optical-media-with-O_EXCL.patch
Patch4: 0004-cdrom_id-remove-debugging-code.patch
Patch5: 0005-cdrom_id-retry-to-open-the-device-if-EBUSY.patch
Patch6: 0006-cdrom_id-check-mount-state-in-retry-loop.patch
Patch7: 0007-cdrom_id-always-set-ID_CDROM-regardless-if-we-can-ru.patch
Patch8: 0008-replace-add-change-with-remove.patch
Patch9: 0009-cdrom_id-Fix-uninitialized-variables.patch
Patch10: 0010-cdrom_id-Fix-uninitialized-buffers.patch

Patch101:  udev-141-cpu-online.patch
Patch102:  udev-147-modem-modeswitch.patch
Patch103:  udev-147-wwn.patch
Patch104:  udev-147-virtio.patch
Patch105:  udev-147-layer3.patch
Patch107:  udev-147-Decrease-buffer-size-when-advancing-past-NUL-byte.patch
Patch108:  udev-147-Use-UTIL_LINE_SIZE-not-UTIL_PATH_SIZE-to-truncate-pr.patch
Patch109:  udev-147-Increase-UTIL_LINE_SIZE-from-2048-to-16384.patch
Patch110:  udev-147-sas.patch
Patch111:  udev-147-selinux-preserve.patch
Patch112:  udev-147-xvd_cdrom.patch
Patch114:  udev-147-virtual.patch
Patch115:  udev-147-modprobe-hack.patch
Patch116:  udev-147-patch_id-sas.patch
Patch117:  udev-147-patch_id-sas2.patch
Patch118:  udev-147-no-usb_id-err.patch
Patch119:  udev-147-virtio-blk-patch_id.patch
Patch120:  udev-147-changer-symlink.patch
Patch121:  udev-147-virtio-blk-by-id.patch
Patch122:  udev-147-patch_id-sas3.patch
Patch123:  udev-147-rule_gen.patch

Patch200: udev.git-5539f624.patch
Patch201: udev.git-c4f6dcc4a5c774c4c5c60c7024d59081deecc7f8.patch
Patch202: udev.git-484e1b2d11b9b89418589d885a625e647881933b.patch
Patch203: udev.git-847b4f84c671e98f29f22d8e3e0d70a231d71a7b.patch
Patch204: udev.git-0c7377880974e6eadac7a3ae9e35d339546dde0d.patch
Patch205: udev-147-cdrom-virt.patch
Patch206: udev-147-scsi_id-raw.patch

Source1: start_udev
Source3: udev-post.init
Source4: fw_unit_symlinks.sh
Source5: udev.sysconfig

ExclusiveOS: Linux
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(pre): /bin/sh fileutils /sbin/chkconfig /sbin/service
Requires(pre): /usr/bin/stat /sbin/pidof
Requires(pre): MAKEDEV >= 0:3.11 /usr/bin/getent /usr/sbin/groupadd
Requires: hwdata

%ifarch s390 s390x
# Require s390utils-base, because it's essential on s390
Requires: s390utils-base
%endif

BuildRequires: sed libselinux-devel >= 0:1.17.9-2 flex libsepol-devel
BuildRequires: glib2-devel bison findutils MAKEDEV
BuildRequires: gperf libtool
BuildRequires: libusb-devel libacl-devel
BuildRequires: libxslt
BuildRequires: hwdata
BuildRequires: gtk-doc
BuildRequires: usbutils >= 0.82
BuildRequires: libtool >= 2.2.6
Requires: libselinux >= 0:1.17.9-2 sed 
Conflicts: kernel < 0:2.6 mkinitrd <= 0:4.1.11-1 initscripts < 7.84
Requires: util-linux-ng >= 2.15.1
Obsoletes: dev <= 0:3.12-1
Provides: dev = 0:3.12-2
Obsoletes: DeviceKit < 004
Obsoletes: DeviceKit-devel < 004
Provides: DeviceKit = 004 DeviceKit-devel = 004
# hid2hci moved to udev
Conflicts: bluez < 4.47

%description
The udev package contains an implementation of devfs in 
userspace using sysfs and netlink.

%package -n libudev
Summary: Dynamic library to access udev device information
Group: System Environment/Libraries
Obsoletes: libudev0 <= 142
Provides: libudev0 = 143
License: LGPLv2+

%description -n libudev
This package contains the dynamic library libudev, which provides access
to udev device information, and an interface to search devices in sysfs.

%package -n libudev-devel
Summary: Development files for libudev
Group: Development/Libraries
Requires: udev = %{version}-%{release}
Requires: libudev = %{version}-%{release}
License: LGPLv2+

%description -n libudev-devel
This package contains the development files for the library libudev, a
dynamic library, which provides access to udev device information.

%package -n libgudev1
Summary: Libraries for adding libudev support to applications that use glib
Group: Development/Libraries
Requires: libudev >= 142
# remove the following lines for libgudev so major 1 
Provides: libgudev = 20090518
Obsoletes: libgudev <= 20090517
License: LGPLv2+

%description -n libgudev1
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n libgudev1-devel
Summary: Header files for adding libudev support to applications that use glib
Group: Development/Libraries
Requires: libudev-devel >= 142
Provides: libgudev-devel = 20090518
Obsoletes: libgudev-devel <= 20090517
License: LGPLv2+

Requires: libgudev1 = %{version}-%{release}

%description -n libgudev1-devel
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%prep 
%setup -q  

%patch1 -p1 -b .git1
%patch2 -p1 -b .git2
%patch3 -p1 -b .git3
%patch4 -p1 -b .git4
%patch5 -p1 -b .git5
%patch6 -p1 -b .git6
%patch7 -p1 -b .git7
%patch8 -p1 -b .git8
%patch9 -p1 -b .git9
%patch10 -p1 -b .git10


%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1 
%patch119 -p1 
%patch120 -p1 
%patch121 -p1 
%patch122 -p1 

%patch200 -p1 
%patch201 -p1 
%patch202 -p1 
%patch203 -p1 
%patch204 -p1 
%patch205 -p1  -b .virt
%patch206 -p1  -b .raw

%patch123 -p1  -b .rg

%build
# get rid of rpath
libtoolize -f -c
%configure --with-selinux  --prefix=%{_prefix} --exec-prefix="" \
	   --sysconfdir=%{_sysconfdir} \
	   --sbindir="/sbin" --libexecdir=%{udev_scriptdir} \
	   --with-rootlibdir=/%{_lib} --disable-introspection \
	   --enable-debug

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sbindir}

make install DESTDIR=$RPM_BUILD_ROOT

rm -fr $RPM_BUILD_ROOT%{_docdir}/udev
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

# Deprecated, but keep the ownership
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/{rules.d,makedev.d,scripts,devices}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dev.d
mkdir -p $RPM_BUILD_ROOT%{_bindir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/scsi_id.config

# force relative symlinks
ln -sf ..%{udev_scriptdir}/scsi_id $RPM_BUILD_ROOT/sbin/scsi_id

for i in \
	rules/redhat/40-redhat.rules \
%ifarch ia64
	rules/packages/40-ia64.rules \
%endif
%ifarch ppc ppc64
	rules/packages/40-ppc.rules \
%endif
%ifarch s390 s390x
	rules/packages/40-s390.rules \
%endif
	rules/packages/40-isdn.rules \
	rules/packages/64-md-raid.rules \
	rules/packages/64-device-mapper.rules \
	; do
	install -m 0644 "$i"  "$RPM_BUILD_ROOT%{udev_scriptdir}/rules.d/${i##*/}"
done
	
mkdir -p $RPM_BUILD_ROOT%{udev_scriptdir}/{,devices}

install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{udev_scriptdir}/fw_unit_symlinks.sh

mkdir -p $RPM_BUILD_ROOT%{_datadir}/udev
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/sbin/start_udev

mkdir -p -m 0755 $RPM_BUILD_ROOT%{firmwaredir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/udev-post

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/udev

mkdir -p $RPM_BUILD_ROOT/var/lib/udev/makedev.d

%preun
if [ "$1" -eq 0 -a -f %{_initrddir}/udev ]; then
	if [ -x /sbin/pidof ]; then
		pid=$(/sbin/pidof -c udevd)
		if [ -n "$pid" ]; then
			kill $pid >/dev/null 2>&1 || :
		fi
	fi
	/sbin/chkconfig --del udev
fi
if [ "$1" -eq 0 ]; then
	/sbin/chkconfig --del udev-post
fi
exit 0

%pre
# to be removed after F10 EOL (and for RHEL-6)
getent group video >/dev/null || /usr/sbin/groupadd -g 39 video || :
getent group audio >/dev/null || /usr/sbin/groupadd -g 63 audio || :
# to be kept
getent group cdrom >/dev/null || /usr/sbin/groupadd -g 11 cdrom || :
getent group tape >/dev/null || /usr/sbin/groupadd -g 33 tape || :
getent group dialout >/dev/null || /usr/sbin/groupadd -g 18 dialout || :

# kill daemon if we are not in a chroot
if test -f /proc/1/exe -a -d /proc/1/root; then
	if test -x /usr/bin/stat -a "$(/usr/bin/stat -Lc '%%D-%%i' /)" = "$(/usr/bin/stat -Lc '%%D-%%i' /proc/1/root)"; then
		if test -x /sbin/udevd -a -x /sbin/pidof ; then
			/sbin/udevadm control --stop-exec-queue
			pid=$(/sbin/pidof -c udevd)
			while [ -n "$pid" ]; do
				for p in $pid; do
					kill $hard $p >/dev/null 2>&1 || :
				done
				pid=$(/sbin/pidof -c udevd)
				hard="-9"
			done
		fi
	fi
fi
exit 0

%post
# start daemon if we are not in a chroot
if test -f /proc/1/exe -a -d /proc/1/root; then
	if test "$(/usr/bin/stat -Lc '%%D-%%i' /)" = "$(/usr/bin/stat -Lc '%%D-%%i' /proc/1/root)"; then
		/sbin/udevd -d
		/sbin/udevadm control --start-exec-queue
	fi
fi
/sbin/chkconfig --add udev-post

exit 0

%triggerin -- selinux-policy
rm -f /var/lib/udev/makenode.d/*  >/dev/null 2>&1 || :

%triggerin -- MAKEDEV
rm -f /var/lib/udev/makenode.d/*  >/dev/null 2>&1 || :

%post -n libudev -p /sbin/ldconfig
%postun -n libudev -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc NEWS COPYING README TODO ChangeLog docs/* extras/keymap/README.keymap.txt
%attr(0755,root,root) /sbin/udevadm
%attr(0755,root,root) /sbin/udevd
%attr(0755,root,root) /sbin/start_udev
%attr(0755,root,root) /sbin/scsi_id
%attr(0755,root,root) %{udev_scriptdir}/scsi_id
%attr(0755,root,root) %{udev_scriptdir}/ata_id
%attr(0755,root,root) %{udev_scriptdir}/edd_id
%attr(0755,root,root) %{udev_scriptdir}/usb_id
%attr(0755,root,root) %{udev_scriptdir}/cdrom_id
%attr(0755,root,root) %{udev_scriptdir}/path_id
%attr(0755,root,root) %{udev_scriptdir}/hid2hci
%attr(0755,root,root) %{udev_scriptdir}/create_floppy_devices
%attr(0755,root,root) %{udev_scriptdir}/fw_unit_symlinks.sh
%attr(0755,root,root) %{udev_scriptdir}/firmware.sh
%attr(0644,root,root) %{udev_scriptdir}/rule_generator.functions
%attr(0755,root,root) %{udev_scriptdir}/write_cd_rules
%attr(0755,root,root) %{udev_scriptdir}/write_net_rules
%attr(0755,root,root) %{udev_scriptdir}/collect
%attr(0755,root,root) %{udev_scriptdir}/fstab_import

%attr(0755,root,root) %dir %{udev_scriptdir}/rules.d/
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/udev-post
%attr(0755,root,root) %dir %{_sysconfdir}/udev/
%attr(0755,root,root) %dir %{_sysconfdir}/udev/rules.d/
%attr(0755,root,root) %dir %{udev_scriptdir}/
%attr(0755,root,root) %dir %{udev_scriptdir}/devices/
%attr(0755,root,root) %dir %{_sysconfdir}/udev/makedev.d/

%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/udev

%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/udev/udev.conf
%attr(0644,root,root) %{udev_scriptdir}/rules.d/*.rules

%ghost %config(noreplace,missingok) %attr(0644,root,root) %{_sysconfdir}/scsi_id.config

%dir %attr(0755,root,root) %{firmwaredir}
%attr(0644,root,root) %{_mandir}/man8/udev*.8*
%attr(0644,root,root) %{_mandir}/man7/udev*.7*
%attr(0644,root,root) %{_mandir}/man8/scsi_id*.8*

%dir %attr(0755,root,root) /var/lib/udev
%dir %attr(0755,root,root) /var/lib/udev/makedev.d

# Deprecated, but keep the ownership
%ghost %dir %{_sysconfdir}/udev/scripts/
%ghost %dir %{_sysconfdir}/udev/devices/
%ghost %dir %{_sysconfdir}/dev.d/

%attr(0755,root,root) %{udev_scriptdir}/modem-modeswitch
%attr(0755,root,root) %{udev_scriptdir}/pci-db
%attr(0755,root,root) %{udev_scriptdir}/usb-db
%attr(0755,root,root) %{udev_scriptdir}/keymap
%attr(0755,root,root) %{udev_scriptdir}/udev-acl
%attr(0755,root,root) %{udev_scriptdir}/v4l_id
%attr(0755,root,root) %{udev_scriptdir}/findkeyboards
%dir %attr(0755,root,root) %{udev_scriptdir}/keymaps
%attr(0644,root,root) %{udev_scriptdir}/keymaps/*
%attr(0644,root,root) %{_prefix}/lib/ConsoleKit/run-seat.d/udev-acl.ck


%files -n libudev
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) /%{_lib}/libudev.so.*

%files -n libudev-devel
%defattr(0644, root, root, 0755)
%doc COPYING
%{_includedir}/libudev.h
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libudev.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/gtk-doc/html/libudev/*

%files -n libgudev1
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) %{_libdir}/libgudev-1.0.so.*

%files -n libgudev1-devel
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) %{_libdir}/libgudev-1.0.so
%attr(0644,root,root) %{_includedir}/gudev-1.0/gudev/*.h
%dir %attr(0755,root,root) %{_includedir}/gudev-1.0
%dir %attr(0755,root,root) %{_includedir}/gudev-1.0/gudev
%dir %{_datadir}/gtk-doc/html/gudev
%attr(0644,root,root) %{_datadir}/gtk-doc/html/gudev/*
%attr(0644,root,root) %{_libdir}/pkgconfig/gudev-1.0*

%changelog
* Tue Aug 31 2010 Harald Hoyer <harald@redhat.com> 147-2.29
- set the selinux context for "add" events, regression
  the fix for rhbz#575128 caused a lot of selinux errors like
  rhbz#603729
Resolves: rhbz#575128

* Tue Aug 31 2010 Harald Hoyer <harald@redhat.com> 147-2.28
- quirk for cisco virtual cdrom was not complete, reports
  blank media, rhbz#628962
Resolves: rhbz#624707

* Tue Aug 24 2010 Harald Hoyer <harald@redhat.com> 147-2.27
- added ID_SERIAL_RAW to scsi_id export output, which is not
  whitespace stripped
Resolves: rhbz#612173

* Wed Aug 18 2010 Harald Hoyer <harald@redhat.com> 147-2.26
- more quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#624707

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.25
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.24
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.23
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Fri Jul 23 2010 Harald Hoyer <harald@redhat.com> 147-2.22
- fixed random MAC address handling 
- honor ifcfg HWADDR settings for 70-persistent-net.rules
Resolves: rhbz#596464

* Mon Jul 12 2010 Harald Hoyer <harald@redhat.com> 147-2.21
- fix tape by-path symlinks
Resolves: rhbz#612064

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 147-2.20
- add by-id for virtio-blk devices
Resolves: rhbz#601248

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 147-2.19
- do not blkid blank or audio CDROMs 
Resolves: rhbz#606293
- fixed scsi changer symlink
Resolves: rhbz#603051
- suppress warnings from usb_id
Resolves: rhbz#585648
- add path_id for virtio-blk devices
Resolves: rhbz#601248
- fixed reference leak in path_id sas patch
Resolves: rhbz#537185

* Fri Jun 11 2010 Harald Hoyer <harald@redhat.com> 147-2.18
- removed obsolete arguments to configure
Resolves: rhbz#601882
- add IMPORT{db} IMPORT{cmdline} and set rd_NO_MDIMSM for noiswmd kernel cmdline option
Resolves: rhbz#589775
- add port for sas in path_id 
Resolves: rhbz#537185
- add modprobe hack to serialize modprobes
Resolves: rhbz#515413
- revert path check from 147-2.16
Resolves: rhbz#591970

* Tue Jun 08 2010 Harald Hoyer <harald@redhat.com> 147-2.17
- get path_id for virtual disks also
- Resolves: rhbz#601248

* Wed Jun 02 2010 Phil Knirsch <pknirsch@redhat.com> 147-2.16
- Added path checks for mdadm and blkid binaries in 64-md-raid.rules rules
- Resolves: rhbz#591970

* Mon Apr 26 2010 Harald Hoyer <harald@redhat.com> 147-2.15
- fix "do not mark xvd* devices as cdrom by default (rhbz#584163)"
  included patch but did not apply
- Resolves: rhbz#584163

* Thu Apr 22 2010 Harald Hoyer <harald@redhat.com> 147-2.14
- do not mark xvd* devices as cdrom by default (rhbz#584163)
- Do not rename network interfaces.
  This causes more problems, than solving the original one.
  (rhbz#565724)
- Resolves: rhbz#584163, rhbz#572681

* Thu Apr 15 2010 Harald Hoyer <harald@redhat.com> 147-2.13
- supress error message in pre/post while killing old udevd
  (rhbz#576819)
- fixed a lot of cdrom related problems (rhbz#582557, rhbz#582559)
- Resolves: rhbz#576819, rhbz#582557, rhbz#582559

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 147-2.12
- fixed virtio-ports rule patch (rhbz#569699)
- removed IFINDEX from renamed interfaces (rhbz#572681)
- do not reset selinux labels (rhbz#575128)
- Resolves: rhbz#572681, rhbz#569699, rhbz#575128

* Wed Mar 03 2010 Harald Hoyer <harald@redhat.com> 147-2.11
- add SCSI SAS handling to path_id (rhbz#537185)
- fixed handling of boxes with lots of disks and huge
  volume groups (rhbz#570016)
- fixed virtio-ports rule (rhbz#569699)
- Resolves: rhbz#537185, rhbz#569699, rhbz#570016

* Tue Feb 23 2010 Harald Hoyer <harald@redhat.com> 147-2.10
- add one more letter to renamed interfaces to avoid name 
  clashing (rhbz#565724)
- Resolves: rhbz#565724

* Mon Feb 22 2010 Harald Hoyer <harald@redhat.com> 147-2.9
- rename non-handled network interfaces, so that the handled
  can be renamed to their destination name (rhbz#565724)
- Resolves: rhbz#565724

* Mon Feb 22 2010 Harald Hoyer <harald@redhat.com> 147-2.8
- reverting patch for network interface renaming (rhbz#565724)
- Related: rhbz#565724

* Tue Feb 16 2010 Harald Hoyer <harald@redhat.com> 147-2.7
- fixed udev-post initscript retriggering (rhbz#566568)
- attempt to fix network interface renaming (rhbz#565724)
- Resolves: rhbz#565724, rhbz#566568

* Tue Feb 09 2010 Harald Hoyer <harald@redhat.com> 147-2.6
- ignore dev_id for all s390 network interfaces (rhbz#561017)
- Resolves: rhbz#561017

* Tue Feb 09 2010 Harald Hoyer <harald@redhat.com> 147-2.5
- ignore dev_id for layer3 s390 network interfaces (rhbz#561017)
- Resolves: rhbz#561017

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 147-2.4
- add symlink rule for virtio ports (rhbz#559180)
- fixed initscript
- create /dev/net/tun with 0666 in start_udev
- Export ID_WWN_VENDOR_EXTENSION and ID_WWN_WITH_EXTENSION
- Related: rhbz#543948 rhbz#515413
- Resolves: rhbz#559180

* Wed Jan 13 2010 Harald Hoyer <harald@redhat.com> 147-2.3
- rebuild with gobject-introspection (#553806)
- Resolves: rhbz#553806

* Fri Jan 08 2010 Harald Hoyer <harald@redhat.com> 147-2.2
- only require s390utils-base, rather than s390utils (#553156)
- removed non-working softlinks (partly fixes also #528883)
- Resolves: rhbz#553156

* Fri Dec 11 2009 Dennis Gregorovic <dgregor@redhat.com> - 147-2.1
- Rebuilt for RHEL 6

* Tue Nov 24 2009 Harald Hoyer <harald@redhat.com> 147-2
- require s390utils, because it's essential on s390

* Thu Nov 12 2009 Harald Hoyer <harald@redhat.com> 147-1
- version 147
- Fix upgrade from Fedora 11 with bluez installed (#533925)
- obsolete DeviceKit and DeviceKit-devel (#532961)
- fixed udev-post exit codes (#523976)
- own directory /lib/udev/keymaps (#521801)
- no more floppy modaliases (#514329)
- added one more modems to modem-modeswitch.rules (#515349)
- add NEWS file to the doc section
- automatically turn on hotplugged CPUs (rhbz#523127)
- recognize a devtmpfs on /dev (bug #528488)

* Fri Oct 09 2009 Harald Hoyer <harald@redhat.com> 147-0.1.gitdf3e07d
- pre 147 
- database format changed
- lots of potential buffer overflow fixes

* Tue Sep 29 2009 Harald Hoyer <harald@redhat.com> 145-10
- add ConsoleKit patch for ConsoleKit 0.4.1

* Fri Sep 25 2009 harald@redhat.com 145-9
- add patches to fix cdrom_id
- add patch to fix the inotify bug (bug #524752)

* Wed Sep 23 2009 harald@redhat.com 145-8
- obsolete libgudev and libgudev-devel (bug #523569)

* Mon Aug 24 2009 Karsten Hopp <karsten@redhat.com> 145-7
- drop ifnarch s390x for usbutils, as we now have usbutils for s390x

* Mon Aug 24 2009 Harald Hoyer <harald@redhat.com> 145-6
- ifnarch s390 for usbutils

* Tue Aug 04 2009 Harald Hoyer <harald@redhat.com> 145-5
- do not make extra nodes in parallel
- restorecon on /dev

* Tue Aug 04 2009 Harald Hoyer <harald@redhat.com> 145-4
- --enable-debug 
- add patch for timestamps in debugging output

* Wed Jul 29 2009 Harald Hoyer <harald@redhat.com> 145-3
- add patch from upstream git to fix bug #514086
- add version to usbutils build requirement

* Fri Jul 24 2009 Harald Hoyer <harald@redhat.com> 145-2
- fix file permissions
- remove rpath
- chkconfig --add for udev-post
- fix summaries
- add "Required-Stop" to udev-post

* Tue Jul 14 2009 Harald Hoyer <harald@redhat.com> 145-1
- version 145
- add "udevlog" kernel command line option to redirect the
  output of udevd to /dev/.udev/udev.log

* Fri Jul 03 2009 Harald Hoyer <harald@redhat.com> 143-2
- add acpi floppy modalias
- add retrigger of failed events in udev-post.init
- killall pids of udev in %%pre

* Fri Jun 19 2009 Harald Hoyer <harald@redhat.com> 143-1
- version 143

* Thu Jun 08 2009 Harald Hoyer <harald@redhat.com> 142-4
- git fix: udevadm: settle - fix timeout
- git fix: OWNER/GROUP: fix if logic
- git fix: rule-generator: cd - skip by-path links if we create by-id links
- git fix: fix possible endless loop for GOTO to non-existent LABEL
- git fix: cdrom_id: suppress ID_CDROM_MEDIA_STATE=blank for plain non-writable 
		CDROM media

* Thu Jun 08 2009 Harald Hoyer <harald@redhat.com> 142-3
- delay device-mapper changes

* Fri Jun 05 2009 Bastien Nocera <bnocera@redhat.com> 142-2
- Rebuild in dist-f12

* Fri May 15 2009 Harald Hoyer <harald@redhat.com> 142-1
- version 142
- no more libvolume_id and vol_id

* Fri Apr 17 2009 Harald Hoyer <harald@redhat.com> 141-3
- added /dev/fuse creation to start_udev

* Thu Apr 16 2009 Harald Hoyer <harald@redhat.com> 141-2
- fixed post and pre

* Tue Apr 14 2009 Harald Hoyer <harald@redhat.com> 141-1
- version 141

* Wed Apr 01 2009 Harald Hoyer <harald@redhat.com> 139-4
- double the IMPORT buffer (bug #488554)
- Resolves: rhbz#488554

* Wed Apr 01 2009 Harald Hoyer <harald@redhat.com> 139-3
- renamed modprobe /etc/modprobe.d/floppy-pnp to
  /etc/modprobe.d/floppy-pnp.conf (bug #492732 #488768)
- Resolves: rhbz#492732

* Tue Mar 03 2009 Harald Hoyer <harald@redhat.com> 139-2
- speedup of start_udev by doing make_extra_nodes in parallel to 
  the daemon start

* Fri Feb 27 2009 Harald Hoyer <harald@redhat.com> 139-1
- version 139

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 137-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Harald Hoyer <harald@redhat.com> 137-4
- fixed md change/remove event handling

* Thu Feb 05 2009 Harald Hoyer <harald@redhat.com> 137-3
- added 5 second sleep for "modprobedebug" to catch bad modules

* Fri Jan 30 2009 Harald Hoyer <harald@redhat.com> 137-2
- moved groupadd to pre section (bug #483089)

* Thu Jan 29 2009 Harald Hoyer <harald@redhat.com> 137-1
- version 137
- add vol_id patches from kzak
- dialout group has gid 18 now

* Tue Jan 20 2009 Harald Hoyer <harald@redhat.com> 136-2
- added some rule fixes, which will be in udev-137

* Tue Jan 20 2009 Harald Hoyer <harald@redhat.com> 136-1
- test for restorecon in start_udev before it is used (bug #480608)
- added groups video audio cdrom tape dialout in post
  (might be moved to MAKEDEV)
- version 136

* Tue Dec 16 2008 Harald Hoyer <harald@redhat.com> 135-3
- added sepol patch

* Tue Dec 16 2008 Harald Hoyer <harald@redhat.com> 135-2
- changed udevsettle -> udevadm settle
- added doc to libudev-devel
- added more attr and defattr
- various rpmlint fixes

* Tue Dec 02 2008 Harald Hoyer <harald@redhat.com> 135-1
- version 135

* Wed Nov 19 2008 Harald Hoyer <harald@redhat.com> 133-1
- version 133

* Mon Nov 10 2008 Harald Hoyer <harald@redhat.com> 132-1
- version 132
- added memory stick rules (bug #470096)

* Thu Oct 16 2008 Harald Hoyer <harald@redhat.com> 127-2
- added 2 patches for md raid vol_id 

* Mon Sep 01 2008 Harald Hoyer <harald@redhat.com> 127-1
- version 127

* Fri Aug 08 2008 Harald Hoyer <harald@redhat.com> 126-1
- version 126
- fixed udevadm syntax in start_udev (credits B.J.W. Polman)
- removed some manually created devices from makedev (bug #457125)

* Tue Jun 17 2008 Harald Hoyer <harald@redhat.com> 124-1.1
- readded udevcontrol, udevtrigger symlinks for Fedora 9,
  which are needed by live-cd-tools

* Thu Jun 12 2008 Harald Hoyer <harald@redhat.com> 124-1
- version 124
- removed udevcontrol, udevtrigger symlinks (use udevadm now)

* Tue Jun  3 2008 Jeremy Katz <katzj@redhat.com> - 121-2.20080516git
- Add lost F9 change to remove /dev/.udev in start_udev (#442827)

* Fri May 16 2008 Harald Hoyer <harald@redhat.com> 121-1.20080516git
- version 121 + latest git fixes

* Thu May 07 2008 Harald Hoyer <harald@redhat.com> 120-6.20080421git
- added input/hp_ilo_mouse symlink

* Tue May 06 2008 Harald Hoyer <harald@redhat.com> 120-5.20080421git
- remove /dev/.udev in start_udev (bug #442827)

* Mon Apr 21 2008 Harald Hoyer <harald@redhat.com> 120-4.20080421git
- added patches from git:
- persistent device naming: also read unpartitioned media
- scsi_id: initialize serial strings
- logging: add trailing newline to all strings
- path_id: remove subsystem whitelist
- allow setting of MODE="0000"
- selinux: more context settings
- rules_generator: net rules - always add KERNEL== match to generated rules
- cdrom_id: replace with version which also exports media properties
- vol_id: add --offset option
- udevinfo: do not replace chars when printing ATTR== matches
- Resolves: rhbz#440568

* Fri Apr 11 2008 Harald Hoyer <harald@redhat.com> 120-3
- fixed pre/preun scriptlets (bug #441941)
- removed fedora specific patch for selinux symlink handling

* Sat Apr 05 2008 Harald Hoyer <harald@redhat.com> 120-2
- removed warning about deprecated /lib/udev/devices (rhbz#440961)
- replaced /usr/bin/find with shell find function (rhbz#440961)

* Fri Apr 04 2008 Harald Hoyer <harald@redhat.com> 120-1
- version 120

* Mon Mar 17 2008 Harald Hoyer <harald@redhat.com> 118-11
- removed /var/lib/udev/rules.d again

* Fri Mar 14 2008 Harald Hoyer <harald@redhat.com> 118-10
- turned off MAKEDEV cache, until the generated shell scripts 
  create new directories

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-9
- added more support for the "modprobedebug" kernel command 
  line option, to debug hanging kernel modules

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-8
- added /etc/sysconfig/udev to configure some speedups
- added "udevnopersist" as a kernel command line, to disable
  persistent storage symlink generation

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-7
- files from /var/lib/udev/rules.d are copied to /dev/.udev/rules.d 
  at startup and back at shutdown
- persistent cd and net rules generate the files in 
  /dev/.udev/rules.d now
- added post section to symlink 70-persistent-cd.rules 70-persistent-net.rules
  from /etc/udev/rules.d to /dev/.udev/rules.d

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-6
- moved all generated files to /var/lib/udev 
  (also 70-persistent-cd.rules 70-persistent-net.rules)
- added a caching mechanism for MAKEDEV (saves some seconds on startup)
- added trigger for selinux-policy and MAKEDEV to remove the udev cache files

* Wed Feb 20 2008 Harald Hoyer <harald@redhat.com> 118-4
- made symlinks relative (rhbz#432878)
- removed the backgrounding of node creation (rhbz#381461)
- do not change sg group ownership to disk for scanners (rhbz#432602)
- attempt to fix selinux symlink bug (rhbz#345071)
- fixed URL
- made rpmlint mostly happy
- disabled static version (no static selinux lib)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 118-3
- Autorebuild for GCC 4.3

* Wed Jan 09 2008 Harald Hoyer <harald@redhat.com> 118-2
- reenabled static version

* Tue Jan 08 2008 Harald Hoyer <harald@redhat.com> 118-1
- version 118
- removed old USB compat rule (rhbz#424331)
- disabled static version

* Thu Oct 18 2007 Harald Hoyer <harald@redhat.com> 116-3
- fixed preun chkconfig
- added /sbin path to chkconfig in post section 
- patch: do not generate net rules for type > 256
- fixes glitches appearing in bz#323991

* Tue Oct 16 2007 Dennis Gilmore <dennis@ausil.us> 116-2
- sparc64 requires -fPIE not -fpie

* Mon Oct 15 2007 Harald Hoyer <harald@redhat.com> 116-1
- version 116

* Fri Oct 12 2007 Harald Hoyer <harald@redhat.com> 115-5.20071012git
- added upstream patch for rhbz#328691
- moved floppy module loading to pnp-alias in /etc/modprobe.d/floppy-pnp

* Wed Oct 10 2007 Harald Hoyer <harald@redhat.com> 115-5.20070921git
- better modprobe options for the kernel command line 'modprobedebug' option

* Fri Sep 21 2007 Harald Hoyer <harald@redhat.com> - 115-4
- more upstream fixes from git

* Thu Sep 20 2007 Harald Hoyer <harald@redhat.com> - 115-3
- some upstream fixes from git
- removed last_rule for loop rules
- added "udevinfo udevtrace" kernel command line options for better debugging

* Fri Sep 07 2007 Harald Hoyer <harald@redhat.com> - 115-2
- some upstream fixes from git
- last_rule for loop rules (speedup for live-cds/qemu with 128 loop devices)

* Thu Aug 24 2007 Harald Hoyer <harald@redhat.com> - 115-1
- version 115

* Fri Aug 24 2007 Harald Hoyer <harald@redhat.com> - 113-12
- removed /dev/tape symlink, because it's now a directory
  (bug #251755)

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 114-4
- added patch to prevent persistent net rules for virtual network interfaces,
  like vmware and vlans

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 114-3
- changed license tag
- changed to latest upstream rule ordering

* Thu Aug 16 2007 Harald Hoyer <harald@redhat.com> - 113-11
- readded firmware rule (#252983)

* Wed Aug 15 2007 Harald Hoyer <harald@redhat.com> - 113-10
- do not run vol_id on non-partition block devices (bug #251401)
- read all multiline pnp modaliases again

* Mon Aug 13 2007 Harald Hoyer <harald@redhat.com> - 114-2
- fixed isapnp rule (bug #251815)
- fix for nikon cameras (bug #251401)

* Fri Aug 10 2007 Harald Hoyer <harald@redhat.com> - 114-1
- version 114
- big rule unification and cleanup
- added persistent names for network and cdrom devices over reboot

* Wed Aug 08 2007 Harald Hoyer <harald@redhat.com> - 113-9
- added lp* to 50-udev.nodes (#251272)

* Mon Jul 30 2007 Harald Hoyer <harald@redhat.com> - 113-8
- removed "noreplace" config tag from rules (#250043)

* Fri Jul 27 2007 Harald Hoyer <harald@redhat.com> - 113-7
- major rule cleanup
- removed persistent rules from 50 and included upstream rules
- removed skip_wait from modprobe

* Fri Jul 20 2007 Harald Hoyer <harald@redhat.com> - 113-6
- kernel does not provide usb_device anymore,
  corrected the rules (#248916)

* Thu Jul 19 2007 Harald Hoyer <harald@redhat.com> - 113-5
- corrected the rule for usb devices (#248916)

* Sat Jul 14 2007 Harald Hoyer <harald@redhat.com> - 113-4
- do not collect modprobes (bug #222542), because firmware
  loading seems to depend on it.

* Mon Jul  9 2007 Harald Hoyer <harald@redhat.com> - 113-3
- speedup things a little bit

* Wed Jun 27 2007 Harald Hoyer <harald@redhat.com> - 113-2
- added more firewire symlinks (#240770)
- minor rule patches

* Tue Jun 26 2007 Harald Hoyer <harald@redhat.com> - 113-1
- version 113
- added rule for SD cards in a TI FlashMedia slot (#217070)

* Tue Jun 26 2007 Harald Hoyer <harald@redhat.com> - 106-4.1
- fixed modprobedebug option
- removed snd-powermac from the default modules (#200585)

* Wed May 02 2007 Harald Hoyer <harald@redhat.com> - 106-4
- do not skip all events on modprobe (#238385)
- Resolves: rhbz#238385

* Fri Apr 27 2007 Harald Hoyer <harald@redhat.com> - 106-3
- modprobe only on modalias (bug #238140)
- make startup messages visible again
- speedup boot process by not executing pam_console_apply while booting
- Resolves: rhbz#238140

* Wed Apr 11 2007 Harald Hoyer <harald@redhat.com> - 106-2
- create floppy device nodes with the correct selinux context (bug #235953)
- Resolves: rhbz#235953

* Wed Mar  7 2007 Harald Hoyer <harald@redhat.com> - 106-1
- version 106
- specfile cleanup
- removed pilot rule
- removed dasd_id and dasd_id rule
- provide static versions in a subpackage

* Wed Feb 21 2007 Harald Hoyer <harald@redhat.com> - 105-1
- version 105

* Tue Feb  6 2007 Harald Hoyer <harald@redhat.com> - 104-2
- moved uinput to input subdirectory (rhbz#213854)
- added USB floppy symlinks (rhbz#185171)
- fixed ZIP drive handling (rhbz#223016)
- Resolves: rhbz#213854,rhbz#185171,rhbz#223016

* Tue Jan 23 2007 Harald Hoyer <harald@redhat.com> - 104-1
- version 104
- merged changes from RHEL

* Wed Dec  6 2006 Harald Hoyer <harald@redhat.com> - 103-3
- changed DRIVER to DRIVERS 
- Resolves: rhbz#218160

* Fri Nov 10 2006 Harald Hoyer <harald@redhat.com> - 103-2
- changed SYSFS to new ATTR rules
- Resolves: rhbz#214898

* Fri Nov 10 2006 Harald Hoyer <harald@redhat.com> - 103-1
- Removed 51-hotplug.rules
- Resolves: rhbz#214277

* Wed Oct 11 2006 Harald Hoyer <harald@redhat.com> - 095-14
- skip persistent block for gnbd devices (bug #210227)

* Wed Oct  4 2006 Harald Hoyer <harald@redhat.com> - 095-13
- fixed path_id script (bug #207139)

* Tue Oct  3 2006 Jeremy Katz <katzj@redhat.com> - 095-12
- autoload mmc_block (#171687)

* Wed Sep 27 2006 Harald Hoyer <harald@redhat.com> - 095-10
- typo in xpram/slram rule (bug #205563)

* Mon Sep 25 2006 Harald Hoyer <harald@redhat.com> - 095-9
- improved error msg for firmware_helper (bug #206944)
- added xpram symlink to slram device nodes (bug #205563)
- removed infiniband rules (bug #206224)
- use newest path_id script (bug #207139)

* Tue Aug 29 2006 Harald Hoyer <harald@redhat.com> - 095-8
- fixed bug #204157

* Wed Aug 16 2006 Harald Hoyer <harald@redhat.com> - 095-7
- added udevtimeout=<timeout in seconds>
  kernel command line parameters for start_udev 
  (default is to wait forever)

* Wed Aug 16 2006 Harald Hoyer <harald@redhat.com> - 095-6
- new speedup patch for selinux (bug #202673)

* Thu Aug 10 2006 Harald Hoyer <harald@redhat.com> - 095-5
- allow long comments (bug #200244)

* Mon Aug  7 2006 Harald Hoyer <harald@redhat.com> - 095-4
- fixed CAPI device nodes (bug #139321)
- fixed bug #201422

* Wed Jul 12 2006 Harald Hoyer <harald@redhat.com> - 095-3
- more infiniband rules (bug #198501)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 095-2.1
- rebuild

* Thu Jul  6 2006 Harald Hoyer <harald@redhat.com> - 095-2
- added option to debug udev with kernel cmdline option "udevdebug"

* Wed Jul  5 2006 Harald Hoyer <harald@redhat.com> - 095-1
- version 095

* Wed Jun 14 2006 Harald Hoyer <harald@redhat.com> - 094-1
- version 094

* Sun May 21 2006 Peter Jones <pjones@redhat.com> - 092-2
- Fix typo in pam-console rule

* Wed May 18 2006 Harald Hoyer <harald@redhat.com> - 092-1
- version 092
- corrected some rules (bug #192210 #190927)

* Tue May 09 2006 Harald Hoyer <harald@redhat.com> - 091-3
- corrected some rules (bug #190927)

* Wed May 03 2006 Harald Hoyer <harald@redhat.com> - 091-2
- added subpackages libvolume_id and libvolume_id-devel

* Wed May 03 2006 Harald Hoyer <harald@redhat.com> - 091-1
- version 091

* Wed Apr 19 2006 Harald Hoyer <harald@redhat.com> - 090-1
- version 090

* Thu Apr 13 2006 Harald Hoyer <harald@redhat.com> - 089-1
- version 089
- do not force loading of parport_pc (bug #186850)
- manually load snd-powermac (bug #176761)
- added usb floppy symlink (bug #185171)
- start_udev uses udevtrigger now instead of udevstart

* Wed Mar 08 2006 Harald Hoyer <harald@redhat.com> - 084-13
- fixed pam_console rules (#182600)

* Mon Mar 06 2006 Harald Hoyer <harald@redhat.com> - 084-12
- fixed DRI permissions

* Sun Mar 05 2006 Bill Nottingham <notting@redhat.com> - 084-11
- use $ENV{MODALIAS}, not $modalias (#181494)

* Thu Mar 02 2006 Harald Hoyer <harald@redhat.com> - 084-10
- fixed cdrom rule

* Wed Mar 01 2006 Harald Hoyer <harald@redhat.com> - 084-9
- create non-enum device (cdrom, floppy, scanner, changer)
  for compatibility (random device wins)
  e.g. /dev/cdrom -> hdd /dev/cdrom-hdc -> hdc /dev/cdrom-hdd -> hdd

* Wed Mar 01 2006 Harald Hoyer <harald@redhat.com> - 084-8
- fixed ZIP drive thrashing (bz #181041 #182601)
- fixed enumeration (%%e does not work anymore) (bz #183288)

* Fri Feb 24 2006 Peter Jones <pjones@redhat.com> - 084-7
- Don't start udevd in %%post unless it's already running
- Stop udevd before chkconfig --del in %%preun

* Fri Feb 24 2006 Harald Hoyer <harald@redhat.com> - 084-6
- put back original WAIT_FOR_SYSFS rule

* Fri Feb 24 2006 Harald Hoyer <harald@redhat.com> - 084-5
- removed WAIT_FOR_SYSFS rule

* Wed Feb 22 2006 Harald Hoyer <harald@redhat.com> - 084-4
- fixed group issue with vol_id (bz #181432)
- fixed dvb permissions (bz #179993)
- added support for scsi media changer (bz #181911)
- fixed pktcdvd device creation (bz #161268)

* Tue Feb 21 2006 Florian La Roche <laroche@redhat.com> - 084-3
- also output the additional space char as part of the startup message

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 084-1.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Harald Hoyer <harald@redhat.com> - 084-1
- version 084

* Mon Feb 06 2006 Harald Hoyer <harald@redhat.com> - 078-9
- closed fd leak (bug #179980)

* Thu Jan 26 2006 Harald Hoyer <harald@redhat.com> - 078-8
- changed usb device naming

* Tue Jan 24 2006 Harald Hoyer <harald@redhat.com> - 078-7
- put WAIT_FOR_SYSFS rules in 05-udev-early.rules

* Mon Jan 23 2006 Harald Hoyer <harald@redhat.com> - 078-6
- added some WAIT_FOR_SYSFS rules
- removed warning message, if udev_db is not available

* Sun Jan 22 2006 Kristian Høgsberg <krh@redhat.com> 078-5
- Drop udev dependency (#178621).

* Tue Jan 11 2006 Harald Hoyer <harald@redhat.com> - 078-4
- removed group "video" from the rules
- fixed specfile
- load nvram, floppy, parport and lp modules in
  /etc/sysconfig/modules/udev-stw.modules until there 
  is a better solution
- fixed more floppy module loading

* Fri Dec 23 2005 Harald Hoyer <harald@redhat.com> - 078-3
- fixed floppy module loading
- added monitor socket
- fixed typo in dvb rule

* Wed Dec 21 2005 Bill Nottingham <notting@redhat.com> - 078-2
- udevstart change: allow greylisting of certain modaliases (usb, firewire)

* Wed Dec 21 2005 Harald Hoyer <harald@redhat.com> - 078-1
- version 078
- fixed symlink to pam_console.dev

* Thu Dec 15 2005 Harald Hoyer <harald@redhat.com> - 077-2
- switched back to udevstart and use active /dev/.udev/queue waiting 
  in start_udev
- removed support for old kernels
- refined some udev.rules

* Mon Dec 13 2005 Harald Hoyer <harald@redhat.com> - 077-1
- version 077
- patch to include udevstart2 in udevd and delay daemonize until queue is empty

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec 06 2005 Harald Hoyer <harald@redhat.com> - 076-1
- speedup udevd with selinux by calling matchpathcon_init_prefix()
- version 076

* Mon Nov 21 2005 Harald Hoyer <harald@redhat.com> - 075-4
- speedup udev event replay with udevstart2 

* Fri Nov 18 2005 Harald Hoyer <harald@redhat.com> - 075-3
- refined start_udev for old kernels

* Fri Nov 11 2005 Harald Hoyer <harald@redhat.com> - 075-2
- moved /etc/udev/scripts to /lib/udev
- moved /etc/udev/devices to /lib/udev/devices
- added new event replay for kernel >= 2.6.15
- added usb devices
- renamed cpu device to cpuid (bug #161538)
- changed vendor string "Onstream" to "On[sS]tream" (bug #173043)
- compiled all *_id programs statically

* Fri Nov 11 2005 Harald Hoyer <harald@redhat.com> - 075-1
- version 075

* Tue Oct 25 2005 Harald Hoyer <harald@redhat.com> - 071-1
- version 071

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-10
- removed group usb

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-9
- added libsepol-devel BuildReq
- refined persistent rules

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-8
- corrected c&p edd_id rule, symlink for js devices
- added -lsepol

* Thu Oct 06 2005 Harald Hoyer <harald@redhat.com> - 069-7
- added edd_id

* Fri Sep 30 2005 Harald Hoyer <harald@redhat.com> - 069-6
- special handling of IEEE1394 firewire devices (bug #168093)

* Fri Sep 23 2005 Harald Hoyer <harald@redhat.com> - 069-5
- added missing path_id

* Wed Sep 21 2005 Harald Hoyer <harald@redhat.com> - 069-4
- readded volume_id now known as vol_id, bug #168883

* Thu Sep 15 2005 Bill Nottingham <notting@redhat.com> - 069-3
- fix firmware loading

* Wed Sep 14 2005 Bill Nottingham <notting@redhat.com> - 069-2
- own /lib/firmware (#167016)

* Wed Sep 14 2005 Harald Hoyer <harald@redhat.com> - 069-1
- version 069

* Thu Aug 04 2005 Harald Hoyer <harald@redhat.com> - 063-6
- compile with pie .. again... (#158935)
- fixed typo in echo (#138509)

* Tue Aug 02 2005 Harald Hoyer <harald@redhat.com> - 063-5
- fixed scsi hotplug replay

* Tue Aug 02 2005 Bill Nottingham <notting@redhat.com> - 063-5
- add rule to allow function id matching for pcmcia after loading
  modules (#164665)

* Tue Aug 02 2005 Harald Hoyer <harald@redhat.com> - 063-4
- fixed typo for tape devices and changed mode to 0660

* Thu Jul 28 2005 Harald Hoyer <harald@redhat.com> - 063-3
- changed "SYMLINK=" to "SYMLINK+="

* Sun Jul 24 2005 Bill Nottingham <notting@redhat.com> - 063-2
- don't set SEQNUM for scsi replay events (#163729)

* Tue Jul 19 2005 Bill Nottingham <notting@redhat.com> - 063-1
- update to 063
- handle the hotplug events for ieee1394, scsi, firmware

* Fri Jul 08 2005 Bill Nottingham <notting@redhat.com> - 062-2
- update to 062
- use included ata_id, build usb_id
- load modules for pci, usb, pcmcia
- ship RELEASE-NOTES in %%doc

* Thu Jul 07 2005 Harald Hoyer <harald@redhat.com> - 058-2
- compile with pie

* Fri May 20 2005 Bill Nottingham <notting@redhat.com> - 058-1
- update to 058, fixes conflict with newer kernels (#158371)

* Thu May 12 2005 Harald Hoyer <harald@redhat.com> - 057-6
- polished persistent scripts

* Thu May  5 2005 Bill Nottingham <notting@redhat.com> - 057-5
- rebuild

* Thu May  5 2005 Bill Nottingham <notting@redhat.com> - 057-4
- better check for mounted tmpfs on /dev (#156862)

* Wed Apr 27 2005 Peter Jones <pjones@redhat.com> - 057-3
- use udevstart rather than udev for udevstart.static 

* Thu Apr 21 2005 Harald Hoyer <harald@redhat.com> - 057-2
- added Inifiniband devices (bug #147035)
- fixed pam_console.dev (bug #153250)

* Mon Apr 18 2005 Harald Hoyer <harald@redhat.com> - 057-1
- version 057

* Fri Apr 15 2005 Dan Walsh <dwalsh@redhat.com> - 056-2
- Fix SELinux during creation of Symlinks

* Mon Apr 11 2005 Harald Hoyer <harald@redhat.com> - 056-1
- updated to version 056
- merged permissions in the rules file
- added udevpermconv.sh to convert old permission files

* Mon Mar 28 2005 Warren Togami <wtogami@redhat.com> - 050-10
- own default and net dirs (#151368 Hans de Goede)

* Mon Mar 07 2005 Warren Togami <wtogami@redhat.com> - 050-9
- fixed rh#150462 (udev DRI permissions)

* Wed Mar 02 2005 Harald Hoyer <harald@redhat.com> - 050-8
- fixed rh#144598

* Fri Feb 18 2005 Harald Hoyer <harald@redhat.com> - 050-6
- introducing /etc/udev/makedev.d/50-udev.nodes
- glibcstatic patch modified to let gcc4 compile udev

* Thu Feb 10 2005 Harald Hoyer <harald@redhat.com> - 050-5
- doh, reverted the start_udev devel version, which slipped in

* Thu Feb 10 2005 Harald Hoyer <harald@redhat.com> - 050-3
- fixed forgotten " in udev.rules

* Tue Jan 11 2005 Harald Hoyer <harald@redhat.com> - 050-2
- removed /dev/microcode, /dev/cpu/microcode is now the real node
- cleaned up start_udev

* Tue Jan 11 2005 Harald Hoyer <harald@redhat.com> - 050-1
- version 050
- /dev/cpu/0/microcode -> /dev/cpu/microcode

* Tue Dec 21 2004 Dan Walsh <dwalsh@redhat.com> - 048-4
- Call selinux_restore to fix labeling problem in selinux
- Fixes rh#142817

* Tue Dec 21 2004 Harald Hoyer <harald@redhat.com> - 048-3
- maybe fixed bug rh#143367

* Thu Dec 16 2004 Harald Hoyer <harald@redhat.com> - 048-2
- fixed a case where reading /proc/ide/hd?/media returns EIO
  (bug rh#142713)
- changed all device node permissions of group "disk" to 0640 
  (bug rh#110197)
- remove $udev_db with -fr in case of a directory (bug rh#142962)

* Mon Dec 13 2004 Harald Hoyer <harald@redhat.com> - 048-1
- version 048
- major specfile cleanup

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 042-1
- version 042

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 039-10
- speed improvement, scripts in rules are now executed only once,
  instead of four times

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 039-9
- removed wrong SIG_IGN for SIGCHLD
- moved ide media check to script to wait for the procfs

* Wed Nov  3 2004 Jeremy Katz <katzj@redhat.com> - 039-8.FC3
- recreate lvm device nodes if needed in the trigger (#137807)

* Wed Nov 03 2004 Harald Hoyer <harald@redhat.com> - 039-6.FC3.2
- replace udev.conf by default
- LANG=C for fgrep in start_udev; turn grep into fgrep

* Tue Nov 02 2004 Harald Hoyer <harald@redhat.com> - 039-6.FC3.1
- speed up pam_console.dev
- mount pts and shm, in case of the dev trigger
- increased timeout for udevstart
- removed syslog() from signal handler (caused vmware locks)
- turned off logging, which speeds up the boot process

* Thu Oct 21 2004 Harald Hoyer <harald@redhat.com> - 039-6
- fixed typo

* Thu Oct 21 2004 Harald Hoyer <harald@redhat.com> - 039-5
- added udev-039-norm.patch, which prevents removal of hd* devices,
  because the kernel sends remove/add events, if an IDE removable device
  is close(2)ed. mke2fs, e.g. would fail in this case.

* Wed Oct 20 2004 Harald Hoyer <harald@redhat.com> - 039-4
- do not call dev.d scripts, if network interface hasn't changed 
  the name
- correct wait for dummy network devices
- removed NONBLOCK from volume-id
- do not log in udev.static, which should fix bug 136005 

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-3
- refined wait_for_sysfs for udev.static

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-2
- improved wait_for_sysfs for virtual consoles with Kay Siever's patch
- wait for ppp class
- wait for LVM dm- devices
- integrate wait_for_sys in udev.static for the initrd

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-1
- version 039, fixes also manpage bug 135996 
- fixed glibc issue for static version (getgrnam, getpwnam) (bug 136005)
- close the syslog in every app

* Fri Oct 15 2004 Harald Hoyer <harald@redhat.com> - 038-2
- par[0-9] is now a symlink to lp
- MAKEDEV the parport devices
- now conflicts with older initscripts

* Thu Oct 14 2004 Harald Hoyer <harald@redhat.com> - 038-1
- raw device nodes are now created in directory raw
- version 038

* Wed Oct 13 2004 Harald Hoyer <harald@redhat.com> - 036-1
- better wait_for_sysfs warning messages

* Wed Oct 13 2004 Harald Hoyer <harald@redhat.com> - 035-2
- fixed double bug in start_udev (bug 135405)

* Tue Oct 12 2004 Harald Hoyer <harald@redhat.com> - 035-1
- version 035, which only improves wait_for_sysfs
- load ide modules in start_udev, until a hotplug script is available
  (bug 135260)

* Mon Oct 11 2004 Harald Hoyer <harald@redhat.com> - 034-3
- removed scary error messages from wait_for_sysfs
- symlink from nst? -> tape?
- kill udevd on update

* Fri Oct  8 2004 Harald Hoyer <harald@redhat.com> - 034-2
- check for /proc/sys/dev/cdrom/info existence in check-cdrom.sh

* Fri Oct  8 2004 Harald Hoyer <harald@redhat.com> - 034-1
- new version udev-034
- removed patches, which went upstream
- pam_console.dev link renamed to 05-pam_console.dev
- MAKEDEV.dev links renamed to 10-MAKEDEV.dev

* Thu Oct 07 2004 Harald Hoyer <harald@redhat.com> - 032-10
- added floppy madness (bug 134830)
- replay scsi events in start_udev for the devices on the adapter (bug 130746)

* Wed Oct 06 2004 Harald Hoyer <harald@redhat.com> - 032-9
- obsoleted $UDEV_LOG, use udev_log
- correct SYMLINK handling in pam_console.dev
- specfile cleanup
- added check-cdrom.sh for nice cdrom symlinks

* Mon Oct 04 2004 Harald Hoyer <harald@redhat.com> - 032-8
- added patches from Féliciano Matias for multiple symlinks (bug 134477 and 134478)
- corrected some permissions with a missing leading 0
- added z90crypt to the permissions file (bug 134448)
- corrected requires and conflicts tags
- removed /dev/log from MAKEDEV creation

* Fri Oct 01 2004 Harald Hoyer <harald@redhat.com> - 032-7
- more device nodes for those without initrd

* Thu Sep 30 2004 Harald Hoyer <harald@redhat.com> - 032-6
- prevent error message from device copying
- use already translated starting strings

* Wed Sep 29 2004 Harald Hoyer <harald@redhat.com> - 032-5
- add "fi" to start_udev
- do not create floppy devices manually (bug 133838)

* Tue Sep 28 2004 Harald Hoyer <harald@redhat.com> - 032-4
- made /etc/udev/devices/ for manual device nodes
- refined SELINUX check, if /dev is not yet mounted in start_dev

* Mon Sep 27 2004 Harald Hoyer <harald@redhat.com> - 032-3
- corrected permissions for /dev/rtc (bug 133636)
- renamed device-mapper to mapper/control (bug 133688)

* Wed Sep 22 2004 Harald Hoyer <harald@redhat.com> - 032-2
- removed option to turn off udev
- udevstart.static now symling to udev.static

* Tue Sep 21 2004 Harald Hoyer <harald@redhat.com> - 032-1
- version 032

* Mon Sep 20 2004 Harald Hoyer <harald@redhat.com> - 030-27
- simplified udev.conf
- refined close_on_exec patch
- added pam_console supply for symlinks, now gives correct permissions,
  for e.g. later plugged in cdroms
- renamed sr? to scd? (see devices.txt; k3b likes that :)

* Mon Sep 13 2004 Jeremy Katz <katzj@redhat.com> - 030-26
- require a 2.6 kernel
- prereq instead of requires MAKEDEV
- obsolete and provide dev
- add a trigger for the removal of /dev so that we set things up 

* Fri Sep 10 2004 Dan Walsh <dwalsh@redhat.com> - 030-25
- Use matchmediacon

* Fri Sep 10 2004 Harald Hoyer <harald@redhat.com> - 030-24
- check if SELINUX is not disabled before executing setfiles (bug 132099)

* Wed Sep  8 2004 Harald Hoyer <harald@redhat.com> - 030-23
- mount tmpfs with mode 0755 in start_udev

* Tue Sep  7 2004 Harald Hoyer <harald@redhat.com> - 030-22
- applied rules from David Zeuthen which read /proc directly without 
  shellscript

* Tue Sep  7 2004 Harald Hoyer <harald@redhat.com> - 030-21
- applied enumeration patch from David Zeuthen for cdrom symlinks (bug 131532)
- create /dev/ppp in start_udev (bug 131114)
- removed nvidia devices from start_udev
- check for restorecon presence in start_udev (bug 131904)

* Fri Sep  3 2004 Harald Hoyer <harald@redhat.com> - 030-20
- due to -x added to MAKEDEV specify the par and lp numbers

* Fri Sep  3 2004 Harald Hoyer <harald@redhat.com> - 030-19
- added udev-030-rhsec.patch (bug 130351)

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 030-18
- make the exact device in start_udev (and thus, require new MAKEDEV)

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 030-17
- make sure file contexts of everything in the tmpfs /dev are set right 
  when start_udev runs

* Thu Sep 02 2004 Harald Hoyer <harald@redhat.com> - 030-16
- moved %%{_sysconfdir}/hotplug.d/default/udev.hotplug to %%{_sysconfdir}/hotplug.d/default/10-udev.hotplug

* Thu Sep 02 2004 Harald Hoyer <harald@redhat.com> - 030-15
- added nvidia devices to start_udev
- added UDEV_RAMFS for backwards compat to udev.conf
- changed Group (bug 131488)
- added libselinux-devel to build requirements

* Wed Sep  1 2004 Jeremy Katz <katzj@redhat.com> - 030-14
- require MAKEDEV

* Wed Sep 1 2004 Dan Walsh <dwalsh@redhat.com> - 030-13
- Change to setfilecon if directory exists.

* Wed Sep 01 2004 Harald Hoyer <harald@redhat.com> - 030-12
- fixed start_udev

* Tue Aug 31 2004 Jeremy Katz <katzj@redhat.com> - 030-11
- use tmpfs instead of ramfs (it has xattr support now)
- change variables appropriately to TMPFS intead of RAMFS in udev.conf
- create loopN, not just loop in start_udev

* Fri Aug 27 2004 Dan Walsh <dwalsh@redhat.com> - 030-10
- Fix Patch

* Thu Aug 26 2004 Dan Walsh <dwalsh@redhat.com> - 030-9
- Cleaned up selinux patch

* Tue Aug 24 2004 Harald Hoyer <harald@redhat.com> - 030-8
- changed defaults not to remove device nodes
- added rule for net/tun
- extended start_udev to create devices, which can trigger module autoloading
- refined cloexec patch, to redirect stdin,out,err of /dev.d execed apps to /dev/null

* Mon Aug 23 2004 Harald Hoyer <harald@redhat.com> - 030-7
- removed usage of /usr/bin/seq in start_udev
- set correct permissions in start_udev
- extended the cloexec patch
- removed udev-persistent package (define with_persistent==0)
- check for /var/run/console/console.lock before calling /sbin/pam_console_setowner
- linked pam_console_setowner statically against libglib-2.0.a

* Fri Aug 20 2004 Harald Hoyer <harald@redhat.com> - 030-5
- use correct console.lock file now in pam_console_setowner

* Wed Aug 18 2004 Harald Hoyer <harald@redhat.com> - 030-4
- added the selinux patch

* Fri Jul 23 2004 Harald Hoyer <harald@redhat.com> - 030-3
- extended the cloexec patch

* Wed Jul 21 2004 Dan Walsh <dwalsh@redhat.com> - 030-2
- Close Database fd in exec processes using FD_CLOSEXEC

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 030-1
- version 030

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 029-4
- added udevstart.static 

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 029-3
- put /etc/sysconfig/udev in /etc/udev/udev.conf and removed it
- made only udev.static static
- make our defaults the default values
- removed /udev

* Tue Jul  6 2004 Harald Hoyer <harald@redhat.com> - 029-1
- version 029, added udev_remove and udev_owner to udev.conf

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  8 2004 Harald Hoyer <harald@redhat.com> - 026-3
- fixed UDEV_REMOVE=no

* Tue Jun  8 2004 Harald Hoyer <harald@redhat.com> - 026-2
- udev-026
- preserve ownership of device nodes, which already exist
- do not remove device nodes if UDEV_REMOVE="no"
- added volume_id
- build with klibc

* Wed May 26 2004 Harald Hoyer <harald@redhat.com> - 025-1
- udev-025
- added ata_identify
- build nearly all with dietlibc

* Mon May 10 2004 Elliot Lee <sopwith@redhat.com> 024-6
- Turn off udevd by default for FC2

* Tue Apr 20 2004 Harald Hoyer <harald@redhat.com> - 024-5
- fixed permission for /dev/tty (FC2)

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-4
- moved the 00- files to 50-, to let the use place his files in front

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-3
- set UDEV_SELINUX to yes
- added UDEV_LOG

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-2
- added /udev to filelist

* Wed Apr 14 2004 Harald Hoyer <harald@redhat.com> - 024-1
- update to 024
- added /etc/sysconfig/udev
- added selinux, pam_console, dbus support

* Fri Mar 26 2004 Harald Hoyer <harald@redhat.com> - 023-1
- update to 023

* Wed Mar 24 2004 Bill Nottingham <notting@redhat.com> 022-1
- update to 022

* Sun Mar 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- really move initscript

* Sun Feb 29 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- move chkconv to preun
- nicer url

* Wed Feb 25 2004 Harald Hoyer <harald@redhat.com> - 018-1
- changes permissions and rules

* Mon Feb 23 2004 Dan Walsh <dwalsh@redhat.com>
- Add selinux support

* Thu Feb 19 2004 Greg Kroah-Hartman <greg@kroah.com>
- add some more files to the documentation directory
- add ability to build scsi_id and make it the default

* Mon Feb 16 2004 Greg Kroah-Hartman <greg@kroah.com>
- fix up udevd build, as it's no longer needed to be build seperatly
- add udevtest to list of files
- more Red Hat sync ups.

* Thu Feb 12 2004 Greg Kroah-Hartman <greg@kroah.com>
- add some changes from the latest Fedora udev release.

* Mon Feb 2 2004 Greg Kroah-Hartman <greg@kroah.com>
- add udevsend, and udevd to the files
- add ability to build udevd with glibc after the rest is build with klibc

* Mon Jan 26 2004 Greg Kroah-Hartman <greg@kroah.com>
- added udevinfo to rpm
- added URL to spec file
- added udevinfo's man page

* Mon Jan 05 2004 Rolf Eike Beer <eike-hotplug@sf-tec.de>
- add defines to choose the init script (Redhat or LSB)

* Tue Dec 16 2003 Robert Love <rml@ximian.com>
- install the initscript and run chkconfig on it

* Tue Nov 2 2003 Greg Kroah-Hartman <greg@kroah.com>
- changes due to config file name changes

* Fri Oct 17 2003 Robert Love <rml@tech9.net>
- Make work without a build root
- Correctly install the right files
- Pass the RPM_OPT_FLAGS to gcc so we can build per the build policy
- Put some prereqs in
- Install the hotplug symlink to udev

* Mon Jul 28 2003 Paul Mundt <lethal@linux-sh.org>
- Initial spec file for udev-0.2.
