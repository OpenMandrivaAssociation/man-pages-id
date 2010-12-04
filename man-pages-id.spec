%define LNG id
%define name man-pages-%LNG
%define version 0.1
%define release %mkrel 16

Summary: Man pages in Indonesian language
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Internationalization
Source: id-man.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: man => 1.5j-8mdk
Requires: locales-%LNG, man => 1.5j-8mdk
Autoreq: false
BuildArch: noarch

%description
A collection of man pages for Linux in Indonesian language

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%_mandir/%LNG/
tar jxf %{SOURCE0} -C %{buildroot}/%_mandir/%LNG/

LANG=%LNG DESTDIR=%{buildroot} %{_sbindir}/makewhatis %{buildroot}/%_mandir/%LNG

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron << EOF
#!/bin/bash
LANG=%LNG %{_sbindir}/makewhatis %_mandir/%LNG
exit 0
EOF
chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron

mkdir -p  %{buildroot}/var/cache/man/%LNG

touch %{buildroot}/var/cache/man/%LNG/whatis

%post
%create_ghostfile /var/cache/man/%LNG/whatis root root 644

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,man,755)
#%doc CHANGES README* COPYRIGHT
%dir %_mandir/%LNG
%dir /var/cache/man/%LNG
%config(noreplace) /var/cache/man/%LNG/whatis
%ghost %config(noreplace) /var/cache/man/%LNG/whatis
%_mandir/%LNG/man*
%_mandir/%LNG/whatis
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron

