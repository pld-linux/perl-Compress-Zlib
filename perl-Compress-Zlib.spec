#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Zlib
Summary:	Compress::Zlib - interface to zlib library
Summary(pl):	Compress::Zlib - interfejs do biblioteki zlib
Name:		perl-Compress-Zlib
Version:	1.20
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.8.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.

%description -l pl
Modu³ Compress::Zlib stanowi interfejs Perla do biblioteki zlib.
Wiêkszo¶æ funkcji biblioteki zlib jest dostêpna poprzez
Compress::Zlib.

Modu³ mo¿na podzieliæ funkcjonalnie na dwie zasadnicze cz±¶ci: do
kompresji/dekompresji w pamiêci oraz do dostêpu (odczyt i zapis) do
plików skompresowanych gzipem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"
rm -f examples/*.orig*

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ANNOUNCE
%{perl_vendorarch}/Compress/Zlib.pm
%dir %{perl_vendorarch}/auto/Compress/Zlib
%{perl_vendorarch}/auto/Compress/Zlib/Zlib.bs
%{perl_vendorarch}/auto/Compress/Zlib/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Zlib/Zlib.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
