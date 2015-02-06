Summary:	XML data compression program
Name:		xmlppm
Version:	0.98.2
Release:	9
URL:		http://sourceforge.net/projects/xmlppm
License:	GPL
Group:		File tools
Source:		http://prdownloads.sourceforge.net/xmlppm/%{name}-%{version}-src.tar.bz2
Patch:		%{name}-0.98.2.gcc4.patch
BuildRequires:	expat-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
XMLPPM is a data compression program that compresses XML files from 5 to
30% better than any existing text or XML-specific compressors. It is a
combination of the well-known Prediction by Partial Match (PPM)
algorithm for text compression, first described by Cleary and Witten in
1984, and an approach to modeling tree-structured data called
Multiplexed Hierarchical Modeling (MHM) developed by James Cheney.
XMLPPM source code is part of a project at Sourceforge on XML
compression.

%prep
%setup
%patch -p 1 -b fix-gcc4-build

%build
cd src
%make OPT_FLAGS="%{optflags}"

%install
rm -rf %{buildroot}
cd src
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 xmlppm xmlunppm %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.98.2-8mdv2010.0
+ Revision: 435151
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.98.2-7mdv2009.0
+ Revision: 262461
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.98.2-6mdv2009.0
+ Revision: 257166
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.98.2-4mdv2008.1
+ Revision: 140966
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.98.2-4mdv2008.0
+ Revision: 38611
- fix mixture of tabs and spaces
- rebuild for expat
- Import xmlppm



* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.2-3mdv2007.0
- Rebuild

* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.2-2mdk
- fix build

* Sat May 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.98.2-1mdk
- New release 0.98.2
- spec cleanup

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.98.1-1mdk 
- new version

* Wed Jun  9 2004 Guillaume Rousse <guillomovitch@mandrakesoft.com> 0.98-1mdk
- New release 0.98
- dropped patch0

* Fri Jun 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.97-1mdk 
- new version
- new url
- rpmbuildupdate aware

* Sat Dec 05 2003 Franck Villaume <fvill@freesurf.fr> 0.96-2mdk
- add real support to RPM_OPT_FLAGS
- modify BuildRequires to get 64bits support

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.96-1mdk
- 0.96 

* Mon Oct 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.95-3mdk
- fix group

* Wed Mar 13 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.95-2mdk
- fixed 1st person description (Levi Ramsey <lramsey@student.umass.edu>)
- mdk optimisations

* Wed Mar 13 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 0.95-1mdk
- first mdk release
