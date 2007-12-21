%define name	google-apps-installer
%define version	0.4
%define release %mkrel 2

Summary:	Desktop links to install Google apps
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Other
URL:		http://www.mandrivalinux.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	wget gurpmi  
Buildarch:	noarch

%description
This is an icon for the default PWP desktop, used to install GoogleEarth and Picasa.

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 0755 %buildroot/%_datadir/applications/

cat > %buildroot/%_datadir/applications/googleearthinstall.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Icon=mandrake
Name=Google Earth Install
Type=Application
Terminal=true
Exec=sh -c "wget http://api.mandriva.com/3rd-party/200800/downloadURL/GoogleEarth -O GoogleEarthLinux.bin && sh +x GoogleEarthLinux.bin"
Categories=X-MandrivaLinux-Internet;X-MandrivaLinux-CrossDesktop;
EOF

cat > %buildroot/%_datadir/applications/googlepicasainstall.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Icon=mandrake
Name=Google Picasa Install
Type=Application
Terminal=true
Exec=sh -c "wget http://api.mandriva.com/3rd-party/200800/downloadURL/GooglePicasa -O GooglePicasa.rpm && gurpmi GooglePicasa.rpm"
Categories=X-MandrivaLinux-Multimedia-Graphics;X-MandrivaLinux-CrossDesktop;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_datadir/applications/*


%changelog
* Fri Sep 21 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.4-2mdv2008.0
- restore Picasa  (missing agreement)

* Tue Sep 18 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.4-1mdv2008.0
- remove picasa
- fix menu
- update URL

* Fri Mar 30 2007 Lenny Cartier <lenny@mandriva.com> 0.3-2mdv2007.1
+ Revision: 150025
- Fixes on .desktop (FCrozat)
- Import google-apps-installer

* Wed Mar 21 2007 Lenny Cartier <lenny@mandriva.com> 0.3-1mdv2007.1
- fix categories
- use Terminal=true rather than explicit xterm
- rename

* Mon Mar 19 2007 Lenny Cartier <lenny@mandriva.com> 0.2-1mdv2007.1
- remove desktop icons, then move to menus
- use wget for both

* Tue Mar 13 2007 Lenny Cartier <lenny@mandriva.com> 0.1-1mdv2007.1
- new
- add GoogleEarthInstall & GooglePicasaInstall shortcuts
