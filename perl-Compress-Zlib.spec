%include	/usr/lib/rpm/macros.perl
Summary:	Compress-Zlib perl module
Summary(pl):	Modu³ perla Compress-Zlib
Name:		perl-Compress-Zlib
Version:	1.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Compress/Compress-Zlib-%{version}.tar.gz
Patch0:		perl-Compress-Zlib-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	zlib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
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
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Compress/Zlib/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Compress/Zlib
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ANNOUNCE}.gz

%{perl_sitearch}/Compress/Zlib.pm

%dir %{perl_sitearch}/auto/Compress/Zlib
%{perl_sitearch}/auto/Compress/Zlib/.packlist
%{perl_sitearch}/auto/Compress/Zlib/Zlib.bs
%{perl_sitearch}/auto/Compress/Zlib/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Compress/Zlib/Zlib.so

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
