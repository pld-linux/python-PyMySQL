Summary:	Pure Python MySQL Client
Name:		python-PyMySQL
Version:	0.4
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/downloads/petehunt/PyMySQL/PyMySQL-%{version}.tar.gz
# Source0-md5:	4bc27e750f5d16e1e6169ad43b2c3568
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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/{PyMySQL/{constants/,},}*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{py_sitescriptdir}/PyMySQL-*.egg-info
%{py_sitescriptdir}/pymysql
