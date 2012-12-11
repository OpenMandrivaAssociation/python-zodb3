Name:		python-zodb3
Version:	3.10.5
Release:	1
Group:		Development/Python
License:	Zope Public License
Summary:	Zope Object Database: object database and persistence
Source:		http://pypi.python.org/packages/source/Z/ZODB3/ZODB3-3.10.5.tar.gz
URL:		http://pypi.python.org/pypi/ZODB3/3.10.5

BuildRequires:	python-devel
BuildRequires:	python-setuptools

Requires:	python-transaction
Requires:	python-zc.lockfile
Requires:	python-zope.proxy

%description
The Zope Object Database provides an object-oriented database for
Python that provides a high-degree of transparency. Applications
can take advantage of object database features with few, if any,
changes to application logic. ZODB includes features such as a
plugable storage interface, rich transaction support, and undo.

%prep
%setup -q -n ZODB3-%{version}

%build

%install
PYTHONDONTWRITEBYTECODE= \
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
sed -i 's/.*egg-info$//' INSTALLED_FILES

%files -f INSTALLED_FILES


%changelog
* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 3.9.0b4-3mdv2011.0
+ Revision: 593446
+ rebuild (emptylog)

* Fri Aug 07 2009 Paulo Andrade <pcpa@mandriva.com.br> 3.9.0b4-2mdv2010.0
+ Revision: 411009
+ rebuild (emptylog)

* Wed Aug 05 2009 Paulo Andrade <pcpa@mandriva.com.br> 3.9.0b4-1mdv2010.0
+ Revision: 410409
- Import python-zodb3 version 3.9.0b4
- python-zodb3

