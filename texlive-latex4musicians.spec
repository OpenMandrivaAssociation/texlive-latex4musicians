Name:		texlive-latex4musicians
Version:	49759
Release:	1
Summary:	A guide for combining LaTeX and music
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex4musicians
License:	fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4musicians.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4musicians.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This guide, "LaTeX for Musicians", explains how to create LaTeX
documents that include several kinds of music elements: music
symbols, song lyrics, guitar chords diagrams, lead sheets,
music excerpts, guitar tablatures, multi-page scores.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex4musicians

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
