%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Zlib
Summary:	Compress::Zlib perl module
Summary(es):	Modulo Perl Compress::Zlib
Summary(pl):	Modu³ perla Compress::Zlib
Summary(pt_BR):	Modulo Perl Compress::Zlib
Name:		perl-Compress-Zlib
Version:	1.19
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::Zlib - Interface to zlib library.

%description -l pl
Compress::Zlib - interfejs do biblioteki zlib.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"
rm -f examples/*.orig*

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
