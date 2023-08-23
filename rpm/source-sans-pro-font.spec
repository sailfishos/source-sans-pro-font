Name:       source-sans-pro-font
Summary:    Source Sans Pro Light and Source Sans Pro ExtraLight fonts
Version:    1.038
Release:    1
Group:      User Interface/X
License:    OFL
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
URL:        https://github.com/adobe/source-sans-pro
Requires:   fontconfig

%define fontname source-sans-pro

%description    
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/%{fontname}
install -m 0644 -p *.ttf %{buildroot}/%{_datadir}/fonts/%{fontname}

%post
{
    [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
} &> /dev/null || :

%files
%defattr(-,root,root,0755)
%license LICENSE.txt
%{_datadir}/fonts/%{fontname}

