# revision 17223
# category Package
# catalog-ctan /macros/latex/contrib/bigints
# catalog-date 2010-02-26 01:00:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-bigints
Version:	20100226
Release:	2
Summary:	Writing big integrals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigints
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100226-2
+ Revision: 749701
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100226-1
+ Revision: 717947
- texlive-bigints
- texlive-bigints
- texlive-bigints
- texlive-bigints
- texlive-bigints

