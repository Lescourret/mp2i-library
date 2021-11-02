(*Calcul de la moyenne d'une liste*)

let rec somme = function
    | [] -> 0
    | e::q -> e + somme q;;

(* on définit tout d'abord une fonction qui somme l'ensemble des termes de la liste puis on divise par la taille de la liste. *)
let moyenne l = (somme l) / (List.length l);;
