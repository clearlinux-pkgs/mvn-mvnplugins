#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mvnplugins
Version  : 1.9
Release  : 1
URL      : https://repo1.maven.org/maven2/org/fusesource/mvnplugins/fuse-jxr-skin/1.9/fuse-jxr-skin-1.9.jar
Source0  : https://repo1.maven.org/maven2/org/fusesource/mvnplugins/fuse-jxr-skin/1.9/fuse-jxr-skin-1.9.jar
Source1  : https://repo1.maven.org/maven2/org/fusesource/mvnplugins/fuse-jxr-skin/1.9/fuse-jxr-skin-1.9.pom
Source2  : https://repo1.maven.org/maven2/org/fusesource/mvnplugins/mvnplugins/1.9/mvnplugins-1.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-mvnplugins-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-mvnplugins package.
Group: Data

%description data
data components for the mvn-mvnplugins package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/mvnplugins/1.9
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/mvnplugins/mvnplugins/1.9


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9/fuse-jxr-skin-1.9.jar
/usr/share/java/.m2/repository/org/fusesource/mvnplugins/fuse-jxr-skin/1.9/fuse-jxr-skin-1.9.pom
/usr/share/java/.m2/repository/org/fusesource/mvnplugins/mvnplugins/1.9/mvnplugins-1.9.pom
