#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdg-user-dirs-gtk
Version  : 0.10
Release  : 13
URL      : https://download.gnome.org/sources/xdg-user-dirs-gtk/0.10/xdg-user-dirs-gtk-0.10.tar.xz
Source0  : https://download.gnome.org/sources/xdg-user-dirs-gtk/0.10/xdg-user-dirs-gtk-0.10.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xdg-user-dirs-gtk-bin = %{version}-%{release}
Requires: xdg-user-dirs-gtk-data = %{version}-%{release}
Requires: xdg-user-dirs-gtk-license = %{version}-%{release}
Requires: xdg-user-dirs-gtk-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
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
Requires: xdg-user-dirs-gtk-data = %{version}-%{release}
Requires: xdg-user-dirs-gtk-license = %{version}-%{release}

%description bin
bin components for the xdg-user-dirs-gtk package.


%package data
Summary: data components for the xdg-user-dirs-gtk package.
Group: Data

%description data
data components for the xdg-user-dirs-gtk package.


%package license
Summary: license components for the xdg-user-dirs-gtk package.
Group: Default

%description license
license components for the xdg-user-dirs-gtk package.


%package locales
Summary: locales components for the xdg-user-dirs-gtk package.
Group: Default

%description locales
locales components for the xdg-user-dirs-gtk package.


%prep
%setup -q -n xdg-user-dirs-gtk-0.10
cd %{_builddir}/xdg-user-dirs-gtk-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664163729
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664163729
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-user-dirs-gtk
cp %{_builddir}/xdg-user-dirs-gtk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xdg-user-dirs-gtk/dfac199a7539a404407098a2541b9482279f690d || :
%make_install
%find_lang xdg-user-dirs-gtk
## install_append content
mv %{buildroot}/etc/xdg %{buildroot}/usr/share/. && rmdir %{buildroot}/etc

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xdg-user-dirs-gtk-update

%files data
%defattr(-,root,root,-)
/usr/share/xdg/autostart/user-dirs-update-gtk.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-user-dirs-gtk/dfac199a7539a404407098a2541b9482279f690d

%files locales -f xdg-user-dirs-gtk.lang
%defattr(-,root,root,-)

