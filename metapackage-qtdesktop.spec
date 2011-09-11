Summary:	Qt4-based desktop environment
Name:		metapackage-qtdesktop
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications
URL:		https://code.google.com/p/qtdesktop/
# TODO
#Requires:	qmailclient
#Requires:	qrdc
#Requires:	qtarc
#Requires:	qtftp
#Requires:	qtpdfview
#Requires:	qtrun
#Requires:	znotes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main goal of QtDesktop project is to get all usual applications,
X-platform (Linuxnix/Windows) and Qt4-based.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
