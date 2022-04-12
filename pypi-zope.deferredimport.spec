#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.deferredimport
Version  : 4.4
Release  : 23
URL      : https://files.pythonhosted.org/packages/50/0b/751237130777dc4497bd7c404b29c483efa7c39672a8796d7bfe4ef059cd/zope.deferredimport-4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/0b/751237130777dc4497bd7c404b29c483efa7c39672a8796d7bfe4ef059cd/zope.deferredimport-4.4.tar.gz
Summary  : zope.deferredimport allows you to perform imports names that will only be resolved when used in the code.
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.deferredimport-license = %{version}-%{release}
Requires: pypi-zope.deferredimport-python = %{version}-%{release}
Requires: pypi-zope.deferredimport-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.proxy)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=========================
``zope.deferredimport``
=========================
.. image:: https://img.shields.io/pypi/v/zope.deferredimport.svg
:target: https://pypi.python.org/pypi/zope.deferredimport/
:alt: Latest release

%package license
Summary: license components for the pypi-zope.deferredimport package.
Group: Default

%description license
license components for the pypi-zope.deferredimport package.


%package python
Summary: python components for the pypi-zope.deferredimport package.
Group: Default
Requires: pypi-zope.deferredimport-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.deferredimport package.


%package python3
Summary: python3 components for the pypi-zope.deferredimport package.
Group: Default
Requires: python3-core
Provides: pypi(zope.deferredimport)
Requires: pypi(setuptools)
Requires: pypi(zope.proxy)

%description python3
python3 components for the pypi-zope.deferredimport package.


%prep
%setup -q -n zope.deferredimport-4.4
cd %{_builddir}/zope.deferredimport-4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649799569
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.deferredimport
cp %{_builddir}/zope.deferredimport-4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.deferredimport/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.deferredimport/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
