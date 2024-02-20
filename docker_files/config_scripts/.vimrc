syntax on               " Enable syntax highlighting
filetype plugin on      " Enable filetype-specific plugins
filetype indent on      " Enable filetype-specific indentation
set tabstop=4           " Number of spaces that a <Tab> in the file counts for
set softtabstop=4       " See tabstop, but for the use of <BS>
set shiftwidth=4        " Size of an indent
set expandtab           " Use spaces instead of tabs
set autoindent          " Copy indent from current line when starting a new line
set smartindent         " Make indenting smarter again
call plug#begin('~/.vim/plugged')

Plug 'davidhalter/jedi-vim'
call plug#end()