"""" START Vundle Configuration 

" Disable file type for vundle
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Utility
" Plugin 'scrooloose/nerdtree'
Plugin 'Valloric/YouCompleteMe'
Plugin 'davidhalter/jedi-vim'
Plugin 'mileszs/ack.vim'
Plugin 'sk1418/QFGrep'
" Generic Programming Support 
Plugin 'MarcWeber/vim-addon-mw-utils'
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'
" Plugin 'jakedouglas/exuberant-ctags'
Plugin 'honza/vim-snippets'
Plugin 'mattn/emmet-vim'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'tpope/vim-surround'
Plugin 'flazz/vim-colorschemes'
Plugin 'romainl/Apprentice'
Plugin 'w0rp/ale'
call vundle#end()            " required
filetype plugin indent on    " required
"""" END Vundle Configuration 



" let g:ycm_autoclose_preview_window_after_completion=1
" map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

let mapleader=";"
map <C-i> "+p
map <C-c> "+y
map<esc> :w<enter>
noremap <Leader>j :NERDTreeToggle<enter>
noremap <Leader>w :cd %:p:h<enter>
map <Leader>b :ls<CR>:b<Space>
map <Leader>p :CtrlP<CR>:
map <Leader>c :ALEToggle<CR>
map <Leader>a :cp<CR>
map <Leader>; :cn<CR>

" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
let g:UltiSnipsExpandTrigger="<c-j>"
let g:UltiSnipsListSnippets="<c-l>"
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-k>"
let g:UltiSnipsSnippetsDir="~/.vim/snips"

" ale linter settings
" Write this in your vimrc file
" let g:ale_lint_on_text_changed = 'never'
" You can disable this option too
" if you don't want linters to run on opening a file
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'never'


" let g:jedi#popup_on_dot = 0
let g:jedi#show_call_signatures = "2"
let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_collect_identifiers_from_tags_files = 1

set nu
set term=ansi
let NERDTreeIgnore = ['\.pyc$']

if has('gui_running')
  set guioptions -=T
  set guifont=Monospace\ 12
  colorscheme codeschool
else
  set t_Co=256
  colorscheme zenburn 
endif

autocmd FileType python setlocal completeopt-=preview
autocmd BufNewFile * silent! 0r ~/.vim/templates/%:e.tpl
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=120 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |

au BufNewFile,BufRead *.js
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=120 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |

au BufNewFile,BufRead *.*
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=120 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |


set langmap=АA,БB,ЦC,ДD,ЕE,ФF,ГG,ХH,ИI,ЙJ,КK,ЛL,МM,НN,ОO,ПP,ЯQ,РR,СS,ТT,УU,ЖV,ВW,ЬX,ЫY,ЗZ,аa,бb,цc,дd,еe,фf,гg,хh,иi,йj,кk,лl,мm,нn,оo,пp,яq,рr,сs,тt,уu,жv,вw,ьx,ыy,зz,Ч: 

function! HelloVim()
    py3 hello.py
endfunc
