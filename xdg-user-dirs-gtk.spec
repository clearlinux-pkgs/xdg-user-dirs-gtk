#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdg-user-dirs-gtk
Version  : 0.10
Release  : 1
URL      : http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/0.10/xdg-user-dirs-gtk-0.10.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/0.10/xdg-user-dirs-gtk-0.10.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xdg-user-dirs-gtk-bin
Requires: xdg-user-dirs-gtk-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : xdg-user-dirs

%description
xdg-user-dirs-gtk is a companion to xdg-user-dirs that integrates it into
the Gnome desktop and Gtk+ applications.

%package bin
Summary: bin components for the xdg-user-dirs-gtk package.
Group: Binaries

%description bin
bin components for the xdg-user-dirs-gtk package.


%package locales
Summary: locales components for the xdg-user-dirs-gtk package.
Group: Default

%description locales
locales components for the xdg-user-dirs-gtk package.


%prep
%setup -q -n xdg-user-dirs-gtk-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492797135
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492797135
rm -rf %{buildroot}
%make_install
%find_lang xdg-user-dirs-gtk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xdg-user-dirs-gtk-update

%files locales -f xdg-user-dirs-gtk.lang
%defattr(-,root,root,-)

