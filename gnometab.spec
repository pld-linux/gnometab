Summary:	Gnometab aims to be a WYSIWIG guitar tablature editor
Summary(pl):	Gnometab - edytor WYSIWYG do tabulatur gitarowych
Name:		gnometab
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.solutionm.com/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel
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

%description -l pl
Gnometab ma byæ edytorem WYSIWYG to tabulatur. Mo¿liwo¶ci Gnometaba
obejmuj± kopiowanie i wklejanie fragmentów tabulatur, bibliotekê
akordów (któr± u¿ytkownik musi wype³niæ akordami), profesjonalnie
wygl±daj±c± notacjê rytmu (jeszcze nie doskona³±), mo¿liwo¶æ tworzenia
ró¿nych symboli specyficznych dla gitary (podci±ganie, legato) oraz,
oczywi¶cie, czysto wygl±daj±ce wydruki w PostScripcie. Gnometab nie
próbuje byæ "m±dry", tzn. nie wie, ile uderzeñ jest takcie, ani jak
zrobiæ akord E z Am. Zamiast tego nacisk zosta³ po³o¿ony na wygl±d
wyj¶cia.

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
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/gnometab
%{_pixmapsdir}/*
%{_desktopdir}/gnometab.desktop
%{_sysconfdir}/gconf/schemas/gnometab.schemas
