%include	/usr/lib/rpm/macros.perl
Summary:	Compress-Zlib perl module
Summary(pl):	Modu³ perla Compress-Zlib
Name:		perl-Compress-Zlib
Version:	1.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Compress/Compress-Zlib-%{version}.tar.gz
Patch:		perl-Compress-Zlib-paths.patch
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-13
BuildRequires:	zlib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Compress-Zlib - Interface to zlib library.

%description -l pl
Compress-Zlib - interfejs do biblioteki zlib.

%prep
%setup -q -n Compress-Zlib-%{version}
%patch -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

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

/usr/src/examples/%{name}-%{version}
