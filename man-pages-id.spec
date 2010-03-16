%define LANG id
%define name man-pages-%LANG
%define version 0.1
%define release %mkrel 15

Summary: Man pages in Indonesian language
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Internationalization
Source: id-man.tar.bz2
Buildroot: %_tmppath/%name-root
BuildRequires: man => 1.5j-8mdk
Requires: locales-%LANG, man => 1.5j-8mdk
Autoreq: false
BuildArch: noarch

%description
A collection of man pages for Linux in Indonesian language

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/%LANG/
tar jxf %{SOURCE0} -C $RPM_BUILD_ROOT/%_mandir/%LANG/

LANG=%LANG DESTDIR=$RPM_BUILD_ROOT /usr/sbin/makewhatis $RPM_BUILD_ROOT/%_mandir/%LANG

mkdir -p $RPM_BUILD_ROOT/etc/cron.weekly
cat > $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis-%LANG.cron << EOF
#!/bin/bash
LANG=%LANG /usr/sbin/makewhatis %_mandir/%LANG
exit 0
EOF
chmod a+x $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis-%LANG.cron

mkdir -p  $RPM_BUILD_ROOT/var/cache/man/%LANG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,man,755)
#%doc CHANGES README* COPYRIGHT
%dir %_mandir/%LANG
%dir /var/cache/man/%LANG
%config(noreplace) /var/cache/man/%LANG/whatis
%_mandir/%LANG/man*
%config(noreplace) %attr(755,root,root)/etc/cron.weekly/makewhatis-%LANG.cron

