#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Zlib
Summary:	Compress::Zlib - interface to zlib library
Summary(cs):	Compress::Zlib - modul poskytující rozhraní Perlu ke komprimaèní knihovnì zlib
Summary(da):	Compress::Zlib - et modul som giver Perl en grænseflade til komprimeringsbiblioteket zlib
Summary(de):	Compress::Zlib - ein Modul mit Perl-Interfaces zur zlib Komprimier-Bibliothek
Summary(es):	Compress::Zlib - módulo que proporciona las interfaces Perl para la librería de compresión
Summary(fr):	Compress::Zlib - module fournissant une interface Perl à la bibliothèque de compression zlib
Summary(it):	Compress::Zlib - modulo che fornisce interfacce di Perl alla libreria di compressione zlib
Summary(ja):	Compress::Zlib - zlib°µ½Ì¥é¥¤¥Ö¥é¥ê¤ØPerl ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òÄó¶¡¤¹¤ë¥â¥¸¥å¡¼¥ë¡£
Summary(ko):	Compress::Zlib - zlib ¾ÐÃà ¶óÀÌºê·¯¸®·ÎÀÇ Perl ÀÎÅÍÆäÀÌ½º¸¦ Á¦°øÇÏ´Â ¸ðµâ
Summary(pl):	Compress::Zlib - interfejs do biblioteki zlib
Summary(pt):	Compress::Zlib - um módulo que oferece interfaces em Perl para a biblioteca de compressão zlib
Summary(pt_BR):	Compress::Zlib - um módulo que oferece interfaces em Perl para a biblioteca de compressão zlib
Summary(sv):	Compress::Zlib - en modul som ger Perl ett gränssnitt till komprimeringsbiblioteket zlib
Summary(tr):	Compress::Zlib - zlib sýkýþtýrma kitaplýðýna Perl arayüzler saðlayan bir modül
Summary(zh_CN):	Compress::Zlib - Ìá¹©µ½ zlib Ñ¹Ëõ¿âµÄ Perl ½çÃæµÄÄ£¿é¡£
Summary(zh_TW):	Compress::Zlib - ´£¨Ñ Perl ¤¶­±µ¹ zlib À£ÁY¨ç¦¡®wªº¤@­Ó¼Ò²Õ¡C
Name:		perl-Compress-Zlib
Version:	1.33
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	927814da77b31b5a9ace821eb3ece5fd
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.

%description -l cs
Modul Compress::Zlib poskytuje rozhraní ke komprimaèní knihovnì v
Perlu. Vìt¹ina funkcí poskytovaných zlib je k dispozici v
Compress::Zlib.

Modul mù¾e být rozdìlen do dvou obecných oblastí funkènosti, konkrétnì
do komprese/dekomprese v pamìti a do ètení/zápisu souborù gzip.

%description -l da
Modulet Compress::Zlib giver Perl en grænseflade til
komprimeringsbiblioteket zlib. Det meste af funktionaliteten som
zlibgiver er tilgængelig i Compress::Zlib.

Modulet kan deles i to generelle funktionsområder, nemlig
komprimering/dekomprimering i hukommelsen og læsning/skrivning til
gzip-filer.

%description -l de
Das Compress::Zlib Modul enthält ein Perl-Interface zur zlib
Komprimier-Bibliothek. Die meisten Funktionen von zlib sind in
Compress::Zlib verfügbar.

Das Modul kann in zwei allgemeine Funktionsbereiche aufgeteilt werden:
Komprimieren/Dekomprimieren im Speicher und Lese-/Schreibzugriff für
gzip files.

%description -l es
El módulo Compress::Zlib proporciona una interfaz Perl para la
librería de compresión zlib. La mayoría de la funcionalidad
proporcionada por zlib está disponible en Compress::Zlib.

El módulo puede separarse en dos áreas generales de funcionalidad,
compresión/decompresión de memoria interna y acceso lectura/escritura
para los ficheros gzip.

%description -l fr
Le module Compress::Zlib fournit une interface Perl pour la
bibliothèque de compression zlib. La plupart des fonctionnalités
fournies par zlib est accessible dans Compress::Zlib.

