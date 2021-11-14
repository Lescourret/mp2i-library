(*insérer un élément dans une liste*)

let rec insere e l = match l with
    | [] -> [e] (*cas de base*)
    | x::q -> if e < x then e::l (*on regarde où plasser e : on le compare donc aux éléments de la liste triée, si e plus petitque le premier élément de la liste alors on le fusionne à la liste*)
else x::insere e (*sinon on le compare à l'élément suivant, et ainsi de suite.*)
