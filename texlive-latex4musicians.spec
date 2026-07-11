%global tl_name latex4musicians
%global tl_revision 49759

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	A guide for combining LaTeX and music
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex4musicians
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4musicians.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4musicians.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This guide, "LaTeX for Musicians", explains how to create LaTeX
documents that include several kinds of music elements: music symbols,
song lyrics, guitar chords diagrams, lead sheets, music excerpts, guitar
tablatures, multi-page scores.

