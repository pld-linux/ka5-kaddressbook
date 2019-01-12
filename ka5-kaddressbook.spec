%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kaddressbook
Summary:	KAddressbook
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3b9534aa71d03cb4cca0b58e1f92488f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.8.0
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-kdepim-apps-libs-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-prison-devel >= 5.51.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAddressBook stores all the personal details of your family, friends
and other contacts.

Features

• Imports and exports to nearly every address book standard • Reads
.vcf format files, and can import and export vCards and csv format
files • Can use multiple LDAPservers • Configurable filters and
powerful search capabilities • Integrates with other Kontact
components, e.g. exporting Birthday reminders to KOrganizer • Capable
of groupware integration • Powered by Akonadi

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kaddressbook.categories
/etc/xdg/kaddressbook.renamecategories
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %ghost %{_libdir}/libkaddressbookprivate.so.5
%attr(755,root,root) %{_libdir}/libkaddressbookprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbook_config_plugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbookpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_kaddressbookplugin.so
%{_desktopdir}/kaddressbook-importer.desktop
%{_desktopdir}/org.kde.kaddressbook.desktop
%{_iconsdir}/hicolor/128x128/apps/kaddressbook.png
%{_iconsdir}/hicolor/16x16/apps/kaddressbook.png
%{_iconsdir}/hicolor/22x22/apps/kaddressbook.png
%{_iconsdir}/hicolor/32x32/apps/kaddressbook.png
%{_iconsdir}/hicolor/48x48/apps/kaddressbook.png
%{_iconsdir}/hicolor/64x64/apps/kaddressbook.png
%{_iconsdir}/hicolor/scalable/apps/kaddressbook.svg
%{_datadir}/kaddressbook
%attr(755,root,root) %{_datadir}/kconf_update/kaddressbook-15.08-kickoff.sh
%{_datadir}/kconf_update/kaddressbook.upd
%{_datadir}/kontact/ksettingsdialog/kaddressbook.setdlg
%{_datadir}/kservices5/kaddressbook_config_plugins.desktop
%{_datadir}/kservices5/kaddressbookpart.desktop
%{_datadir}/kservices5/kontact/kaddressbookplugin.desktop
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
