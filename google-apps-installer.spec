%define name	google-apps-installer
%define version	0.3
%define release %mkrel 2

Summary:	Desktop links to install the wonderful Google Apps
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
This is a set of icons for the default desktop, used to install the wonderful 
Google Apps.

For now :
- GoogleEarth
- Google Picasa

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
Exec=sh -c "wget http://api.mandriva.com/3rd-party/200701/downloadURL/GoogleEarth -O GoogleEarthLinux.bin && sh +x GoogleEarthLinux.bin"
Categories=X-MandrivaLinux-Internet;
EOF

cat > %buildroot/%_datadir/applications/googlepicasainstall.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Icon=mandrake
Name=Google Picasa Install
Type=Application
Terminal=true
Exec=sh -c "wget http://api.mandriva.com/3rd-party/200701/downloadURL/GooglePicasa -O GooglePicasa.rpm && gurpmi GooglePicasa.rpm"
Categories=X-MandrivaLinux-Multimedia-Graphics;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_datadir/applications/*


