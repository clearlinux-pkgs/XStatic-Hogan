#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Hogan
Version  : 2.0.0.3
Release  : 27
URL      : https://files.pythonhosted.org/packages/1b/25/4535fe5c20dd42445aee7b1a3f0b572ebda0e3979e70a8c218eec2d5d09d/XStatic-Hogan-2.0.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/25/4535fe5c20dd42445aee7b1a3f0b572ebda0e3979e70a8c218eec2d5d09d/XStatic-Hogan-2.0.0.3.tar.gz
Summary  : Hogan 2.0.0 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-Hogan-python = %{version}-%{release}
Requires: XStatic-Hogan-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
-------------
        
        Hogan JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Hogan package.
Group: Default
Requires: XStatic-Hogan-python3 = %{version}-%{release}
Provides: xstatic-hogan-python

%description python
python components for the XStatic-Hogan package.


%package python3
Summary: python3 components for the XStatic-Hogan package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_hogan)

%description python3
python3 components for the XStatic-Hogan package.


%prep
%setup -q -n XStatic-Hogan-2.0.0.3
cd %{_builddir}/XStatic-Hogan-2.0.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587077044
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
