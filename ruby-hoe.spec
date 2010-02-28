%define pkgname hoe
Summary:	Rake/rubygems helper for project Rakefiles
Name:		ruby-%{pkgname}
Version:	2.5.0
Release:	0.1
License:	MIT/Ruby License
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7afb2f143fbeff68d0bfa46cd1d51623
Group:		Development/Languages
URL:		http://rubyforge.org/projects/seattlerb/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
...

%package rdoc
Summary:	Documentation files for %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.txt  -o -print | xargs touch --reference %{SOURCE0}

%{__sed} -i -e 's|/usr/bin/env ruby|%{__ruby}|' bin/sow

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -rf ri/{File,Rake,String}
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc History.txt README.txt Hoe.pdf
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/%{pkgname}.rb
%{ruby_rubylibdir}/%{pkgname}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Hoe
