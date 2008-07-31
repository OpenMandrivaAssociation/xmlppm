Summary:	XML data compression program
Name:		xmlppm
Version:	0.98.2
Release:	%mkrel 6
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
