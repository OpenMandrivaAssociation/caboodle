Name:           caboodle
Version:        0.5
Release:        %mkrel 1
Summary:        Clone of the Flash game Planarity
License:        GNU/GPL>=2
Group:          Games/Puzzles
URL:            http://juripakaste.fi/caboodle/
Source0:        http://www.juripakaste.fi/store/dl/caboodle/releases/caboodle-%{version}.tar.gz
Patch0:         caboodle-makefile.patch
Patch1:         caboodle-desktop.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-cairo-devel
BuildRequires:  cairo-devel
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  gtk+2-devel
Requires:       gtk+2
BuildRequires:  libglade2-devel

%description
Caboodle is a clone of the Flash game Planarity for
the GNOME desktop.

The objective of the game is to arrange the balls on
the screen so that no lines cross.

Screenshot:
http://juripakaste.fi/caboodle/Screenshot-Caboodle.png

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
make

%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}/%{_usr} REALPREFIX=%{_usr}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README NEWS
%{_gamesbindir}/caboodle
%{_datadir}/applications/caboodle.desktop
%{_datadir}/caboodle/
%{_datadir}/caboodle/caboodle.glade
%{_datadir}/caboodle/caboodle.svg

