#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	Zlib
Summary:	Compress::Zlib - interface to zlib library
Summary(cs.UTF-8):	Compress::Zlib - modul poskytující rozhraní Perlu ke komprimační knihovně zlib
Summary(da.UTF-8):	Compress::Zlib - et modul som giver Perl en grænseflade til komprimeringsbiblioteket zlib
Summary(de.UTF-8):	Compress::Zlib - ein Modul mit Perl-Interfaces zur zlib Komprimier-Bibliothek
Summary(es.UTF-8):	Compress::Zlib - módulo que proporciona las interfaces Perl para la librería de compresión
Summary(fr.UTF-8):	Compress::Zlib - module fournissant une interface Perl à la bibliothèque de compression zlib
Summary(it.UTF-8):	Compress::Zlib - modulo che fornisce interfacce di Perl alla libreria di compressione zlib
Summary(ja.UTF-8):	Compress::Zlib - zlib圧縮ライブラリへPerl インターフェイスを提供するモジュール。
Summary(ko.UTF-8):	Compress::Zlib - zlib 압축 라이브러리로의 Perl 인터페이스를 제공하는 모듈
Summary(pl.UTF-8):	Compress::Zlib - interfejs do biblioteki zlib
Summary(pt.UTF-8):	Compress::Zlib - um módulo que oferece interfaces em Perl para a biblioteca de compressão zlib
Summary(pt_BR.UTF-8):	Compress::Zlib - um módulo que oferece interfaces em Perl para a biblioteca de compressão zlib
Summary(sv.UTF-8):	Compress::Zlib - en modul som ger Perl ett gränssnitt till komprimeringsbiblioteket zlib
Summary(tr.UTF-8):	Compress::Zlib - zlib sıkıştırma kitaplığına Perl arayüzler sağlayan bir modül
Summary(zh_CN.UTF-8):	Compress::Zlib - 提供到 zlib 压缩库的 Perl 界面的模块。
Summary(zh_TW.UTF-8):	Compress::Zlib - 提供 Perl 介面給 zlib 壓縮函式庫的一個模組。
Name:		perl-Compress-Zlib
Version:	2.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ea7837294a3a434c1266c7e9862c4360
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Compress-Zlib/
%if %{with tests}
BuildRequires:	perl-Compress-Raw-Zlib >= %{version}
BuildRequires:	perl-IO-Compress-Base >= %{version}
BuildRequires:	perl-IO-Compress-Zlib >= %{version}
BuildRequires:	perl-Scalar-List-Utils
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.

%description -l cs.UTF-8
Modul Compress::Zlib poskytuje rozhraní ke komprimační knihovně v
Perlu. Většina funkcí poskytovaných zlib je k dispozici v
Compress::Zlib.

Modul může být rozdělen do dvou obecných oblastí funkčnosti, konkrétně
do komprese/dekomprese v paměti a do čtení/zápisu souborů gzip.

%description -l da.UTF-8
Modulet Compress::Zlib giver Perl en grænseflade til
komprimeringsbiblioteket zlib. Det meste af funktionaliteten som
zlibgiver er tilgængelig i Compress::Zlib.

Modulet kan deles i to generelle funktionsområder, nemlig
komprimering/dekomprimering i hukommelsen og læsning/skrivning til
gzip-filer.

%description -l de.UTF-8
Das Compress::Zlib Modul enthält ein Perl-Interface zur zlib
Komprimier-Bibliothek. Die meisten Funktionen von zlib sind in
Compress::Zlib verfügbar.

Das Modul kann in zwei allgemeine Funktionsbereiche aufgeteilt werden:
Komprimieren/Dekomprimieren im Speicher und Lese-/Schreibzugriff für
gzip files.

%description -l es.UTF-8
El módulo Compress::Zlib proporciona una interfaz Perl para la
librería de compresión zlib. La mayoría de la funcionalidad
proporcionada por zlib está disponible en Compress::Zlib.

El módulo puede separarse en dos áreas generales de funcionalidad,
compresión/decompresión de memoria interna y acceso lectura/escritura
para los ficheros gzip.

%description -l fr.UTF-8
Le module Compress::Zlib fournit une interface Perl pour la
bibliothèque de compression zlib. La plupart des fonctionnalités
fournies par zlib est accessible dans Compress::Zlib.

Le module peut être divisé en deux zones de fonctionnalité distinctes:
compression/décompression dans la mémoire et accès en lecture/écriture
aux fichiers gzip.

%description -l it.UTF-8
Il modulo Compress::Zlib fornisce un'interfaccia Perl per la libreria
di compressione zlib Gran parte delle funzionalità fornite da zlib è
disponibile in Compress::Zlib.

Il modulo può essere diviso in due aree di funzionalità generali:
compressione/decompressione nella memoria e accesso in lettura/
scrittura ai file gzip.

%description -l ko.UTF-8
Compress::Zlib 모듈은 zlib 압축 라이브러리에 Perl 인터페이스를
제공합니다. Compress::Zlib은 zlib이 제공하는 대부분의 기능을 갖추고
있습니다.

이 모듈은 일반적으로 다음과 같은 두가지 기능을 제공합니다: 메모리
압축/ 압축 해제 기능과 gzip 파일로의 읽기/ 쓰기 접근 기능.

%description -l pl.UTF-8
Moduł Compress::Zlib stanowi interfejs Perla do biblioteki zlib.
Większość funkcji biblioteki zlib jest dostępna poprzez
Compress::Zlib.

Moduł można podzielić funkcjonalnie na dwie zasadnicze części: do
kompresji/dekompresji w pamięci oraz do dostępu (odczyt i zapis) do
plików skompresowanych gzipem.

%description -l pt.UTF-8
O módulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compressão zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib está então disponível no Compress::Zlib.

O módulo pode ser dividido em duas áreas de funcionalidade geral,
nomeadamente na compressão/descompressão na memória e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l pt_BR.UTF-8
O módulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compressão zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib está então disponível no Compress::Zlib.

O módulo pode ser dividido em duas áreas de funcionalidade geral,
nomeadamente na compressão/descompressão na memória e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l sv.UTF-8
Modulen Compress::Zlib ger Perl ett gränssnitt till
komprimeringsbiblioteket zlib. Det mesta av funktionaliteten som
zlibger är åtkomlig i Compress::Zlib.

Modulen kan delas i två allmänna funktionsområden, nämligen
komprimering/dekomprimering i minnet och läsning/skrivning till
gzip-filer.

%description -l zh_CN.UTF-8
Compress::Zlib 模块提供了到 zlib 压缩库的 Perl 界面 zlib
提供的多数功能在 Compress::Zlib 中可用。

该模块的功能可以被分成两类，即内存内的压缩/解压和 到 gzip
文件的读写访问。

%description -l zh_TW.UTF-8
Compress::Zlib 模組為 zlib 壓縮函式庫提供一個 Perl 的介面。 由 zlib
提供的大部分功能性都可在 Compress::Zlib 取得。

這個模組可以分割為兩個一般功能性的範圍，
稱為記憶體中的壓縮與解壓縮，以及讀寫存取 gzip 檔案。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

rm -f examples/*.orig*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Compress/Zlib.pm
%dir %{perl_vendorlib}/auto/Compress/Zlib
%{perl_vendorlib}/auto/Compress/Zlib/autosplit.ix
%{_mandir}/man3/Compress::Zlib.3*
%{_examplesdir}/%{name}-%{version}
