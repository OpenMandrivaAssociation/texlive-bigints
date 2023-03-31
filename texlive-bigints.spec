Name:		texlive-bigints
Version:	29803
Release:	2
Summary:	Writing big integrals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigints
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities for drawing big integral signs
when needed. An example would be when the integrand is a
matrix.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bigints/bigints.sty
%doc %{_texmfdistdir}/doc/latex/bigints/Makefile
%doc %{_texmfdistdir}/doc/latex/bigints/README
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.forlisting
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.pdf
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.tex
%doc %{_texmfdistdir}/doc/latex/bigints/perso.ist

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
