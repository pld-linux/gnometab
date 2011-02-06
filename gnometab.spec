Summary:	Gnometab aims to be a WYSIWIG guitar tablature editor
Summary(pl.UTF-8):	Gnometab - edytor WYSIWYG do tabulatur gitarowych
Name:		gnometab
Version:	0.7.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.solutionm.com/gnometab/%{name}-%{version}.tar.gz
# Source0-md5:	63cf945a16a4dbf2bc240dff99354114
Patch0:		%{name}-desktop.patch
URL:		http://www.solutionm.com/gnometab/gnometab.html
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnometab aims to be a WYSIWYG (what you see is what you get) tablature
editor. Gnometab's features include copying and pasting of tablature
passages, a chord library (which the user must fill with chords),
professional-looking rhythm notation (not perfect yet), the ability to
create a variety of tablature symbols specific to the guitar -- bends,
slurs (hammer-ons, pull-offs, etc.), etc. -- and, of course,
clean-looking printed output, given any postscript-compatible printer.
Gnometab does not attempt to be "smart", i.e., it does not know how
many beats are in a measure, nor does it know an E chord from an Am
chord. Instead, the emphasis has been on the appearance of the output.

%description -l pl.UTF-8
Gnometab ma być edytorem WYSIWYG to tabulatur. Możliwości Gnometaba
obejmują kopiowanie i wklejanie fragmentów tabulatur, bibliotekę
akordów (którą użytkownik musi wypełnić akordami), profesjonalnie
wyglądającą notację rytmu (jeszcze nie doskonałą), możliwość tworzenia
różnych symboli specyficznych dla gitary (podciąganie, legato) oraz,
oczywiście, czysto wyglądające wydruki w PostScripcie. Gnometab nie
próbuje być "mądry", tzn. nie wie, ile uderzeń jest takcie, ani jak
zrobić akord E z Am. Zamiast tego nacisk został położony na wygląd
wyjścia.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#remove uneeded docs (installed via %doc)
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/gnometab
%{_pixmapsdir}/*
%{_desktopdir}/gnometab.desktop
%{_sysconfdir}/gconf/schemas/gnometab.schemas
