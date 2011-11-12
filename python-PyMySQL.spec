Summary:	Pure Python MySQL Client
Name:		python-PyMySQL
Version:	0.5
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/downloads/petehunt/PyMySQL/PyMySQL-%{version}.tar.gz
# Source0-md5:	125e8a3449e05afcb04874a19673426b
URL:		http://www.pymysql.org/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a pure-Python MySQL client library.

The goal of pymysql is to be a drop-in replacement for MySQLdb and
work on CPython 2.3+, Jython, IronPython, PyPy and Python 3.

%prep
%setup  -q -n PyMySQL-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/PyMySQL-*.egg-info
%{py_sitescriptdir}/pymysql
