# revision 32048
# category Package
# catalog-ctan /language/japanese/bxcjkjatype
# catalog-date 2013-10-30 11:43:37 +0100
# catalog-license other-free
# catalog-version 0.2c
Name:		texlive-bxcjkjatype
Version:	0.2c
Release:	2
Summary:	Typeset Japanese with pdfLaTeX and CJK
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/bxcjkjatype
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a working configuration of the CJK
package, suitable for Japanese typesetting of moderate quality.
Moreover, it facilitates use of the CJK package for pLaTeX
users, by providing commands that are similar to those used by
the pLaTeX kernel and some other packages used with it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxcjkjatype/bxcjkjatype.sty
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/LICENSE
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/README
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/README-ja.md
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/sample-bxcjkjatype-beamer.pdf
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/sample-bxcjkjatype-beamer.tex
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/sample-bxcjkjatype.pdf
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype/sample-bxcjkjatype.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
