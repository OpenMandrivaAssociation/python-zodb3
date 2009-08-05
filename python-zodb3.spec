Name:		python-zodb3
Version:	3.9.0b4
Release:	%mkrel 1
Group:		Development/Python
License:	Zope Public License
Summary:	Zope Object Database: object database and persistence
# md5=d93e8612e727874255a3f7fa467c7518
Source:		http://pypi.python.org/packages/source/Z/ZODB3/ZODB3-3.9.0b4.tar.gz
URL:		http://pypi.python.org/pypi/ZODB3/3.9.0b4
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel

%description
The Zope Object Database provides an object-oriented database for
Python that provides a high-degree of transparency. Applications
can take advantage of object database features with few, if any,
changes to application logic. ZODB includes features such as a
plugable storage interface, rich transaction support, and undo.

%prep
%setup -q -q -n ZODB3-%{version}

%build

%install
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
