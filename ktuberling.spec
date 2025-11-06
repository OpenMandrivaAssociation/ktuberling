#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
# Workaround for problem with debugsource generation
%global _empty_manifest_terminate_build 0

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ktuberling
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
Summary:	"Potato editor" game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/ktuberling/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/ktuberling/-/archive/%{gitbranch}/ktuberling-%{gitbranchd}.tar.bz2#/ktuberling-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ktuberling-%{version}.tar.xz
%endif
BuildRequires:	cmake ninja cmake(ECM)
BuildRequires: 	cmake(KDEGames6)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Completion) cmake(KF6Config) cmake(KF6ConfigWidgets) cmake(KF6CoreAddons) cmake(KF6Crash) cmake(KF6DBusAddons) cmake(KF6I18n) cmake(KF6WidgetsAddons) cmake(KF6XmlGui) cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6PrintSupport) cmake(Qt6Svg) cmake(Qt6Widgets) cmake(Qt6Xml) cmake(Phonon4Qt6) cmake(Qt6Multimedia) cmake(KF6KIO) cmake(KF6DocTools)

%rename plasma6-ktuberling

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KTuberling is a "potato editor" game intended for small children and adults
who remain young at heart. The game has no winner; the only purpose is to
make the funniest faces you can.

%files -f %{name}.lang
%{_bindir}/ktuberling
%{_datadir}/applications/org.kde.ktuberling.desktop
%{_datadir}/ktuberling/pics/*.theme
%{_datadir}/ktuberling/pics/*.desktop
%{_datadir}/ktuberling/pics/*.svgz
%{_datadir}/ktuberling/pics/*.svg
%{_iconsdir}/hicolor/*/apps/ktuberling.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png
%{_datadir}/ktuberling/sounds/en.soundtheme
%{_datadir}/ktuberling/sounds/en/*.ogg
%{_datadir}/metainfo/org.kde.ktuberling.appdata.xml
%{_datadir}/qlogging-categories6/ktuberling.renamecategories
%{_datadir}/qlogging-categories6/ktuberling.categories
%lang(ca) %{_datadir}/ktuberling/sounds/ca.soundtheme
%lang(ca) %{_datadir}/ktuberling/sounds/ca
%lang(da) %{_datadir}/ktuberling/sounds/da.soundtheme
%lang(da) %{_datadir}/ktuberling/sounds/da
%lang(de) %{_datadir}/ktuberling/sounds/de.soundtheme
%lang(de) %{_datadir}/ktuberling/sounds/de
%lang(el) %{_datadir}/ktuberling/sounds/el.soundtheme
%lang(el) %{_datadir}/ktuberling/sounds/el
%lang(es) %{_datadir}/ktuberling/sounds/es.soundtheme
%lang(es) %{_datadir}/ktuberling/sounds/es
%lang(eo) %{_datadir}/ktuberling/sounds/eo.soundtheme
%lang(eo) %{_datadir}/ktuberling/sounds/eo
%lang(fi) %{_datadir}/ktuberling/sounds/fi.soundtheme
%lang(fi) %{_datadir}/ktuberling/sounds/fi
%lang(fr) %{_datadir}/ktuberling/sounds/fr.soundtheme
%lang(fr) %{_datadir}/ktuberling/sounds/fr
%lang(ga) %{_datadir}/ktuberling/sounds/ga.soundtheme
%lang(ga) %{_datadir}/ktuberling/sounds/ga
%lang(gl) %{_datadir}/ktuberling/sounds/gl.soundtheme
%lang(gl) %{_datadir}/ktuberling/sounds/gl
%lang(id) %{_datadir}/ktuberling/sounds/id.soundtheme
%lang(id) %{_datadir}/ktuberling/sounds/id
%lang(it) %{_datadir}/ktuberling/sounds/it.soundtheme
%lang(it) %{_datadir}/ktuberling/sounds/it
%lang(lt) %{_datadir}/ktuberling/sounds/lt.soundtheme
%lang(lt) %{_datadir}/ktuberling/sounds/lt
%lang(nds) %{_datadir}/ktuberling/sounds/nds.soundtheme
%lang(nds) %{_datadir}/ktuberling/sounds/nds
%lang(nl) %{_datadir}/ktuberling/sounds/nl.soundtheme
%lang(nl) %{_datadir}/ktuberling/sounds/nl
%lang(nn) %{_datadir}/ktuberling/sounds/nn.soundtheme
%lang(nn) %{_datadir}/ktuberling/sounds/nn
%lang(pt) %{_datadir}/ktuberling/sounds/pt.soundtheme
%lang(pt) %{_datadir}/ktuberling/sounds/pt
%lang(ro) %{_datadir}/ktuberling/sounds/ro.soundtheme
%lang(ro) %{_datadir}/ktuberling/sounds/ro
%lang(ru) %{_datadir}/ktuberling/sounds/ru.soundtheme
%lang(ru) %{_datadir}/ktuberling/sounds/ru
%lang(sl) %{_datadir}/ktuberling/sounds/sl.soundtheme
%lang(sl) %{_datadir}/ktuberling/sounds/sl
%lang(sr) %{_datadir}/ktuberling/sounds/sr
%lang(sr) %{_datadir}/ktuberling/sounds/sr.soundtheme
%lang(sr@ijekavian) %{_datadir}/ktuberling/sounds/sr@ijekavian
%lang(sr@ijekavian) %{_datadir}/ktuberling/sounds/sr@ijekavian.soundtheme
%lang(sr@ijekavianlatin) %{_datadir}/ktuberling/sounds/sr@ijekavianlatin
%lang(sr@ijekavianlatin) %{_datadir}/ktuberling/sounds/sr@ijekavianlatin.soundtheme
%lang(sr@latin) %{_datadir}/ktuberling/sounds/sr@latin
%lang(sr@latin) %{_datadir}/ktuberling/sounds/sr@latin.soundtheme
%lang(sv) %{_datadir}/ktuberling/sounds/sv.soundtheme
%lang(sv) %{_datadir}/ktuberling/sounds/sv
%lang(uk) %{_datadir}/ktuberling/sounds/uk.soundtheme
%lang(uk) %{_datadir}/ktuberling/sounds/uk
%lang(wa) %{_datadir}/ktuberling/sounds/wa.soundtheme
%lang(wa) %{_datadir}/ktuberling/sounds/wa
