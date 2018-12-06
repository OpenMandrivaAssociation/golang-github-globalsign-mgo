# Run tests in check section
# Tests require Internet access
%bcond_with check

%global goipath         github.com/globalsign/mgo
%global commit          113d3961e7311526535a1ef7042196563d442761

%global common_description %{expand:
The MongoDB driver for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        The MongoDB driver for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(gopkg.in/tomb.v2)

%if %{with check}
BuildRequires: golang(gopkg.in/check.v1)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git113d396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git113d396
- Bump to commit 113d3961e7311526535a1ef7042196563d442761

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416gitf76e4f9
- First package for Fedora

