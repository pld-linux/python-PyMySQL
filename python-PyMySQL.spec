#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	PyMySQL
Summary:	Pure Python MySQL Client
Name:		python-%{module}
Version:	0.7.4
Release:	10
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/PyMySQL/PyMySQL/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	e5d21154a71e5f6e73bcb3fd7659c642
URL:		https://github.com/PyMySQL/PyMySQL
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a pure-Python MySQL client library.

The goal of PyMySQL is to be a drop-in replacement for MySQLdb and
work on CPython, PyPy and IronPython.

%package -n python3-%{module}
Summary:	Pure Python MySQL Client
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package contains a pure-Python MySQL client library.

The goal of PyMySQL is to be a drop-in replacement for MySQLdb and
work on CPython, PyPy and IronPython.

%prep
%setup  -q -n PyMySQL-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pymysql/tests
%endif

%if %{with python3}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pymysql/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst CHANGELOG LICENSE
%{py_sitescriptdir}/pymysql
%{py_sitescriptdir}/PyMySQL-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst CHANGELOG LICENSE
%{py3_sitescriptdir}/pymysql
%{py3_sitescriptdir}/PyMySQL-%{version}-py*.egg-info
%endif
