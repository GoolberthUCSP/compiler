productions = {
    "DOCUMENT" : [["BLOCKS", "EOF"]],
    "BLOCKS" : [["BLOCK", "BLOCKSEP", "BLOCKS"], 
                ["EPSILON"]],
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
              ["EPSILON"]],
    "SENTENCE" : [["STRING"],
                  ["BOLDMARK", "STRING", "BOLDMARK"],
                  ["ITALICMARK", "STRING", "ITALICMARK"]],
    "STRING" : [["TEXTMARK", "ALPHA", "TEXTMARK"]],
    "OLIST" : [["OLISTITEM", "NEWLINE", "OLIST"], # DELETE OLISTPRIME PRODUCTION
               ["EPSILON"]],
    "OLISTITEM" : [["OLISTMARK", "TEXT"]],
    "ULIST" : [["ULISTITEM", "NEWLINE", "ULIST"], # DELETE ULISTPRIME PRODUCTION
               ["EPSILON"]],
    "ULISTITEM" : [["ULISTMARK", "TEXT"]],
    "TABLE" : [["TABLEHEAD", "NEWLINE", "TABLEBODY"]],
    "TABLEHEAD" : [["TABHEADSEP", "TEXT", "TABLEHEAD"],
                   ["EPSILON"]],
    "TABLEBODY" : [["TABLEBODYROW", "NEWLINE", "TABLEBODY"],
                   ["EPSILON"]],
    "TABLEBODYROW" : [["TABLEBODYSEP", "TEXT", "TABLEBODYROW"], # ADDED TABLEBORYROW INSTEAD OF TABLEBODYPRIME
                      ["EPSILON"]],
    "IMAGE" : [["IMAGEMARK", "OPENBRACKET", "TEXT", "CLOSEBRACKET","OPENPARENT", "TEXT", "CLOSEPARENT"]],
    "URL" : [["OPENBRACKET", "TEXT", "CLOSEBRACKET","OPENPARENT", "TEXT", "CLOSEPARENT"]],
    "COMMENT" : [["COMMENTOPEN", "STRING", "COMMENTCLOSE"]],
    "OLISTMARK" : "+",
    "ULISTMARK" : "-",
    "IMAGEMARK" : "!",
    "H1" : "#",
    "H2" : "##",
    "H3" : "###",
    "BOLDMARK" : "**",
    "ITALICMARK" : "*",
    "TEXTMARK" : "'",
    "NEWLINE" : "\n",
    "BLOCKSEP" : "\n\n",
    "TABHEADSEP" : "&",
    "TABLEBODYSEP" : "|",
    "OPENBRACKET" : "[",
    "CLOSEBRACKET" : "]",
    "OPENPARENT" : "(",
    "CLOSEPARENT" : ")",
    "COMMENTOPEN" : "/*",
    "COMMENTCLOSE" : "*/",
    "ALPHA" : "alphabet", # DEBUGGING
    "EOF" : "$",
    "EPSILON" : ""
}