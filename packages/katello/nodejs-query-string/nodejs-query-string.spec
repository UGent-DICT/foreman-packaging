%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name query-string

Name: %{?scl_prefix}nodejs-query-string
Version: 6.1.0
Release: 2%{?dist}
Summary: Parse and stringify URL query strings
License: MIT
Group: Development/Libraries
URL: https://github.com/sindresorhus/query-string#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(decode-uri-component) >= 0.2.0
Requires: %{?scl_prefix}npm(decode-uri-component) < 0.3.0
Requires: %{?scl_prefix}npm(strict-uri-encode) >= 2.0.0
Requires: %{?scl_prefix}npm(strict-uri-encode) < 3.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc readme.md

%changelog
* Sun Oct 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.1.0-2
- Update to handle building for SCL

* Fri Sep 14 2018 Eric D. Helms <ericdhelms@gmail.com> 6.1.0-1
- Add nodejs-query-string generated by npm2rpm using the bundle strategy
