Summary:	Wayfire Config Manager
Name:		wcm
Version:	0.9.0
Release:	4
License:	MIT
Group:		Applications
Source0:	https://github.com/WayfireWM/wcm/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5a2c98a93a14c6f43b2e8d76c2e09df3
URL:		https://wayfire.org/
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	gtkmm3-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libevdev-devel
BuildRequires:	libstdc++-devel >= 6:9
BuildRequires:	libxkbregistry-devel
BuildRequires:	libxml2-devel
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayfire-devel >= 0.9.0
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.17
BuildRequires:	wf-config >= 0.6.0
BuildRequires:	wf-shell-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	wf-config >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wayfire Config Manager is a Gtk3 application to configure wayfire. It
writes the config file that wayfire reads to update option values.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/wcm
%attr(755,root,root) %{_bindir}/wdisplays
%{_desktopdir}/network.cycles.wdisplays.desktop
%{_desktopdir}/wayfire-config-manager.desktop
%{_iconsdir}/hicolor/*x*/apps/wcm.png
%{_iconsdir}/hicolor/scalable/apps/network.cycles.wdisplays.svg
%{_datadir}/wayfire/icons/plugin-*.svg
%{_datadir}/wayfire/icons/wcm.png
