Name:		texlive-handout
Version:	43962
Release:	1
Summary:	Create handout for auditors of a talk
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/handout
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/handout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/handout.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In some fields of scholarship, a beamer does not offer good
support when giving a talk in a proceeding. For example, in
classical philology, the main sources are text, and it will be
better to distribute a handout to the audience with extracts of
the texts about which we will talk. The package supports
preparation of such handouts when writing the talk.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/handout/handout.sty
%doc %{_texmfdistdir}/doc/latex/handout/README
%doc %{_texmfdistdir}/doc/latex/handout/examples/example.bib
%doc %{_texmfdistdir}/doc/latex/handout/examples/example1-minimal.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example1-minimal.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example2-cancel-quotation.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example2-cancel-quotation.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example3-defined-path.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example3-defined-path.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example4-sectioning.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example4-sectioning.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example5-numbering.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example5-numbering.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example6-not-and-only.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example6-not-and-only.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/example7-biblatex.pdf
%doc %{_texmfdistdir}/doc/latex/handout/examples/example7-biblatex.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/latexmkrc
%doc %{_texmfdistdir}/doc/latex/handout/examples/makefile
%doc %{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583-not-and-only.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583b.tex
%doc %{_texmfdistdir}/doc/latex/handout/examples/txt/Richard_Simon_NT.tex
%doc %{_texmfdistdir}/doc/latex/handout/handout.pdf
%doc %{_texmfdistdir}/doc/latex/handout/handout.tex
%doc %{_texmfdistdir}/doc/latex/handout/latexmkrc
%doc %{_texmfdistdir}/doc/latex/handout/makefile

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
