%define LANG id

Summary: Man pages in Indonesian language
Name: man-pages-%LANG
Version: 0.1
Release: 9mdk
License: GPL
Group: System/Internationalization
Source: http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/id-man.tar.bz2
Icon: books-%LANG.xpm
URL: http://nakula.rvs.uni-bielefeld.de/made/my_project/ManPage/
Buildroot: %_tmppath/%name-root
BuildRequires: man => 1.5j-8mdk
Requires: locales-%LANG, man => 1.5j-8mdk
Prereq: sed grep man
Autoreq: false
BuildArch: noarch
Obsoletes: man-%LANG, manpages-%LANG
Provides: man-%LANG, manpages-%LANG

%description
A collection of man pages for Linux in Indonesian language

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/%LANG/
mkdir -p $RPM_BUILD_ROOT/var/catman/%LANG/cat{1,2,3,4,5,6,7,8,9,n}
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


%postun
# 0 means deleting the package
if [ "$1" = "0" ]; then
   ## Force removing of /var/catman/%LANG, if there isn't any man page
   ## directory /%_mandir/%LANG
   if [ ! -d %_mandir/%LANG ] ; then
       rm -rf /var/catman/%LANG
   fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,man,755)
#%doc CHANGES README* COPYRIGHT
%dir %_mandir/%LANG
%dir /var/cache/man/%LANG
%config(noreplace) /var/cache/man/%LANG/whatis
%_mandir/%LANG/man*
%attr(755,root,man)/var/catman/%LANG
%config(noreplace) %attr(755,root,root)/etc/cron.weekly/makewhatis-%LANG.cron

