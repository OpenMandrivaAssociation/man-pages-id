%define LNG id

Summary:	Man pages in Indonesian language
Name:		man-pages-%{LNG}
Version:	0.1
Release:	26
License:	GPLv2
Group:		System/Internationalization
Source0:	id-man.tar.bz2
BuildArch:	noarch
BuildRequires:	man
Requires:	locales-%{LNG}
Requires:	man
Autoreq:	false

%description
A collection of man pages for Linux in Indonesian language

%prep

%build

%install
mkdir -p %{buildroot}%{_mandir}/%{LNG}/
tar jxf %{SOURCE0} -C %{buildroot}%{_mandir}/%{LNG}/

LANG=%LNG DESTDIR=%{buildroot} %{_bindir}/mandb %{buildroot}/%{_mandir}/%{LNG}

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron << EOF
#!/bin/bash
LANG=%{LNG} %{_bindir}/mandb %{_mandir}/%{LNG}
exit 0
EOF
chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

mkdir -p  %{buildroot}/var/cache/man/%{LNG}

touch %{buildroot}/var/cache/man/%{LNG}/whatis

%post
%create_ghostfile /var/cache/man/%{LNG}/whatis root root 644

%files
%dir %{_mandir}/%{LNG}
%dir /var/cache/man/%{LNG}
%ghost %config(noreplace) /var/cache/man/%{LNG}/whatis
%{_mandir}/%{LNG}/man*
%{_mandir}/%{LNG}/cat*
%{_mandir}/%{LNG}/CACHEDIR.TAG*
%{_mandir}/%{LNG}/index.db*
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

