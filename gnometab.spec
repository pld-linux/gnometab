
Summary:	Gnometab aims to be a WYSIWIG guitar tablature editor.
Name:		gnometab
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.solutionm.com/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libxml2-devel
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
rm -rf $RPM_BUILD_ROOT/%{_prefix}/doc

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
