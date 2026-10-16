%define module nab_resolver

Name:		python-nab-resolver
Version:	0.0.21
Release:	1
Summary:	Generic PubGrub dependency-resolver core
License:	MIT
Group:		Development/Python
URL:		https://github.com/notatallshaw/nab
Source0:	https://files.pythonhosted.org/packages/source/n/nab-resolver/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Standard-library PubGrub solver used by nab.
pipdeptree 4 resolves installed packages through this stack.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
