" General settings
syntax on               " Enable syntax highlighting
filetype plugin on      " Enable filetype-specific plugins
filetype indent on      " Enable filetype-specific indentation
colorscheme blue        " Set color scheme
set tabstop=2           " Number of spaces that a <Tab> in the file counts for, adjusted for YAML
set softtabstop=2       " See tabstop, but for the use of <BS>, adjusted for YAML
set shiftwidth=2        " Size of an indent, adjusted for YAML
set expandtab           " Use spaces instead of tabs, crucial for YAML
set autoindent          " Copy indent from current line when starting a new line
set smartindent         " Make indenting smarter again
set foldmethod=indent   " Set fold method to indent
set foldcolumn=2        " Set fold column width
set clipboard=unnamedplus " Use system clipboard

" Python-specific settings
augroup python_settings
    autocmd!
    autocmd FileType python setlocal expandtab tabstop=4 shiftwidth=4 softtabstop=4
    autocmd FileType python setlocal autoindent smartindent
    autocmd FileType python setlocal number
    autocmd FileType python setlocal cursorline cursorcolumn
    autocmd FileType python setlocal showmatch
    autocmd FileType python setlocal foldmethod=indent
    autocmd FileType python setlocal foldlevelstart=10 foldnestmax=10
    " Python enhancements
    autocmd FileType python setlocal list
    autocmd FileType python setlocal listchars=tab:>-,trail:·,extends:#,nbsp:.
    autocmd FileType python setlocal ignorecase smartcase
    autocmd FileType python setlocal incsearch hlsearch
    autocmd FileType python colorscheme blue
augroup END

" YAML-specific settings
augroup yaml_settings
    autocmd!
    autocmd FileType yaml setlocal expandtab tabstop=2 shiftwidth=2 softtabstop=2
    autocmd FileType yaml setlocal autoindent smartindent
    autocmd FileType yaml setlocal number
    autocmd FileType yaml colorscheme darkblue
    " Ensure trailing spaces are visible since they can cause errors in YAML
    autocmd FileType yaml setlocal listchars=tab:>-,trail:·
    autocmd FileType yaml setlocal list
augroup END



# to apply a customization to a file type, you can use autocmd:

autocmd FileType python set shiftwidth=4

colorscheme darkblue
colorscheme default
colorscheme delek
colorscheme desert
colorscheme elflord
colorscheme evening
colorscheme industry
colorscheme koehler
colorscheme morning
colorscheme murphy
colorscheme pablo
colorscheme peachpuff
colorscheme ron
colorscheme shine
colorscheme slate
colorscheme torte
colorscheme zellner
# Plug 'davidhalter/jedi-vim'
# call plug#end()