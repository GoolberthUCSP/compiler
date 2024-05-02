productions = {
    "DOCUMENT" : [["BLOCKS", "EOF"]],
    "BLOCKS" : [["BLOCK", "BLOCKSEP", "BLOCKS"], 
                ["epsilon"]],
    "BLOCK" : [["H1", "TEXT"], 
               ["H2", "TEXT"], 
               ["H3", "TEXT"], 
               ["TEXT"], 
               ["OLIST"], 
               ["ULIST"], 
               ["IMAGE"], 
               ["TABLE"], 
               ["URL"], 
               ["COMMENT"]],
    "TEXT" : [["SENTENCE", "TEXT"],
              ["epsilon"]],
    "SENTENCE" : [["STRING"],
                  ["BOLDMARK", "STRING", "BOLDMARK"],
                  ["ITALICMARK", "STRING", "ITALICMARK"]],
    "STRING" : [["TEXTMARK", "ALPHA", "TEXTMARK"]],
    "OLIST" : [["OLISTITEM", "OLIST'"]],
    "OLIST'" : [["NEWLINE", "OLIST"], 
                ["epsilon"]],
    "OLISTITEM" : [["OLISTMARK", "TEXT"]],
    "ULIST" : [["ULISTITEM", "ULIST'"]],
    "ULIST'" : [["NEWLINE", "ULIST"], 
                ["epsilon"]],
    "ULISTITEM" : [["ULISTMARK", "TEXT"]],
    "TABLE" : [["TABLEHEAD", "TABLEBODY"]],
    "TABLEHEAD" : [["TABLEHEADSEP", "TEXT", "TABLEHEAD'"]],
    "TABLEHEAD'" : [["TABLEHEAD"], 
                    ["NEWLINE"]],
    "TABLEBODY" : [["TABLEBODYSEP", "TEXT", "TABLEBODY'"]],
    "TABLEBODY'" : [["TABLEBODY"],
                    ["NEWLINE", "TABLEBODY"],
                    ["epsilon"]],
    "IMAGE" : [["IMAGEMARK", "OPENBRACKET", "TEXT", "CLOSEBRACKET","OPENPARENT", "TEXT", "CLOSEPARENT"]],
    "URL" : [["OPENBRACKET", "TEXT", "CLOSEBRACKET","OPENPARENT", "TEXT", "CLOSEPARENT"]],
    "COMMENT" : [["COMMENTOPEN", "ALPHA", "COMMENTCLOSE"]],
    "OLISTMARK" : "+",
    "ULISTMARK" : "-",
    "IMAGEMARK" : "!",
    "H1" : "#",
    "H2" : "##",
    "H3" : "###",
    "BOLDMARK" : "**",
    "ITALICMARK" : "*",
    "TEXTMARK" : "'",
    "NEWLINE" : "\n", # Cambiar a n para imprimir tabla
    "BLOCKSEP" : "\n\n", # Cambiar a nn para imprimir tabla
    "TABLEHEADSEP" : "&",
    "TABLEBODYSEP" : "|",
    "OPENBRACKET" : "[",
    "CLOSEBRACKET" : "]",
    "OPENPARENT" : "(",
    "CLOSEPARENT" : ")",
    "COMMENTOPEN" : "/*",
    "COMMENTCLOSE" : "*/",
    "ALPHA" : "a", # DEBUGGING
    "EOF" : "$"
}