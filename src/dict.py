DICT = {
    "MAIN" : lambda content : "\\documentclass[a4paper,12pt]{article}\n" + 
                              "\\usepackage[utf8]{inputenc}\n" + 
                              "\\usepackage{hyperref}\n" +
                              "\\usepackage{graphics}\n" +
                              "\\usepackage[spanish]{babel}\n" +
                              "\\usepackage{tabular}\n" +
                              "\\begin{document}\n" + content + "\end\{document\}",
    "BLOCK" : lambda content : content + "\n",
    "H1" : lambda text : "\\section{" + text + "}\n",
    "H2" : lambda text : "\\subsection{" + text + "}\n",
    "H3" : lambda text : "\\subsubsection{" + text + "}\n",
    "OLIST" : lambda items : "\\begin{enumerate}\n" + items + "\n\\end{enumerate}\n",
    "ULIST" : lambda items : "\\begin{itemize}\n" + items + "\n\\end{itemize}\n",
    "TABLE" : lambda content : "\\begin{table}[H]\n\\centering\n" + content + "\n\\end{table}",
    "BOLD" : lambda text : "\\textbf{" + text + "}",
    "ITALIC" : lambda text : "\\textit{" + text + "}",
    "URL" : lambda url, text : "\\href{" + url + "}{" + text + "}",
    "IMAGE" : lambda path, caption : "\\begin{figure}[H]\n\\centering\n\\includegraphics{" + 
                                  path + "}\n\\caption{" + caption + "}\n\\end{figure}",
}

print(DICT["MAIN"]("test"))