%define	pdir	Compress
%define	pnam	Zlib
%include	/usr/lib/rpm/macros.perl
Summary:	Compress-Zlib perl module
Summary(pl):	Modu³ perla Compress-Zlib
Name:		perl-Compress-Zlib
Version:	1.14
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress-Zlib - Interface to zlib library.

%description -l pl
Compress-Zlib - interfejs do biblioteki zlib.

%prep
%setup -q -n Compress-Zlib-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Compress/Zlib.pm
%dir %{perl_sitearch}/auto/Compress/Zlib
%{perl_sitearch}/auto/Compress/Zlib/Zlib.bs
%{perl_sitearch}/auto/Compress/Zlib/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Compress/Zlib/Zlib.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
