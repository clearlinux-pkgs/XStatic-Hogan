#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Hogan
Version  : 2.0.0.2
Release  : 14
URL      : https://pypi.python.org/packages/source/X/XStatic-Hogan/XStatic-Hogan-2.0.0.2.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Hogan/XStatic-Hogan-2.0.0.2.tar.gz
Summary  : Hogan 2.0.0 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Hogan-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Hogan
--------------
Hogan JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Hogan package.
Group: Default

%description python
python components for the XStatic-Hogan package.


%prep
%setup -q -n XStatic-Hogan-2.0.0.2

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
