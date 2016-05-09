%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hirb-unicode-steakknife

Summary: Unicode support for hirb
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.0.7
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem-hirb >= 0.5
Requires: %{?scl_prefix}rubygem-hirb < 1
Requires: %{?scl_prefix}rubygem-unicode-display_width >= 0.2.0
Requires: %{?scl_prefix}rubygem-unicode-display_width < 2.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(hirb-unicode-steakknife) = %{version}

%description
Unicode support for hirb

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/.gitignore

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/gem-public_cert.pem

%changelog
