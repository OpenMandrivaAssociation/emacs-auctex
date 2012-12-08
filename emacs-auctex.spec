%define	rname	auctex

Summary: 	Enhanced LaTeX mode for GNU Emacs
Name: 		emacs-auctex
Version: 	11.86
Release:	4
License: 	GPLv3+
Group: 		Editors
Source:		http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.zip
URL: 		http://www.gnu.org/software/auctex/
Requires: 	emacs 
Requires: 	tetex-latex
BuildRequires: 	emacs-X11
BuildRequires: 	tetex-latex tetex-dvips
BuildArchitectures: noarch
Provides:	    %rname = %version-%release
Obsoletes:	    %rname
Provides: 	    preview-latex-common preview-latex-emacs
Obsoletes: 	    preview-latex-common preview-latex-emacs

%description
AUCTeX is a comprehensive customizable integrated environment for
writing input files for TeX, LaTeX, ConTeXt, Texinfo, and docTeX using
GNU Emacs.

%prep
%setup -q -n %rname-%version

%build
%configure --with-emacs
%make

%install
%__rm -rf %{buildroot}

install -d $RPM_BUILD_ROOT{%{_datadir}/emacs/site-lisp,%{_infodir}}
%makeinstall autodir=$RPM_BUILD_ROOT/var/lib/auctex

# This is already in tetex-latex:
%__rm -rf %buildroot%_datadir/texmf/tex/latex/preview
# What's this for?
%__rm -rf %buildroot/var/lib/auctex
# Don't install reference card:
%__rm -rf %buildroot%_datadir/doc/auctex

#perl -pi -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT/%_datadir/emacs/site-lisp/tex-site.el
install -d $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d
echo "(if (string-match \"GNU Emacs\" (version)) (require 'tex-site))" >> $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d/%rname.el

%files
%defattr(-,root,root)
%doc RELEASE COPYING INSTALL README TODO FAQ CHANGES
%_infodir/*
%_datadir/emacs/site-lisp/%rname
%_datadir/emacs/site-lisp/auctex.el
%_datadir/emacs/site-lisp/preview-latex.el
%_datadir/emacs/site-lisp/tex-site.el
%_datadir/texmf/doc/latex/styles/preview.dvi
%config(noreplace) %_sysconfdir/emacs/site-start.d/%{rname}*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 11.86-3mdv2011.0
+ Revision: 664143
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 11.86-2mdv2011.0
+ Revision: 605102
- rebuild

* Wed Feb 24 2010 Lev Givon <lev@mandriva.org> 11.86-1mdv2010.1
+ Revision: 510489
- Update to 11.86.

* Mon Jun 08 2009 Lev Givon <lev@mandriva.org> 11.85-2mdv2010.0
+ Revision: 384140
- Remove emacs version dependency.

* Mon Jun 30 2008 Lev Givon <lev@mandriva.org> 11.85-1mdv2009.0
+ Revision: 230405
- Update to 11.85.

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 11.84-3mdv2009.0
+ Revision: 220723
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 11.84-2mdv2008.1
+ Revision: 149696
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 11.84-1mdv2008.0
+ Revision: 18876
- 11.84 (rebuild for new era)


* Tue May 02 2006 Götz Waschk <waschk@mandriva.org> 11.82-2mdk
- remove files that conflict with latex

* Tue May 02 2006 Götz Waschk <waschk@mandriva.org> 11.82-1mdk
- merge with preview-latex
- update file list
- fix build
- New release 11.82

* Mon Oct 10 2005 Giuseppe Ghibò <ghibo@mandriva.com> 11.51-4mdk
- Rebuild for emacs 21.4 to fix dependencies problems.
- use explicit emacs_version   anymore.

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 11.51-3mdk
- rebuild for new emacs

* Wed Aug 25 2004 Götz Waschk <waschk@linux-mandrake.com> 11.51-2mdk
- fix configure call
- fix buildrequires

* Tue Aug 17 2004 Pixel <pixel@mandrakesoft.com> 11.51-1mdk
- new release
- merge a little with upstream srpm

