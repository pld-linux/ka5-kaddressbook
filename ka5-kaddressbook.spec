#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kaddressbook
Summary:	KAddressbook
Name:		ka5-%{kaname}
Version:	22.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9817df0e5070d10093800888abfa296b
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
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-prison-devel >= %{kframever}
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

%description -l pl.UTF-8
KAddressBook potrafi zachować szczegóły osobiste Twojej rodziny,
przyjaciół i inne kontakty.

Właściwości

• Importuje i eksportuje do niemalże każdego standardu książki
adresowej • Czyta pliki formatu .vcf, może importować i eksportować
pliki vCards i csv. • Może używać wielu serwerów LDAP • Konfigurowalne
filtry i duże możliwości wyszukiwania • Integruje się z innymi
komponentami Kontact, np. eksportując przypomnienia o urodzinach do
KOrganizera • Możliwość integracji z groupware • "Napędzane" przez
Akonadi

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
%attr(755,root,root) %{_bindir}/kaddressbook
%ghost %{_libdir}/libkaddressbookprivate.so.5
%attr(755,root,root) %{_libdir}/libkaddressbookprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kaddressbookpart.so
%dir %{_libdir}/qt5/plugins/pim/kcms/kaddressbook
%{_libdir}/qt5/plugins/pim/kcms/kaddressbook/kaddressbook_config_plugins.so
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
%{_datadir}/kservices5/kaddressbook_config_plugins.desktop
%dir %{_datadir}/kservices5/kontact
%{_datadir}/kservices5/kontact/kaddressbookplugin.desktop
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_datadir}/qlogging-categories5/kaddressbook.categories
%{_datadir}/qlogging-categories5/kaddressbook.renamecategories
%ghost %{_libdir}/libKPimAddressbookImportExport.so.5
%attr(755,root,root) %{_libdir}/libKPimAddressbookImportExport.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact5/kontact_kaddressbookplugin.so
%{_desktopdir}/kaddressbook-view.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim/KAddressBookImportExport
%{_includedir}/KPim/kaddressbookimportexport
%{_includedir}/KPim/kaddressbookimportexport_version.h
%{_libdir}/cmake/KPimAddressbookImportExport
%{_libdir}/libKPimAddressbookImportExport.so
%{_libdir}/qt5/mkspecs/modules/qt_KAddressbookImportExport.pri
