#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Zlib
Summary:	Compress::Zlib - interface to zlib library
Summary(cs):	Compress::Zlib - modul poskytuj�c� rozhran� Perlu ke komprima�n� knihovn� zlib
Summary(da):	Compress::Zlib - et modul som giver Perl en gr�nseflade til komprimeringsbiblioteket zlib
Summary(de):	Compress::Zlib - ein Modul mit Perl-Interfaces zur zlib Komprimier-Bibliothek
Summary(es):	Compress::Zlib - m�dulo que proporciona las interfaces Perl para la librer�a de compresi�n
Summary(fr):	Compress::Zlib - module fournissant une interface Perl � la biblioth�que de compression zlib
Summary(it):	Compress::Zlib - modulo che fornisce interfacce di Perl alla libreria di compressione zlib
Summary(ja):	Compress::Zlib - zlib���̥饤�֥���Perl ���󥿡��ե��������󶡤���⥸�塼�롣
Summary(ko):	Compress::Zlib - zlib ���� ���̺귯������ Perl �������̽��� �����ϴ� ���
Summary(pl):	Compress::Zlib - interfejs do biblioteki zlib
Summary(pt):	Compress::Zlib - um m�dulo que oferece interfaces em Perl para a biblioteca de compress�o zlib
Summary(pt_BR):	Compress::Zlib - um m�dulo que oferece interfaces em Perl para a biblioteca de compress�o zlib
Summary(sv):	Compress::Zlib - en modul som ger Perl ett gr�nssnitt till komprimeringsbiblioteket zlib
Summary(tr):	Compress::Zlib - zlib s�k��t�rma kitapl���na Perl aray�zler sa�layan bir mod�l
Summary(zh_CN):	Compress::Zlib - �ṩ�� zlib ѹ����� Perl �����ģ�顣
Summary(zh_TW):	Compress::Zlib - ���� Perl ������ zlib ���Y�禡�w���@�ӼҲաC
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
Modul Compress::Zlib poskytuje rozhran� ke komprima�n� knihovn� v
Perlu. V�t�ina funkc� poskytovan�ch zlib je k dispozici v
Compress::Zlib.

Modul m��e b�t rozd�len do dvou obecn�ch oblast� funk�nosti, konkr�tn�
do komprese/dekomprese v pam�ti a do �ten�/z�pisu soubor� gzip.

%description -l da
Modulet Compress::Zlib giver Perl en gr�nseflade til
komprimeringsbiblioteket zlib. Det meste af funktionaliteten som
zlibgiver er tilg�ngelig i Compress::Zlib.

Modulet kan deles i to generelle funktionsomr�der, nemlig
komprimering/dekomprimering i hukommelsen og l�sning/skrivning til
gzip-filer.

%description -l de
Das Compress::Zlib Modul enth�lt ein Perl-Interface zur zlib
Komprimier-Bibliothek. Die meisten Funktionen von zlib sind in
Compress::Zlib verf�gbar.

Das Modul kann in zwei allgemeine Funktionsbereiche aufgeteilt werden:
Komprimieren/Dekomprimieren im Speicher und Lese-/Schreibzugriff f�r
gzip files.

%description -l es
El m�dulo Compress::Zlib proporciona una interfaz Perl para la
librer�a de compresi�n zlib. La mayor�a de la funcionalidad
proporcionada por zlib est� disponible en Compress::Zlib.

El m�dulo puede separarse en dos �reas generales de funcionalidad,
compresi�n/decompresi�n de memoria interna y acceso lectura/escritura
para los ficheros gzip.

%description -l fr
Le module Compress::Zlib fournit une interface Perl pour la
biblioth�que de compression zlib. La plupart des fonctionnalit�s
fournies par zlib est accessible dans Compress::Zlib.

Le module peut �tre divis� en deux zones de fonctionnalit� distinctes:
compression/d�compression dans la m�moire et acc�s en lecture/�criture
aux fichiers gzip.

%description -l it
Il modulo Compress::Zlib fornisce un'interfaccia Perl per la libreria
di compressione zlib Gran parte delle funzionalit� fornite da zlib �
disponibile in Compress::Zlib.

Il modulo pu� essere diviso in due aree di funzionalit� generali:
compressione/decompressione nella memoria e accesso in lettura/
scrittura ai file gzip.

%description -l ko
Compress::Zlib ����� zlib ���� ���̺귯���� Perl �������̽���
�����մϴ�. Compress::Zlib�� zlib�� �����ϴ� ��κ��� ����� ���߰�
�ֽ��ϴ�.

�� ����� �Ϲ������� ������ ���� �ΰ��� ����� �����մϴ�: �޸�
����/ ���� ���� ��ɰ� gzip ���Ϸ��� �б�/ ���� ���� ���.


%description -l pl
Modu� Compress::Zlib stanowi interfejs Perla do biblioteki zlib.
Wi�kszo�� funkcji biblioteki zlib jest dost�pna poprzez
Compress::Zlib.

Modu� mo�na podzieli� funkcjonalnie na dwie zasadnicze cz��ci: do
kompresji/dekompresji w pami�ci oraz do dost�pu (odczyt i zapis) do
plik�w skompresowanych gzipem.

%description -l pt
O m�dulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compress�o zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib est� ent�o dispon�vel no Compress::Zlib.

O m�dulo pode ser dividido em duas �reas de funcionalidade geral,
nomeadamente na compress�o/descompress�o na mem�ria e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l pt_BR
O m�dulo Compress::Zlib oferece uma interface de Perl para a
biblioteca de compress�o zlib (veja o /AUTHOR para mais detalhes de
como obter a zlib). A maior parte da funcionalidade oferecida pela
zlib est� ent�o dispon�vel no Compress::Zlib.

O m�dulo pode ser dividido em duas �reas de funcionalidade geral,
nomeadamente na compress�o/descompress�o na mem�ria e no acesso para
leitura/escrita nos ficheiros do 'gzip'.

%description -l sv
Modulen Compress::Zlib ger Perl ett gr�nssnitt till
komprimeringsbiblioteket zlib. Det mesta av funktionaliteten som
zlibger �r �tkomlig i Compress::Zlib.

Modulen kan delas i tv� allm�nna funktionsomr�den, n�mligen
komprimering/dekomprimering i minnet och l�sning/skrivning till
gzip-filer.

%description -l zh_CN
Compress::Zlib ģ���ṩ�˵� zlib ѹ����� Perl ���� zlib
�ṩ�Ķ��������� Compress::Zlib �п��á�

��ģ��Ĺ��ܿ��Ա��ֳ����࣬���ڴ��ڵ�ѹ��/��ѹ�� �� gzip
�ļ��Ķ�д���ʡ�

%description -l zh_TW
Compress::Zlib �Ҳլ� zlib ���Y�禡�w���Ѥ@�� Perl �������C �� zlib
���Ѫ��j�����\��ʳ��i�b Compress::Zlib ���o�C

�o�ӼҲեi�H���ά���Ӥ@��\��ʪ��d��A
�٬��O���餤�����Y�P�����Y�A�H��Ū�g�s�� gzip �ɮסC

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
