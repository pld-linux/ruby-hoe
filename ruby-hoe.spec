#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname hoe
Summary:	Rake/rubygems helper for project Rakefiles
Name:		ruby-%{pkgname}
Version:	2.5.0
Release:	1
License:	MIT/Ruby License
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7afb2f143fbeff68d0bfa46cd1d51623
URL:		http://www.zenspider.com/projects/hoe.html
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-minitest >= 5.0
BuildRequires:	ruby-minitest < 6
BuildRequires:	ruby-rdoc >= 4.0
BuildRequires:	ruby-rdoc < 5
%endif
Requires:	ruby-rubygems >= 1.4
Requires:	ruby-rake >= 0.8
Requires:	ruby-rake < 11.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you
manage and maintain, and release your project and includes a dynamic
plug-in system allowing for easy extensibility. Hoe ships with
plug-ins for all your usual project tasks including rdoc generation,
testing, packaging, and deployment.

%package rdoc
Summary:	Documentation files for %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -rf ri/{File,Rake,String,Object}
rm -f ri/created.rid
rm -f ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc History.txt README.txt Hoe.pdf
%attr(755,root,root) %{_bindir}/sow
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Hoe
