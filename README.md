# PyRTF3 - Rich Text Format Document Generation

This is a fork from the PyPI downloadable tarball `PyRTF3-0.47.5.tar.gz` with some clean-up.

## Overview

PyRTF is a set of python classes that make it possible to produce RTF documents from python programs. The library has no external dependancies and in my own testing has proved reliable and fast. Three examples are included in the release that demonstrate some of the features of the library, I'll be adding to these when I can.

PyRTF has been tested on the following OS's; W2K, WinXP, GNU/Linux, OpenBSD, FreeBSD and on the following Word Processors; OpenOffice, Word95, Word97, Word2000, WordXP and MacWord (not sure which version).

## Features

### Styles

A standard style sheet is provided but custom style sheets can be created which makes it possible to create suites of documents that conform to organisational guidelines.

Styles can be overridden down to almost any level, so the basic structure of the document can rely on the style sheet and only those areas that need to be different can be modified. For example bold, italic, underlining, etc can be applied to only the text items that require it.

### Document Sections

Documents can contain multiple sections, each section can have its own page size, style sheet, header and footer. Headers and footers that apply only to the first page of a section are supported.

### Tables

There is extensive support for tables, almost all of the table features provided by RTF are represented in PyRTF. Tables are built up from earlier building blocks so once you are familiar with the basics, tables are relatively easy to handle.

### Images

PNG and JPG images are supported.

Original Author: Simon Cusack, scusack@sourceforge.net

