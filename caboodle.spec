%define debug_package %{nil}

Summary:	Clone of the Flash game Planarity
Name:		caboodle
Version:	0.5
Release:	3
License:	GPLv2+
Group:		Games/Puzzles
Url:		http://juripakaste.fi/caboodle/
Source0:	http://www.juripakaste.fi/store/dl/caboodle/releases/caboodle-%{version}.tar.gz
Patch0:		caboodle-makefile.patch
Patch1:		caboodle-desktop.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-cairo-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
Requires:	gtk+2

%description
Caboodle is a clone of the Flash game Planarity for the GNOME desktop.

The objective of the game is to arrange the balls on the screen so that
no lines cross.

%files
%doc COPYING README NEWS
%{_gamesbindir}/caboodle
%{_datadir}/applications/caboodle.desktop
%{_datadir}/caboodle/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
make

%install
make install PREFIX=%{buildroot}%{_usr} REALPREFIX=%{_usr}

