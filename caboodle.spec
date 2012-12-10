%define debug_package %{nil}
Name:           caboodle
Version:        0.5
Release:        2
Summary:        Clone of the Flash game Planarity
License:        GPLv2
Group:          Games/Puzzles
URL:            http://juripakaste.fi/caboodle/
Source0:        http://www.juripakaste.fi/store/dl/caboodle/releases/caboodle-%{version}.tar.gz
Patch0:         caboodle-makefile.patch
Patch1:         caboodle-desktop.patch
BuildRequires:  ocaml-cairo-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  pkgconfig(gdk-2.0)
Requires:       gtk+2
BuildRequires:  pkgconfig(libglade-2.0)

%description
Caboodle is a clone of the Flash game Planarity for
the GNOME desktop.

The objective of the game is to arrange the balls on
the screen so that no lines cross.

Screen-shot:
http://juripakaste.fi/caboodle/Screenshot-Caboodle.png

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
make

%install
make install PREFIX=%{buildroot}%{_usr} REALPREFIX=%{_usr}

%files
%doc COPYING README NEWS
%{_gamesbindir}/caboodle
%{_datadir}/applications/caboodle.desktop
%{_datadir}/caboodle/





