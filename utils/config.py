from tree_sitter import Language
import tree_sitter_ruby as tsruby
import tree_sitter_python as tspy
import tree_sitter_javascript as tsjs
import tree_sitter_java as tsjava


# Tree-sitter 언어 라이브러리 정의
LANGUAGES = {
    'rb': Language(tsruby.language()),
    'py': Language(tspy.language()),
    'js': Language(tsjs.language()),
    'java': Language(tsjava.language())
}
