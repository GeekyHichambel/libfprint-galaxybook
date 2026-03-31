Name:           libfprint
Version:        1.94.10
Release:        100.galaxybook%{?dist}
Summary:        Toolkit for fingerprint scanner (Galaxy Book 4 FocalTech Fix)

License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/Sid1803/libfprint
# Source branch for the fix
Source0:        https://gitlab.freedesktop.org/Sid1803/libfprint/-/archive/samsung-galaxy-book4-fix/libfprint-samsung-galaxy-book4-fix.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)

%description
Custom build of libfprint with FocalTech 2808:6553 support 
specifically patched for the Samsung Galaxy Book 4 series.

%prep
%setup -q -n libfprint-samsung-galaxy-book4-fix

%build
%meson -Ddrivers=focaltech_moc -Ddoc=false -Dintrospection=true
%meson_build

%install
%meson_install

%files
# The libraries
%{_libdir}/libfprint-2.so.*
%{_libdir}/libfprint-2.so

# Development headers and pkgconfig
%{_includedir}/libfprint-2/
%{_libdir}/pkgconfig/libfprint-2.pc

# Udev rules - CRITICAL for hardware access
/usr/lib/udev/hwdb.d/60-autosuspend-libfprint-2.hwdb
/usr/lib/udev/rules.d/70-libfprint-2.rules

# GObject Introspection data
%{_libdir}/girepository-1.0/FPrint-2.0.typelib
%{_datadir}/gir-1.0/FPrint-2.0.gir

# AppData / Metainfo
%{_datadir}/metainfo/org.freedesktop.libfprint.metainfo.xml

# Excludes the installed tests to keep the package clean
%exclude %{_libexecdir}/installed-tests
%exclude %{_datadir}/installed-tests

%changelog
* Tue Mar 31 2026 Hichambel - 1.94.10-100.galaxybook
- Initial build with FocalTech FT9365 (2808:6553) support for Galaxy Book 4.
