%define LNG id

Summary:	Man pages in Indonesian language
Name:		man-pages-%{LNG}
Version:	0.1
Release:	20
License:	GPL
Group:		System/Internationalization
Source:		id-man.tar.bz2
BuildRequires:	man
Requires:	locales-%{LNG}
Requires:	man
Autoreq:	false
BuildArch:	noarch

%description
A collection of man pages for Linux in Indonesian language

%prep

%build

%install
rm -rf %{buildroot}
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
%defattr(644,root,man,755)
%dir %{_mandir}/%{LNG}
%dir /var/cache/man/%{LNG}
%ghost %config(noreplace) /var/cache/man/%{LNG}/whatis
%{_mandir}/%{LNG}/man*
%{_mandir{/%{LNG}/cat*
%{_mandir}/%{LNG}/CACHEDIR.TAG*
%{_mandir}/%{LNG}/index.db*
#%{_mandir}/%{LNG}/whatis*
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-18mdv2011.0
+ Revision: 666370
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-17mdv2011.0
+ Revision: 609322
- rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-16mdv2011.0
+ Revision: 609304
- fix build
- fix typos
- fix build
- rebuild
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.1-14mdv2009.1
+ Revision: 351577
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-13mdv2009.0
+ Revision: 223185
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1-12mdv2008.1
+ Revision: 152953
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1-11mdv2008.1
+ Revision: 152948
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.1-10mdv2008.0
+ Revision: 31270
- rebuild for new era; drop /var/catman (wildly obsolete)


* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.1-9mdk
- rebuild

* Mon Jan 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-8mdk
- build release

* Wed May 29 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-7mdk
- use new man-pages-LG template
    - don't rebuild whatis on install since
      - we've already build in package
      - cron will rebuild it nightly and so add other package french man pages
    - adapt to new man-pages-LG template
    - requires man => 1.5j-8mdk for new man-pages framework
    - remove old makewhatis.id since default makewhatis is now able to parse
      non english man pages
    - use new std makewhatis to build whatis in spec and in cron entry 
    - whatis db goes into /var/cache/man (so enable ro /usr)
    - standard {Build,}Requires/buildroot/prereq/arc/provides/obsoletes

* Thu Mar 07 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-6mdk
- fix permission on /usr/share/man/id/*
- provides manpages-%%LANG
- don't overwrite crontab if user altered it

* Tue May 01 2001 David BAUDENS <baudens@mandrakesoft.com> 0.1-5mdk
- Use %%_tmppath for BuildRoot

* Tue Jul 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-4mdk
- BM

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-3mdk
- use mandir macro in order to be ok when switching to /usr/share/man as
  following FHS.

* Tue Mar 28 2000 Denis Havlik <denis@mandrakesoft.com> 0.1-2mdk
- convert to new group scheme
- add "Prereq: sed grep man"

* Mon Dec 27 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- Initial Mandrake rpm version