Le module peut être divisé en deux zones de fonctionnalité distinctes:
compression/décompression dans la mémoire et accès en lecture/écriture
aux fichiers gzip.

%description -l it
Il modulo Compress::Zlib fornisce un'interfaccia Perl per la libreria
di compressione zlib Gran parte delle funzionalità fornite da zlib è
disponibile in Compress::Zlib.

Il modulo può essere diviso in due aree di funzionalità generali:
compressione/decompressione nella memoria e accesso in lettura/
scrittura ai file gzip.

%description -l ko
Compress::Zlib ¸ðµâÀº zlib ¾ÐÃà ¶óÀÌºê·¯¸®¿¡ Perl ÀÎÅÍÆäÀÌ½º¸¦
Á¦°øÇÕ´Ï´Ù. Compress::ZlibÀº zlibÀÌ Á¦°øÇÏ´Â ´ëºÎºÐÀÇ ±â´ÉÀ» °®Ãß°í
ÀÖ½À´Ï´Ù.

ÀÌ ¸ðµâÀº ÀÏ¹ÝÀûÀ¸·Î ´ÙÀ½°ú °°Àº µÎ°¡Áö ±â´ÉÀ» Á¦°øÇÕ´Ï´Ù: ¸Þ¸ð¸®
¾ÐÃà/ ¾ÐÃà ÇØÁ¦ ±â´É°ú gzip ÆÄÀÏ·ÎÀÇ ÀÐ±â/ ¾²±â Á¢±Ù ±â´É.


%description -l pl
Modu³ Compress::Zlib stanowi interfejs Perla do biblioteki zlib.
Wiêkszo¶æ funkcji biblioteki zlib jest dostêpna poprzez
Compress::Zlib.

Modu³ mo¿na podzieliæ funkcjonalnie na dwie zasadnicze cz±¶ci: do
kompresji/dekompresji w pamiêci oraz do dostêpu (odczyt i zapis) do
plików skompresowanych gzipem.

%description -l pt
O módulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compressão zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib está então disponível no Compress::Zlib.

O módulo pode ser dividido em duas áreas de funcionalidade geral,
nomeadamente na compressão/descompressão na memória e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l pt_BR
O módulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compressão zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib está então disponível no Compress::Zlib.

O módulo pode ser dividido em duas áreas de funcionalidade geral,
nomeadamente na compressão/descompressão na memória e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l sv
Modulen Compress::Zlib ger Perl ett gränssnitt till
komprimeringsbiblioteket zlib. Det mesta av funktionaliteten som
zlibger är åtkomlig i Compress::Zlib.

Modulen kan delas i två allmänna funktionsområden, nämligen
komprimering/dekomprimering i minnet och läsning/skrivning till
gzip-filer.

%description -l zh_CN
Compress::Zlib Ä£¿éÌá¹©ÁËµ½ zlib Ñ¹Ëõ¿âµÄ Perl ½çÃæ zlib
Ìá¹©µÄ¶àÊý¹¦ÄÜÔÚ Compress::Zlib ÖÐ¿ÉÓÃ¡£

¸ÃÄ£¿éµÄ¹¦ÄÜ¿ÉÒÔ±»·Ö³ÉÁ½Àà£¬¼´ÄÚ´æÄÚµÄÑ¹Ëõ/½âÑ¹ºÍ µ½ gzip
ÎÄ¼þµÄ¶ÁÐ´·ÃÎÊ¡£

%description -l zh_TW
Compress::Zlib ¼Ò²Õ¬° zlib À£ÁY¨ç¦¡®w´£¨Ñ¤@­Ó Perl ªº¤¶­±¡C ¥Ñ zlib
´£¨Ñªº¤j³¡¤À¥\¯à©Ê³£¥i¦b Compress::Zlib ¨ú±o¡C

³o­Ó¼Ò²Õ¥i¥H¤À³Î¬°¨â­Ó¤@¯ë¥\¯à©Êªº½d³ò¡A
ºÙ¬°°O¾ÐÅé¤¤ªºÀ£ÁY»P¸ÑÀ£ÁY¡A¥H¤ÎÅª¼g¦s¨ú gzip ÀÉ®×¡C

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"
rm -f examples/*.orig*

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
%doc README ANNOUNCE
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.bs
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
